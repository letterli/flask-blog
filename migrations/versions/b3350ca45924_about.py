"""about

Revision ID: b3350ca45924
Revises: 1a4d95ee037d
Create Date: 2016-08-11 11:02:39.789550

"""

# revision identifiers, used by Alembic.
revision = 'b3350ca45924'
down_revision = '1a4d95ee037d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('last_access_time', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('location', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('registed_time', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'registed_time')
    op.drop_column('users', 'name')
    op.drop_column('users', 'location')
    op.drop_column('users', 'last_access_time')
    op.drop_column('users', 'about_me')
    ### end Alembic commands ###