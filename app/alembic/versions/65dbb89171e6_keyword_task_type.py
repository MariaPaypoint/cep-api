"""keyword_task_type

Revision ID: 65dbb89171e6
Revises: 021db112c0ee
Create Date: 2023-06-25 21:07:28.324829

"""
from alembic import op
import sqlalchemy as sa
from app.alembic_utils import keyword_group, keyword_value


# revision identifiers, used by Alembic.
revision = '65dbb89171e6'
down_revision = '021db112c0ee'
branch_labels = None
depends_on = None

group_id = 3

def upgrade():
   
    op.bulk_insert(
        keyword_group,
        [
            {
                "id"    : group_id,
                "alias" : "task_type",
            },
        ],
    )
    
    op.bulk_insert(
        keyword_value,
        [
            {
                "group_id" : group_id,
                "code"     : "read_excerpt",
                "value"    : "Read excerpt",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "listen_audio",
                "value"    : "Listen to audio",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "watch_video",
                "value"    : "Watch the video",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "comment",
                "value"    : "Comment",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "answer_question",
                "value"    : "Answer the question",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "pass_test",
                "value"    : "Take the test",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "insert_missed",
                "value"    : "Fill in the missing",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "find_words",
                "value"    : "Find the words",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "put_in_order",
                "value"    : "Arrange in order",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "write_by_heart",
                "value"    : "Write down by heart",
                "language" : "en",
            },
            {
                "group_id" : group_id,
                "code"     : "discuss_with_god",
                "value"    : "Talk to God",
                "language" : "en",
            },
            
            {
                "group_id" : group_id,
                "code"     : "read_excerpt",
                "value"    : "Прочитай отрывок",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "listen_audio",
                "value"    : "Прослушай аудио",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "watch_video",
                "value"    : "Посмотри видео",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "comment",
                "value"    : "Прокомментируй",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "answer_question",
                "value"    : "Ответь на вопрос",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "pass_test",
                "value"    : "Пройди тест",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "insert_missed",
                "value"    : "Вставь пропущенное",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "find_words",
                "value"    : "Найди слова",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "put_in_order",
                "value"    : "Расставь по порядку",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "write_by_heart",
                "value"    : "Запиши наизусть",
                "language" : "ru",
            },
            {
                "group_id" : group_id,
                "code"     : "discuss_with_god",
                "value"    : "Поговори с Богом",
                "language" : "ru",
            },
            
        ],
    )

def downgrade():
    op.execute("DELETE FROM keyword_value WHERE group_id=%s" % group_id)
    op.execute("DELETE FROM keyword_group WHERE id=%s" % group_id)
    