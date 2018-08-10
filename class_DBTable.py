class DBFKey(object):
    def __init__(self, foreign_table, foreign_column):
        self.foreign_table = foreign_table
        self.foreign_column = foreign_column


class DBTable(object):
    def __init__(self, table_name):
        self.table_name = table_name

        self.pkey_row = None

        self.cols = []  # Nombres de columnas en orden
        self.col_dict = {}  # Columna: Valor
        self.fkey_cols = {}  # Claves foraneas - Columna FK: Objeto DBFKey con tabla y columna foraneas

    def load_from_dict(self, orig_dict):
        for col in orig_dict:
            if col in self.col_dict:
                self.col_dict[col] = orig_dict[col]
            else:
                self.add_columns(col)
                self.set_column(col, orig_dict[col])

    def add_columns(self, *args):
        for col in args:
            self.cols.append(col)
            self.col_dict[col] = None

    def add_foreign_key(self, fkey_col, foreign_table, foreign_column):
        self.fkey_cols[fkey_col] = DBFKey(foreign_table, foreign_column)

    def set_primary_key(self, pk_row):
        self.pkey_row = pk_row

    def get_primary_key_col(self):
        return self.col_dict[self.pkey_row]

    def get_display_name(self):
        return str(self.get_primary_key_col())

    def set_column(self, col, value):
        if col in self.cols:
            if not value:
                value = None
            self.col_dict[col] = value
        else:
            raise NameError("Undefined row " + col + " for table " + self.table_name + ".", col)

    def query_insert(self):
        query = "INSERT INTO " + self.table_name + " VALUES ("
        for i, val in enumerate(self.cols):
            val = self.col_dict[val]
            if type(val) is str:
                query += "'" + val + "'"
            elif val is None:
                query += "NULL"
            else:
                query += str(val)
            if i < len(self.cols) - 1:
                query += ","

        query += ");"
        return query

    def query_update(self):
        query = "UPDATE " + self.table_name + " SET"
        for i, row in enumerate(self.cols):
            if not row == self.pkey_row:
                value = self.col_dict[row]
                if type(value) is str:
                    value = "'" + value + "'"

                query += " " + row + " = " + str(value)
                if i < len(self.cols) - 1:
                    query += ","

        query += " WHERE " + self.pkey_row + " = " + str(self.col_dict[self.pkey_row]) + ";"
        return query

    def query_delete(self):
        if not self.pkey_row:
            raise ValueError("Undefined primary key row ", self.pkey_row)
        query = "DELETE FROM " + self.table_name + " WHERE " + self.pkey_row + " = " + str(self.col_dict[self.pkey_row]) + ";"
        return query