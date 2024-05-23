"""empty message

Revision ID: d059999683da
Revises: b95507333ab3
Create Date: 2024-05-23 23:07:49.136309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd059999683da'
down_revision = 'b95507333ab3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_constraint('fk_order_service3', type_='foreignkey')
        batch_op.drop_constraint('fk_order_service2', type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('location_code')
        batch_op.drop_column('service2_code')
        batch_op.drop_column('employee_code')
        batch_op.drop_column('payment_mark')
        batch_op.drop_column('service3_code')
        batch_op.drop_column('cost')
        batch_op.drop_column('service1_code')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('service1_code', sa.VARCHAR(length=10), nullable=True))
        batch_op.add_column(sa.Column('cost', sa.FLOAT(), nullable=False))
        batch_op.add_column(sa.Column('service3_code', sa.VARCHAR(length=10), nullable=True))
        batch_op.add_column(sa.Column('payment_mark', sa.BOOLEAN(), nullable=False))
        batch_op.add_column(sa.Column('employee_code', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('service2_code', sa.VARCHAR(length=10), nullable=True))
        batch_op.add_column(sa.Column('location_code', sa.VARCHAR(length=10), nullable=False))
        batch_op.create_foreign_key(None, 'additional_service', ['service1_code'], ['code'])
        batch_op.create_foreign_key(None, 'employee', ['employee_code'], ['code'])
        batch_op.create_foreign_key(None, 'location', ['location_code'], ['code'])
        batch_op.create_foreign_key('fk_order_service2', 'additional_service', ['service2_code'], ['code'])
        batch_op.create_foreign_key('fk_order_service3', 'additional_service', ['service3_code'], ['code'])

    # ### end Alembic commands ###