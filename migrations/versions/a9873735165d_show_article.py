"""show article

Revision ID: a9873735165d
Revises: b3350ca45924
Create Date: 2016-08-12 09:31:35.316973

"""

# revision identifiers, used by Alembic.
revision = 'a9873735165d'
down_revision = 'b3350ca45924'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_articles_timestamp'), 'articles', ['timestamp'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_articles_timestamp'), table_name='articles')
    op.drop_table('articles')
    ### end Alembic commands ###