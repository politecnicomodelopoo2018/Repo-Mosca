from class_DBTable import *

class Category(DBTable):
    def __init__(self):
        DBTable.__init__(self, "Category")

        self.add_columns("idCategory", "name")
        self.set_primary_key("idCategory")


c = Category()
c.load_from_dict({"idCategory": 1, "name": "General"})
print(c.query_insert())
print(c.query_update())
print(c.query_delete())