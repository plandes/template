"""Application configuration class.

"""
__author__ = '${user}'

import logging
from zensols.config import ImportIniConfig, EnvironmentConfig

logger = logging.getLogger(__name__)


class AppConfig(ImportIniConfig):
    def __init__(self, *args, **kwargs):
        if len(args) == 0 and 'config_file' not in kwargs:
            kwargs['config_file'] = 'resources/${project}.conf'
        env = EnvironmentConfig(map_delimiter='$')
        super().__init__(*args, children=(env,),
                         exclude_config_sections=False,
                         config_section='default',
                         **kwargs)
