from Connection.condb import Con


class Tables(Con):
    def __init__(self):
        Con.__init__(self)
    @classmethod
    def drop_or_create_tables(cls):

        with cls.conn() as con:

            if con.execute("SELECT 1 FROM sys.objects where name = 'Users' AND type = 'U'").fetchone() != None:
                print("Dropping a Table ...")
                con.execute("DROP TABLE Users")

            if con.execute("SELECT 1 FROM sys.objects where name = 'Items' AND type = 'U'").fetchone() != None:
                print("Dropping a Table ...")
                con.execute("DROP TABLE Items")

            # if con.execute("SELECT 1 FROM sys.objects where name = 'Users' AND type = 'U'").fetchone() == None:
            #     con.execute("CREATE TABLE Users (id INT NOT NULL IDENTITY(1,1) PRIMARY KEY, username varchar(max), password varchar(max))")
            #
            # if con.execute("SELECT 1 FROM sys.objects where name = 'Items' AND type = 'U'").fetchone() == None:
            #     con.execute("CREATE TABLE Items (id INT NOT NULL IDENTITY(1,1) PRIMARY KEY, name varchar(max), price FLOAT)")

