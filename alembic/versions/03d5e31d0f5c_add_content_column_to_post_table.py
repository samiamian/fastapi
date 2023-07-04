"""add content column to post table

Revision ID: 03d5e31d0f5c
Revises: c663a801c9c9
Create Date: 2023-07-03 12:16:33.232640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03d5e31d0f5c'
down_revision = 'c663a801c9c9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
