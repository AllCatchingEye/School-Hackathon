"""empty message

Revision ID: 033b8cf497ae
Revises: 7d35b8638b4f
Create Date: 2022-05-29 13:08:15.187252

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '033b8cf497ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('users', sa.Column('role', sa.Integer(), nullable=False))
    # op.add_column('users', sa.Column('organisation', sa.Integer(), nullable=False))
    # op.create_foreign_key(None, 'users', 'roles', ['role'], ['roleid'])
    # op.create_foreign_key(None, 'users', 'organisation', ['organisation'], ['orgaid'])
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'organisation')
    op.drop_column('users', 'role')
    # ### end Alembic commands ###
