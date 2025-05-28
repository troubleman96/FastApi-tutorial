"""adding columns on posts

Revision ID: f88602efa922
Revises: 9e8779285fe5
Create Date: 2025-05-28 06:50:21.488838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f88602efa922'
down_revision: Union[str, None] = '9e8779285fe5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', 
    ))
        


def downgrade():
    """Downgrade schema."""
    pass
