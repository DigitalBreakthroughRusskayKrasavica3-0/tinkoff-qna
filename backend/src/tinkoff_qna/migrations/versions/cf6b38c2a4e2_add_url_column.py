"""add url column

Revision ID: cf6b38c2a4e2
Revises: eb4e9a926783
Create Date: 2024-05-31 18:57:29.167965

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'cf6b38c2a4e2'
down_revision: Union[str, None] = 'eb4e9a926783'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question_answer', sa.Column('url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question_answer', 'url')
    # ### end Alembic commands ###
