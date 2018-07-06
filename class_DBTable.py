class DBTable(object):
    def __init__(self, table_name):
        self.table_name = table_name

        self.rows = []
        self.row_dict = {}

    def add_rows(self, *args):
        for row in args:
            self.rows.append(row)

    def query_insert(self, *args):
        query = "INSERT INTO " + self.table_name + " VALUES ("
        for i, newval in enumerate(args):
            if type(newval) is str:
                query += "'" + newval + "'"
            elif newval is None:
                query += "NULL"
            else:
                query += str(newval)
            if i < len(args) - 1:
                query += ","

        query += ")"
        return query

dbtest = DBTable("Category")
dbtest.add_rows("idCategory", "name")

print(dbtest.query_insert(None, "General"))
print(dbtest.query_insert(None, "Off-Topic"))