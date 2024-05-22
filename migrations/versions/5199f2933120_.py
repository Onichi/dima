"""empty message

Revision ID: 5199f2933120
Revises: 5320fc7a1590
Create Date: 2024-05-22 22:41:23.333729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5199f2933120'
down_revision = '5320fc7a1590'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('service2_code', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('service3_code', sa.String(length=10), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('service3_code')
        batch_op.drop_column('service2_code')

    # ### end Alembic commands ###
