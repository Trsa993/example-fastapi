"""add last few columns to posts table

Revision ID: 56f8557099fc
Revises: f8c7c29f604d
Create Date: 2022-10-07 09:59:51.064592

"""
from cgitb import text
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56f8557099fc'
down_revision = 'f8c7c29f604d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", 
    sa.Column("published", sa.Boolean(), nullable=False, server_default="true"))
    op.add_column("posts", 
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")))    
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
