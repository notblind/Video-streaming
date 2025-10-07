"""

Revision ID: fa305afac328
Revises:
Create Date: 2025-10-07 12:42:58.000416

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "fa305afac328"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "base_files",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("store_name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "clip_clips",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("clip_file", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["clip_file"],
            ["base_files.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("clip_clips")
    op.drop_table("base_files")
