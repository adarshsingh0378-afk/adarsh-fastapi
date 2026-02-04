"""add content column to posts table

Revision ID: 829a1bb8620b
Revises: 60f38bef87a0
Create Date: 2026-02-04 15:18:45.331667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '829a1bb8620b'
down_revision: Union[str, Sequence[str], None] = '60f38bef87a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
