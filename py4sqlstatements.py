class Py4SQLStatements:


    def __init__(self):
        self.db_name = ""
        self.table_name = ""
        self.table_meta = []

    @staticmethod
    def create_table(table_name, meta_data):
        """Sql Statement for Creating table according to table meta_data
        Args:
            table_name: str
            meta_data: list of dictionaries

        Returns:
            sqlstatement, str, sql statement
        e.g.
        meta_data = [{'name': 'userid', 'sqltype': 'INTEGER NOT NULL'},
                    {'name': 'username', 'sqltype': 'TEXT NOT NULL UNIQUE'},
                    {'name': 'age', 'sqltype': 'INTEGER'},
                    {'name': 'height', 'sqltype': 'REAL'}]
        """
        sqlstatement = "CREATE TABLE " + table_name + " (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,"
        for rc in meta_data:
            sqlstatement = sqlstatement + rc['name'] + " " + rc['sqltype'] + ", "
        sqlstatement = sqlstatement.rstrip(', ') + ");"
        return sqlstatement

    @staticmethod
    def load_data_to_table(datablock, table_name, meta_data):
        """sql"""
        for row in datablock:
            rc = tuple(row)
            sqlstatement = 'INSERT INTO ' + table_name + \
                           ' (' + ','.join(a['name'] for a in meta_data) + ')' + \
                           ' VALUES (' + ','.join('?' for i in range(len(rc))) + ')'
            # dbcursor.execute(sqlstatement, rc)
        return None



