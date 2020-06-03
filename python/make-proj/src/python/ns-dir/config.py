"""Application configuration class.

"""
__author__ = '${user}'

from zensols.config import ExtendedInterpolationEnvConfig


class AppConfig(ExtendedInterpolationEnvConfig):
    def __init__(self, *args, **kwargs):
        if 'config_file' not in kwargs:
            kwargs['config_file'] = 'resources/${project}.conf'
        if 'env' not in kwargs:
            kwargs['env'] = {'app_root': '.'}
        super().__init__(*args, default_expect=True, **kwargs)
