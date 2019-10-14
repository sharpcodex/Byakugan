from fbs_runtime.application_context import cached_property

from helpers.db_repository import DbRepository


class ConfigManager:
    def __init__(self, config_db_filename):
        self.db_repository = DbRepository(config_db_filename)

    def get_single_value(self, name):
        return self.db_repository.get_single_value(column='Value', table='Config', q_column='Name', q_value=name)

    @cached_property
    def app_name(self):
        return self.get_single_value('app_name')

    @cached_property
    def app_theme(self):
        return self.get_single_value('app_theme')

    @cached_property
    def app_color(self):
        return self.get_single_value('app_color')

    def dispose(self):
        self.db_repository.dispose()
