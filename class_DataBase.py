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

        query_string = query[0]
        query_args = query[1]
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query_string, query_args)

        db.close()
        return cursor