"""fill questions_answers

Revision ID: b993cd3b97f1
Revises: cf6b38c2a4e2
Create Date: 2024-06-01 11:31:42.783085

"""
from typing import Sequence, Union

from alembic import op

from parse_to_db import parse_to_db

# revision identifiers, used by Alembic.
revision: str = 'b993cd3b97f1'
down_revision: Union[str, None] = 'cf6b38c2a4e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    parse_to_db()
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('TRUNCATE question_answer CASCADE;')
    # ### end Alembic commands ###