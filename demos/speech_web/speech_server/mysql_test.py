
from src.mysql_util import *


with get_connection() as connection:
    with connection.cursor() as cursor:
        sql = 'select id,name from t_g4_course'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

with get_connection() as connection:
    with connection.cursor() as cursor:
        sql = 'select text from t_g4_course where id=%s'
        cursor.execute(sql, (2,))
        result = cursor.fetchone()
        print(result['text'])