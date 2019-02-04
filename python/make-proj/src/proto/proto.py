import logging
import importlib
from ${namespace} import AppConfig

logger = logging.getLogger(__name__)


def create_config():
    return AppConfig('resources/${project}.conf')


def tmp():
    import ${namespace}.${appshortname}
    importlib.reload(${namespace}.${appshortname})
    logging.getLogger('zensols.actioncli').setLevel(logging.INFO)
    logging.getLogger('${namespace}.${appshortname}').setLevel(logging.DEBUG)
    app = ${namespace}.${appshortname}.${appclass}(create_config())
    app.tmp()


def main():
    logging.basicConfig(level=logging.WARNING)
    run = 1
    {1: tmp,
     }[run]()


main()
