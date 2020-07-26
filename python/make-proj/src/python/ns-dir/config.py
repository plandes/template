"""Application configuration class.

"""
__author__ = '${user}'

import logging
from zensols.config import ExtendedInterpolationEnvConfig

logger = logging.getLogger(__name__)


class AppConfig(ExtendedInterpolationEnvConfig):
    def __init__(self, *args, **kwargs):
        if len(args) == 0 and 'config_file' not in kwargs:
            kwargs['config_file'] = 'resources/${project}.conf'
        if 'env' not in kwargs:
            kwargs['env'] = {}
        env = kwargs['env']
        defs = {'app_root': '.'}
        for k, v in defs.items():
            if k not in env:
                if logger.isEnabledFor(logging.INFO):
                    logger.info(f'using default {k} = {v}')
                env[k] = v
        super().__init__(*args, default_expect=True, **kwargs)
