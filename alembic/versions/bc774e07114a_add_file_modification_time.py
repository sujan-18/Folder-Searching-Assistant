"""add file modification time

Revision ID: bc774e07114a
Revises: 0774988c034d
Create Date: 2026-10-26 22:23:31.565904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc774e07114a'
down_revision: Union[str, Sequence[str], None] = '0774988c034d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    op.add_column(
        "files",
        sa.Column(
            "modified_at",
            sa.DateTime(timezone=True),
            nullable=True
        )
    )

    op.execute(
        "UPDATE files "
        "SET modified_at = CURRENT_TIMESTAMP "
        "WHERE modified_at IS NULL"
    )

    op.alter_column(
        "files",
        "modified_at",
        existing_type=sa.DateTime(timezone=True),
        nullable=False
    )


def downgrade() -> None:
    op.drop_column("files", "modified_at")
