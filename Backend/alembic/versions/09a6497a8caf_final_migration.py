"""Final migration

Revision ID: 09a6497a8caf
Revises: cca976f3b132
Create Date: 2025-02-12 19:44:59.763095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09a6497a8caf'
down_revision: Union[str, None] = 'cca976f3b132'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedback', sa.Column('filename', sa.String(), nullable=True))
    op.add_column('feedback', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.drop_index('ix_feedback_vulnerability', table_name='feedback')
    op.create_index(op.f('ix_feedback_filename'), 'feedback', ['filename'], unique=False)
    op.drop_column('feedback', 'vulnerability')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedback', sa.Column('vulnerability', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_feedback_filename'), table_name='feedback')
    op.create_index('ix_feedback_vulnerability', 'feedback', ['vulnerability'], unique=False)
    op.drop_column('feedback', 'created_at')
    op.drop_column('feedback', 'filename')
    # ### end Alembic commands ###
