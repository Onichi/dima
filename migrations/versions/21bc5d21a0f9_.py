"""empty message

Revision ID: 21bc5d21a0f9
Revises: 1bcdfa94fb42
Create Date: 2024-05-23 23:15:44.188511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21bc5d21a0f9'
down_revision = '1bcdfa94fb42'
branch_labels = None
depends_on = None


def upgrade():
    pass



def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cost', sa.FLOAT(), nullable=False))
        batch_op.add_column(sa.Column('service1_code', sa.VARCHAR(length=10), nullable=True))
        batch_op.add_column(sa.Column('service2_code', sa.VARCHAR(length=10), nullable=True))
        batch_op.add_column(sa.Column('location_code', sa.VARCHAR(length=10), nullable=False))
        batch_op.add_column(sa.Column('payment_mark', sa.BOOLEAN(), nullable=False))
        batch_op.add_column(sa.Column('employee_code', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('service3_code', sa.VARCHAR(length=10), nullable=True))
        batch_op.create_foreign_key('fk_order_service3', 'additional_service', ['service3_code'], ['code'])
        batch_op.create_foreign_key(None, 'employee', ['employee_code'], ['code'])
        batch_op.create_foreign_key('fk_order_service2', 'additional_service', ['service2_code'], ['code'])
        batch_op.create_foreign_key(None, 'additional_service', ['service1_code'], ['code'])
        batch_op.create_foreign_key(None, 'location', ['location_code'], ['code'])

    # ### end Alembic commands ###
