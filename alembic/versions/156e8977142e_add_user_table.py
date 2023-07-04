"""add user table

Revision ID: 156e8977142e
Revises: 03d5e31d0f5c
Create Date: 2023-07-03 12:20:37.051490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '156e8977142e'
down_revision = '03d5e31d0f5c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )


    pass


def downgrade() -> None:
    pass
