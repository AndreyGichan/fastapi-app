"""add content column to posts table

Revision ID: 69650cdde74b
Revises: 0564e3764800
Create Date: 2025-08-20 13:47:28.897755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69650cdde74b'
down_revision: Union[str, Sequence[str], None] = '0564e3764800'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
