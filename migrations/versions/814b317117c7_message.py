"""message

Revision ID: 814b317117c7
Revises: 5eba6e0e41df
Create Date: 2024-08-15 11:40:04.128384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '814b317117c7'
down_revision = '5eba6e0e41df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pizza_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('restaurant_id', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_column('restaurant_id')
        batch_op.drop_column('pizza_id')

    # ### end Alembic commands ###
