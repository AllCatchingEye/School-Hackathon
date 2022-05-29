"""empty message

Revision ID: c31561864cff
Revises: 59abbd3a52c9
Create Date: 2022-05-28 13:27:03.932611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c31561864cff'
down_revision = '59abbd3a52c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('adminen')
    op.add_column('users', sa.Column('userid', sa.Integer(), nullable=False))
    op.add_column('users', sa.Column('firstname', sa.String(length=128), nullable=False))
    op.add_column('users', sa.Column('password', sa.String(length=128), nullable=False))
    op.add_column('users', sa.Column('role', sa.Integer(), nullable=False))
    op.add_column('users', sa.Column('organisation', sa.Integer(), nullable=False))
    op.drop_constraint('users_name_key', 'users', type_='unique')
    op.create_foreign_key(None, 'users', 'organisation', ['organisation'], ['orgaid'])
    op.create_foreign_key(None, 'users', 'roles', ['role'], ['roleid'])
    op.drop_column('users', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_unique_constraint('users_name_key', 'users', ['name'])
    op.drop_column('users', 'organisation')
    op.drop_column('users', 'role')
    op.drop_column('users', 'password')
    op.drop_column('users', 'firstname')
    op.drop_column('users', 'userid')
    op.create_table('adminen',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='adminen_pkey'),
    sa.UniqueConstraint('email', name='adminen_email_key'),
    sa.UniqueConstraint('name', name='adminen_name_key')
    )
    # ### end Alembic commands ###
