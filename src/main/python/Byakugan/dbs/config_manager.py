import sqlite3
from fbs_runtime.application_context import cached_property


class Config:
    def __init__(self, ctx):
        self.ctx = ctx
        self.conn = sqlite3.connect(self.ctx.get_resource('dbs/config.db'))
        self.cur = self.conn.cursor()

    def get_config(self, name):
        self.cur.execute('SELECT Value FROM Config WHERE Name = "{}"'.format(name))
        return self.cur.fetchone()[0]

    def close(self):
        self.conn.close()

    @cached_property
    def app_name(self):
        return self.get_config('app_name')
