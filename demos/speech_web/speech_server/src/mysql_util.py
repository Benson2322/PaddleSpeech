import pymysql.cursors
def get_connection():
    return pymysql.connect(host='localhost', user='root', password='UwtDQjgQ8E', database='marvin',
                           cursorclass=pymysql.cursors.DictCursor)
