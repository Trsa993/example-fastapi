"""add content column to posts table

Revision ID: d4059bbcb241
Revises: 8df9bf7d3a3b
Create Date: 2022-10-06 14:42:04.843750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4059bbcb241'
down_revision = '8df9bf7d3a3b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", 
    sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
    pass