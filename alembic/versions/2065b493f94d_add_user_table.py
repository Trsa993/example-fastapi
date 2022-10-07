"""add user table

Revision ID: 2065b493f94d
Revises: d4059bbcb241
Create Date: 2022-10-06 14:42:59.194038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2065b493f94d'
down_revision = 'd4059bbcb241'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
    sa.Column("id", sa.Integer(), nullable=False, primary_key=True), 
    sa.Column("email", sa.String(), nullable=False, unique=True),
    sa.Column("password", sa.String(), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False))

    pass

def downgrade():
    op.drop_table("users")

    pass
