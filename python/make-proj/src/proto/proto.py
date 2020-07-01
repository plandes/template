import logging
from zensols.config import ClassImporter
from ${namespace} import AppConfig

logger = logging.getLogger(__name__)


def instance(name, info=(), debug=()):
    conf = AppConfig()
    for l in debug:
        logging.getLogger(f'${namespace}.{l}').setLevel(logging.DEBUG)
    for l in info:
        logging.getLogger(f'${namespace}.{l}').setLevel(logging.INFO)
    return ClassImporter(name).instance(conf)


def tmp():
    app = instance('${namespace}.${appshortname}.${appclass}', debug='${appshortname}'.split())
    app.tmp()


def main():
    logging.basicConfig(level=logging.WARNING)
    run = 1
    {1: tmp,
     }[run]()


main()
