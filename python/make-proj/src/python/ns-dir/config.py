"""Application configuration class.

"""
__author__ = '${user}'

from zensols.config import ExtendedInterpolationConfig


class AppConfig(ExtendedInterpolationConfig):
    def __init__(self, *args, **kwargs):
        super(AppConfig, self).__init__(*args, default_expect=True, **kwargs)
