"""empty message

Revision ID: a0ca0b770478
Revises: 5d4f83fbfee1
Create Date: 2021-08-26 15:12:42.586428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0ca0b770478'
down_revision = '5d4f83fbfee1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friend',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userfriend_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('url_image', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('friend')
    # ### end Alembic commands ###