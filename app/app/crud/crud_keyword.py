from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import text
from sqlalchemy.dialects import postgresql

from app.crud.base import CRUDBase
from app.models.keyword import Keyword_Group, Keyword_Value
from app.schemas.keyword import KeywordCreate, KeywordUpdate

class CRUDKeyword(CRUDBase[Keyword_Group, KeywordCreate, KeywordUpdate]):
    
    def exist(
        self, db: Session, alias: str, code: str
    ) -> bool:
        # q = (
            # db.query(Keyword_Group)
            # .options(joinedload(Keyword_Group.values))
            # .filter(Keyword_Value.code == code)
        # )
        # print(str(q.statement.compile(dialect=postgresql.dialect())))
        # return bool(q.all())
        
        # очень сложный получается запрос, на него еще варнинг выдается, пока лучше sql написать
        sql = '''
            SELECT *
            FROM %(keyword_value)s
            WHERE group_id = (
                SELECT id 
                FROM %(keyword_group)s 
                WHERE alias = :alias)
            AND code = :code
        ''' % {
            'keyword_value': Keyword_Value.__tablename__,
            'keyword_group': Keyword_Group.__tablename__,
        }
        result = db.query(Keyword_Value).from_statement(text(sql)).params({
            'alias': alias,
            'code': code,
        }).all()

        return bool(result)
        
    def get_values(
        self, db: Session, alias: str
    ) -> tuple:
    
        # group_row = (
            # db.query(Keyword_Group)
            # .filter(Keyword_Group.alias == alias)
            # .all()
        # )
        # value_row = (
            # db.query(Keyword_Value)
            # .filter(Keyword_Value.group_id == group_row[0].id)
            # .all()
        # )
        # return value_row
        
        sql = '''
            SELECT *
            FROM %(keyword_value)s
            WHERE group_id = (
                SELECT id 
                FROM %(keyword_group)s 
                WHERE alias=:alias)
        ''' % {
            'keyword_value': Keyword_Value.__tablename__,
            'keyword_group': Keyword_Group.__tablename__,
        }
        result = db.query(Keyword_Value).from_statement(text(sql)).params({
            'alias': alias,
        }).all()

        return result
    
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100, alias: str = None
    # ) -> List[Keyword_Group]:
    ) -> List:
        filter = []
        if alias:
            filter.append('AND g.alias = :alias')
            
        sql = '''
            SELECT g.id, g.alias, v.code, v.value
            FROM %(keyword_value)s AS v
              LEFT JOIN %(keyword_group)s AS g ON g.id = v.group_id
            WHERE 1=1
              %(filter)s
            ORDER BY g.id, v.code
        ''' % {
            'keyword_value': Keyword_Value.__tablename__,
            'keyword_group': Keyword_Group.__tablename__,
            'filter'       : ' '.join(filter)
        }
        result = db.execute(text(sql).params({
            'alias': alias,
        })).all()

        # groups_with_values = []
        # for row in result:
            # g = {
                # "group_alias": row.alias,
                # "code": row.code,
                # "value": row.value,
            # }
            # groups_with_values.append(g)

        # return groups_with_values
        
        groups_with_values = []
        old_gid = -1
        for row in result:
            if old_gid != row.id:
                if old_gid > -1:
                    groups_with_values.append(g)
                g = {
                    "id": row.id,
                    "alias": row.alias,
                    "items": [
                        {
                            "code": row.code,
                            "value": row.value,
                        }
                    ]
                }
                old_gid = row.id
            else:
                g['items'].append({
                    "code": row.code,
                    "value": row.value,
                })
                
        if g:
            groups_with_values.append(g)
            
        return groups_with_values
    
keyword = CRUDKeyword(Keyword_Group)
