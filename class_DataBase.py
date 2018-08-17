import pymysql

class DataBase(object):
    """<query> es una lista [formato del string, argumentos]
    EJ:   query[0] = "SELECT * FROM %s WHERE %s = %s;"
          query[1] = ["Persona", "nombre", "Juan"]
    """
    @staticmethod
    def run_query(target_db, query):
        db = pymysql.connect(host='127.0.0.1',
                             user='root',
                             passwd='alumno',
                             db=target_db,
                             autocommit=True)

        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(*query)

        db.close()
        return cursor