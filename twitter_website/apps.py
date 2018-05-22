from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "twitter_website"

    def ready(self):
        import_module("twitter_website.receivers")
