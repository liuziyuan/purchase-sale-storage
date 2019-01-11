"""empty message

Revision ID: 8261405620de
Revises: 
Create Date: 2019-01-11 17:57:09.836802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8261405620de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_role')),
    sa.UniqueConstraint('name', name=op.f('uq_role_name'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('sign_in_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('name', name=op.f('uq_user_name'))
    )
    op.create_table('user_roles',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], name=op.f('fk_user_roles_role_id_role')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_user_roles_user_id_user')),
    sa.PrimaryKeyConstraint('user_id', 'role_id', name=op.f('pk_user_roles'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_roles')
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###