"""delete userlist in lesson

Revision ID: e3bfed7c099c
Revises: 6349d9e78d1b
Create Date: 2024-02-17 01:47:26.150291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e3bfed7c099c"
down_revision: Union[str, None] = "6349d9e78d1b"
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
