"""andAnotherOne2

Revision ID: 8d808acf2107
Revises: 68bc2b2ea8ef
Create Date: 2024-02-14 13:54:06.826218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d808acf2107'
down_revision: Union[str, None] = '68bc2b2ea8ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###