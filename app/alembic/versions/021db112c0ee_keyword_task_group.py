"""keyword_task_group

Revision ID: 021db112c0ee
Revises: 562487d42682
Create Date: 2023-06-24 00:35:31.534868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '021db112c0ee'
down_revision = '562487d42682'
branch_labels = None
depends_on = None


def upgrade():
   
    keyword_group = sa.table(
        "keyword_group",
        sa.column("id", sa.Integer()),
        sa.column("alias", sa.String()),
    )
    op.bulk_insert(
        keyword_group,
        [
            {
                "id": 2,
                "alias": "task_group",
            },
        ],
    )
    
    keyword_value = sa.table(
        "keyword_value",
        sa.column("id", sa.Integer()),
        sa.column("group_id", sa.Integer()),
        sa.column("code", sa.String()),
        sa.column("value", sa.String()),
    )
    op.bulk_insert(
        keyword_value,
        [
            {
                "id": 3,
                "group_id": 2,
                "code": "introduction",
                "value": "Знакомство",
            },
            {
                "id": 4,
                "group_id": 2,
                "code": "quote",
                "value": "Учим цитату",
            },
            {
                "id": 5,
                "group_id": 2,
                "code": "discussion",
                "value": "Обсуждение",
            },
            {
                "id": 6,
                "group_id": 2,
                "code": "fixing",
                "value": "Закрепление",
            },
        ],
    )

def downgrade():
    op.execute("DELETE FROM keyword_value WHERE group_id=2")
    op.execute("DELETE FROM keyword_group WHERE id=2")
    