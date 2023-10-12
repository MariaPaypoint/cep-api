"""keywords

Revision ID: f17d33089d98
Revises: 166f7a125d71
Create Date: 2023-06-20 17:10:13.679680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f17d33089d98'
down_revision = '166f7a125d71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'keyword_group',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('alias', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('alias'),
    )
    op.create_index(op.f('ix_keyword_group_id'), 'keyword_group', ['id'], unique=False)
    
    op.create_table(
        'keyword_value',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=True),
        sa.Column('code', sa.String(), nullable=True),
        sa.Column('value', sa.String(), nullable=True),
        sa.Column('language', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['group_id'], ['keyword_group.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_keyword_value_id'), 'keyword_value', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_keyword_value_id'), table_name='keyword_value')
    op.drop_table('keyword_value')
    op.drop_index(op.f('ix_keyword_group_id'), table_name='keyword_group')
    op.drop_table('keyword_group')
    # ### end Alembic commands ###
