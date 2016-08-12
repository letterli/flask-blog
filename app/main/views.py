from flask import render_template, abort, flash, redirect, url_for, current_app, request
from flask_login import login_required, current_user
from ..models import User, Role, Permission, Article
from .forms import EditProfileForm, EditProfileAdminForm, ArticleForm
from . import main
from .. import db


@main.route('/', methods=['GET', 'POST'])
def index():
    form = ArticleForm()
    if form.validate_on_submit() and current_user.can(Permission.WRITE_ARTICLES):
        article = Article(body=form.body.data, 
                                author=current_user._get_current_object())
        db.session.add(article)
        return redirect(url_for('main.index'))
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.timestamp.desc()).paginate(
            page, per_page=current_app.config['FLASK_ARTICLES_PER_PAGE'],
            error_out=False)
    articles = pagination.items
    return render_template('index.html', form=form, articles=articles, pagination=pagination)


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    articles = user.articles.order_by(Article.timestamp.desc()).all()
    return render_template('user.html', user=user, articles=articles)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('main.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        flash('The profile has been updated.')
        return redirect(url_for('main.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)


@main.route('/article/<int:id>')
def article(id):
    article = Article.query.get_or_404(id)
    return render_template('article.html', articles=[article])


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    article = Article.query.get_or_404(id)
    if current_user != article.author and \
            not current_user.can(Permission.ADMINISTER):
        abort(403)
    form = ArticleForm()
    if form.validate_on_submit():
        article.body = form.body.data
        db.session.add(article)
        flash('The article has been updated.')
        return redirect(url_for('.article', id=article.id))
    form.body.data = article.body
    return render_template('edit_article.html', form=form)
