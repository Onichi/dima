"""empty message

Revision ID: 1e16067daeec
Revises: d2c30cc79ca3
Create Date: 2024-05-24 00:16:46.114350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e16067daeec'
down_revision = 'd2c30cc79ca3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_syka')
    with op.batch_alter_table('syka', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location_code', sa.String(length=10), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_syka_location_code_location'), 'location', ['location_code'], ['code'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('syka', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_syka_location_code_location'), type_='foreignkey')
        batch_op.drop_column('location_code')

    op.create_table('_alembic_tmp_syka',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('customer_code', sa.VARCHAR(length=10), nullable=False),
    sa.Column('location_code', sa.VARCHAR(length=10), nullable=False),
    sa.ForeignKeyConstraint(['customer_code'], ['customer.code'], ),
    sa.ForeignKeyConstraint(['location_code'], ['location.code'], name='fk_syka_location_code_location'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
