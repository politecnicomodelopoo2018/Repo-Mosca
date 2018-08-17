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

        """
        Columnas con valores predeterminados (via python)
            Usado al realizar un insert, estas columnas tendran el valor asignado aqui y no le permitira
        al usuario modificarlas a la hora de crear el objeto.
        """
        self.default_cols = {}

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

    def set_default_column(self, column, default_val):
        if column in self.cols:
            self.default_cols[column] = default_val

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
        query_args = []
        query_string = "INSERT INTO " + self.table_name + " VALUES ("
        for i, val in enumerate(self.cols):
            if val in self.default_cols:
                query_string += self.default_cols[val]
            else:
                query_string += "%s"
                val = self.col_dict[val]
                if val is None:
                    query_args.append(None)
                else:
                    query_args.append(str(val))
            if i < len(self.cols) - 1:
                query_string += ","

        query_string += ");"
        return [query_string, query_args]

    def query_update(self):
        query_args = []
        query_string = "UPDATE " + self.table_name + " SET"
        for i, row in enumerate(self.cols):
            cols_len = len(self.cols) - len(self.default_cols) - 1
            if not row == self.pkey_row and row not in self.default_cols:
                value = self.col_dict[row]

                query_string += " %s = %s" % (row, '%s')
                query_args.append(str(value))
                if i < cols_len:
                    query_string += ","

        query_string += " WHERE " + self.pkey_row + " = " + str(self.col_dict[self.pkey_row]) + ";"
        return [query_string, query_args]

    def query_delete(self):
        if not self.pkey_row:
            raise ValueError("Undefined primary key row ", self.pkey_row)
        query = "DELETE FROM " + self.table_name + " WHERE " + self.pkey_row + " = " + str(self.col_dict[self.pkey_row]) + ";"
        return query