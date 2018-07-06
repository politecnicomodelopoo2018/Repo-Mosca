import pymysql

class DataBase(object):
    @staticmethod
    def run(target_db, query):
        db = pymysql.connect(host='127.0.0.1',
                             user='root',
                             passwd='alumno',
                             db=target_db,
                             charset='utf-8',
                             autocommit=True)

        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)

        db.close()
        return cursor