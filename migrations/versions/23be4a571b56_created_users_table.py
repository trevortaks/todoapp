"""Created Users table

Revision ID: 23be4a571b56
Revises: f8a4401177eb
Create Date: 2018-10-09 18:44:01.886200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23be4a571b56'
down_revision = 'f8a4401177eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=25), nullable=True),
    sa.Column('fullname', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('profilepic', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_User_email'), 'User', ['email'], unique=True)
    op.create_index(op.f('ix_User_username'), 'User', ['username'], unique=True)
    op.add_column('Task', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Task', 'User', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Task', type_='foreignkey')
    op.drop_column('Task', 'user_id')
    op.drop_index(op.f('ix_User_username'), table_name='User')
    op.drop_index(op.f('ix_User_email'), table_name='User')
    op.drop_table('User')
    # ### end Alembic commands ###
