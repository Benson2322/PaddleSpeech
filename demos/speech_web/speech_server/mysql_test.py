import random

from src.mysql_util import *


with get_connection() as connection:
    with connection.cursor() as cursor:
        sql = 'select id,name from t_g4_course'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

with get_connection() as connection:
    with connection.cursor() as cursor:
        # sql = 'select text from t_g4_course where id=%s'
        # cursor.execute(sql, (2,))
        # result = cursor.fetchone()
        # print(result['text'])
        sql = 'select * from t_g4_course where id=%s'
        cursor.execute(sql, (3,))
        result = cursor.fetchone()
        print(result)
        out = result['text']
        if result['name'] == '随机':
            sql = 'select text from t_g4_course where text != "" and subjectId=%s'
            cursor.execute(sql, (result['subjectId'],))
            result = cursor.fetchall()
            allText = ''
            for text in result:
                allText += text['text'] + ' '
            texts = allText.split(' ')
            randomText = random.sample(allText.split(' '), 20)
            print(randomText)
            out = ' '.join(randomText)

        print(out)

