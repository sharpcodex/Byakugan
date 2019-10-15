import sqlite3


class LibraryManager:
    def __init__(self, db_filename):
        self.conn = sqlite3.connect(db_filename)
        self.cur = self.conn.cursor()

    def get_single_value(self, column, table, q_column, q_value):
        self.cur.execute(f'SELECT {column} FROM {table} WHERE {q_column} = "{q_value}"')
        return self.cur.fetchone()[0]

    def dispose(self):
        self.conn.close()
