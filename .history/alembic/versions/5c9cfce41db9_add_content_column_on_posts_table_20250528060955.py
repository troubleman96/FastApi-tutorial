"""add content column on posts table

Revision ID: 5c9cfce41db9
Revises: 956347556d43
Create Date: 2025-05-28 06:03:20.227929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c9cfce41db9'
down_revision: Union[str, None] = '956347556d43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    """Downgrade schema."""
    op.drop_table('posts', 'content')
    pass
