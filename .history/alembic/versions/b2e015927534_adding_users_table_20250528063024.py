"""adding users table

Revision ID: b2e015927534
Revises: 5c9cfce41db9
Create Date: 2025-05-28 06:24:53.499862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2e015927534'
down_revision: Union[str, None] = '5c9cfce41db9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                              
                    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
