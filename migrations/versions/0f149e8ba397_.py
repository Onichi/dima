"""empty message

Revision ID: 0f149e8ba397
Revises: 5199f2933120
Create Date: 2024-05-23 22:42:53.148615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f149e8ba397'
down_revision = '5199f2933120'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.alter_column('employee_code',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.create_foreign_key(None, 'additional_service', ['service3_code'], ['code'])
        batch_op.create_foreign_key(None, 'additional_service', ['service2_code'], ['code'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('employee_code',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)

    # ### end Alembic commands ###