"""keyword_lang

Revision ID: 562487d42682
Revises: f17d33089d98
Create Date: 2023-06-20 17:11:53.630357

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from app.alembic_utils import keyword_group, keyword_value


# revision identifiers, used by Alembic.
revision = '562487d42682'
down_revision = 'f17d33089d98'
branch_labels = None
depends_on = None

group_id = 1

# https://alembic.sqlalchemy.org/en/latest/ops.html

def upgrade():

    op.bulk_insert(
        keyword_group,
        [
            {
                "id": group_id,
                "alias": "language",
            },
        ],
    )
    
    op.bulk_insert(
        keyword_value,
        [
            {
                "group_id" : group_id,
                "code"     : "en",
                "value"    : "English",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "ru",
                "value"    : "Russian",
                "language" : "en",
            },
            
            {
                "group_id" : group_id,
                "code"     : "en",
                "value"    : "Английский",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "ru",
                "value"    : "Русский",
                "language" : "ru",
            },
        ],
    )

def downgrade():
    op.execute("DELETE FROM keyword_value WHERE group_id=%s" % group_id)
    op.execute("DELETE FROM keyword_group WHERE id=%s" % group_id)
