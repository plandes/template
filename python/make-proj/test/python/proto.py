import logging
from zensols.config import ImportConfigFactory
from ${namespace} import AppConfig

logger = logging.getLogger(__name__)


def create_factory():
    conf = AppConfig()
    return ImportConfigFactory(conf, reload=True)


def tmp():
    factory = create_factory()
    ${appshortname} = factory('${appshortname}')
    ${appshortname}.tmp()


def main():
    print()
    logging.basicConfig(level=logging.WARNING)
    logging.getLogger('${namespace}').setLevel(logging.DEBUG)
    run = 1
    {1: tmp,
     }[run]()


main()
