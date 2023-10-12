import sqlalchemy as sa

keyword_group = sa.table(
    "keyword_group",
    sa.column("id", sa.Integer()),
    sa.column("alias", sa.String()),
)

keyword_value = sa.table(
    "keyword_value",
    sa.column("id", sa.Integer()),
    sa.column("group_id", sa.Integer()),
    sa.column("code", sa.String()),
    sa.column("value", sa.String()),
    sa.column("language", sa.String()),
)