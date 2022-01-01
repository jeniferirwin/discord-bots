"""Add finished game game id

Revision ID: 2b3b52dd4733
Revises: 757ab2496a9f
Create Date: 2021-12-31 11:01:36.404868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2b3b52dd4733"
down_revision = "757ab2496a9f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "finished_game", sa.Column("game_id", sa.String(), nullable=False)
    )
    op.create_index(
        op.f("ix_finished_game_game_id"),
        "finished_game",
        ["game_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_finished_game_game_id"), table_name="finished_game")
    op.drop_column("finished_game", "game_id")
    # ### end Alembic commands ###