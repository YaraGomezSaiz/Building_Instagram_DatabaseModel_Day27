"""empty message

Revision ID: 7eba5020457c
Revises: a0ca0b770478
Create Date: 2021-08-26 15:20:03.877819

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7eba5020457c'
down_revision = 'a0ca0b770478'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('user_url_image', sa.String(length=120), nullable=True),
    sa.Column('text', sa.String(length=120), nullable=True),
    sa.Column('url_image', sa.String(length=120), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=120), nullable=True),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('user_url_image', sa.String(length=120), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('friend', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'friend', 'user', ['user_id'], ['id'])
    op.add_column('user', sa.Column('username', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('birth', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('country', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('city', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('url_image', sa.String(length=120), nullable=True))
    op.create_unique_constraint(None, 'user', ['username'])
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'url_image')
    op.drop_column('user', 'city')
    op.drop_column('user', 'country')
    op.drop_column('user', 'birth')
    op.drop_column('user', 'username')
    op.drop_constraint(None, 'friend', type_='foreignkey')
    op.drop_column('friend', 'user_id')
    op.drop_table('comment')
    op.drop_table('post')
    # ### end Alembic commands ###