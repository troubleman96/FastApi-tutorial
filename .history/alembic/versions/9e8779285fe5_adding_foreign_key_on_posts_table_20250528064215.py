"""adding foreign key on posts table

Revision ID: 9e8779285fe5
Revises: b2e015927534
Create Date: 2025-05-28 06:41:47.657572

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e8779285fe5'
down_revision: Union[str, None] = 'b2e015927534'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
