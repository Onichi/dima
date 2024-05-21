"""tables_2

Revision ID: d1558e80357e
Revises: 60aed1684aeb
Create Date: 2024-05-21 22:13:48.006201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1558e80357e'
down_revision = '60aed1684aeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('position')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('ix_user_email')
        batch_op.drop_index('ix_user_username')

    op.drop_table('user')
    op.drop_table('employee')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('position_code', sa.VARCHAR(length=10), nullable=False),
    sa.ForeignKeyConstraint(['position_code'], ['position.code'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('ix_user_username', ['username'], unique=1)
        batch_op.create_index('ix_user_email', ['email'], unique=1)

    op.create_table('position',
    sa.Column('code', sa.VARCHAR(length=10), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('salary', sa.FLOAT(), nullable=False),
    sa.Column('duties', sa.TEXT(), nullable=False),
    sa.Column('requirements', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    # ### end Alembic commands ###