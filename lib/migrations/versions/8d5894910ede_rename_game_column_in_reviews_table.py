"""Rename game column in reviews table

Revision ID: 8d5894910ede
Revises: 4c09f5c7e287
Create Date: 2024-05-13 11:12:42.837722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d5894910ede'
down_revision = '4c09f5c7e287'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('reviews', 'game', new_column_name='game_id')


def downgrade() -> None:
    op.alter_column('reviews', 'game_id', new_column_name='game')
