"""create post table

Revision ID: 8df9bf7d3a3b
Revises: 
Create Date: 2022-10-05 09:38:43.321334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8df9bf7d3a3b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column("id", sa.Integer(), nullable=False, primary_key=True), 
    sa.Column("title", sa.String(), nullable=False))
    

def downgrade():
    op.drop_table("posts")
    pass
