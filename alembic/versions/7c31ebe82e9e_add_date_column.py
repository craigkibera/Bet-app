"""add date column

Revision ID: 7c31ebe82e9e
Revises: b653b4aaf41d
Create Date: 2025-03-13 12:30:10.595710

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '7c31ebe82e9e'
down_revision = 'b653b4aaf41d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('date_time', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'date_time')
    # ### end Alembic commands ###
