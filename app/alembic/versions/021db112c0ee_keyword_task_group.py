"""keyword_task_group

Revision ID: 021db112c0ee
Revises: 562487d42682
Create Date: 2023-06-24 00:35:31.534868

"""
from alembic import op
import sqlalchemy as sa
from app.alembic_utils import keyword_group, keyword_value


# revision identifiers, used by Alembic.
revision = '021db112c0ee'
down_revision = '562487d42682'
branch_labels = None
depends_on = None

group_id = 2

def upgrade():
   
    op.bulk_insert(
        keyword_group,
        [
            {
                "id": group_id,
                "alias": "task_group",
            },
        ],
    )
    
    op.bulk_insert(
        keyword_value,
        [
            {
                "group_id" : group_id,
                "code"     : "introduction",
                "value"    : "Introduction",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "quote",
                "value"    : "Learning a quote",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "discussion",
                "value"    : "Discussion",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "fixing",
                "value"    : "Repetition",
                "language" : "en",
            },
            
            {
                "group_id" : group_id,
                "code"     : "introduction",
                "value"    : "Знакомство",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "quote",
                "value"    : "Учим цитату",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "discussion",
                "value"    : "Обсуждение",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "fixing",
                "value"    : "Закрепление",
                "language" : "ru",
            },
        ],
    )

def downgrade():
    op.execute("DELETE FROM keyword_value WHERE group_id=%s" % group_id)
    op.execute("DELETE FROM keyword_group WHERE id=%s" % group_id)
    