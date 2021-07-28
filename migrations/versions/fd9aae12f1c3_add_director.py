"""Add Director

Revision ID: fd9aae12f1c3
Revises: 
Create Date: 2021-07-28 09:14:12.891394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd9aae12f1c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('director', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'movies', ['director'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'movies', type_='unique')
    op.drop_column('movies', 'director')
    # ### end Alembic commands ###
