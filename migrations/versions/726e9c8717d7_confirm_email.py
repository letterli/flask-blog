"""Confirm Email

Revision ID: 726e9c8717d7
Revises: 4b7586b684da
Create Date: 2016-08-05 16:39:00.537736

"""

# revision identifiers, used by Alembic.
revision = '726e9c8717d7'
down_revision = '4b7586b684da'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###
