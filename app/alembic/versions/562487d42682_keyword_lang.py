"""keyword_lang

Revision ID: 562487d42682
Revises: f17d33089d98
Create Date: 2023-06-20 17:11:53.630357

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = '562487d42682'
down_revision = 'f17d33089d98'
branch_labels = None
depends_on = None

# https://alembic.sqlalchemy.org/en/latest/ops.html

def upgrade():
    # op.execute("""
        # INSERT INTO keyword_value 
            # (id, value)
        # VALUES
            # (1, 'lang')
    # """)
    # op.execute("""
        # INSERT INTO keyword_group 
            # (id, group_id, code, value)
        # VALUES
            # (1, 1, 'en', 'English'),
            # (2, 1, 'ru', 'Русский')
    # """)
    
    keyword_group = sa.table(
        "keyword_group",
        sa.column("id", sa.Integer()),
        sa.column("alias", sa.String()),
    )
    op.bulk_insert(
        keyword_group,
        [
            {
                "id": 1,
                "alias": "language",
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
                "id": 1,
                "group_id": 1,
                "code": "en",
                "value": "English",
            },
            {
                "id": 2,
                "group_id": 1,
                "code": "ru",
                "value": "Русский",
            },
        ],
    )

def downgrade():
    op.execute("DELETE FROM keyword_value WHERE group_id=1")
    op.execute("DELETE FROM keyword_group WHERE id=1")
