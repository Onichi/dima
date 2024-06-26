"""empty message

Revision ID: cf7e4bb29fe7
Revises: a2ed2b33822b
Create Date: 2024-05-24 01:02:05.423515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf7e4bb29fe7'
down_revision = 'a2ed2b33822b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('syka', schema=None) as batch_op:
        batch_op.drop_constraint('fk_syka_service3_code_additional_service', type_='foreignkey')
        batch_op.drop_constraint('fk_syka_service2_code_additional_service', type_='foreignkey')
        batch_op.drop_column('service3_code')
        batch_op.drop_column('service2_code')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('syka', schema=None) as batch_op:
        batch_op.add_column(sa.Column('service2_code', sa.VARCHAR(length=10), nullable=True))
        batch_op.add_column(sa.Column('service3_code', sa.VARCHAR(length=10), nullable=True))
        batch_op.create_foreign_key('fk_syka_service2_code_additional_service', 'additional_service', ['service2_code'], ['code'])
        batch_op.create_foreign_key('fk_syka_service3_code_additional_service', 'additional_service', ['service3_code'], ['code'])

    # ### end Alembic commands ###
