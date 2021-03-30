#set ( $environ = $project.toUpperCase() )
#!/usr/bin/env python

from dataclasses import dataclass
import sys
import os
from pathlib import Path
from zensols.config import DictionaryConfig
from zensols.cli import ApplicationFactory


@dataclass
class ${appclass}Factory(ApplicationFactory):
    @classmethod
    def instance(cls: type, root_dir: Path = Path('.'), **kwargs):
        dconf = DictionaryConfig({'appenv': {'root_dir': str(root_dir)}})
        return cls(package_resource='${namespace}.${appshortname}',
                   children_configs=(dconf,), **kwargs)


def main(**factory_kwargs):
    entry_path = Path(sys.argv[0])
    src_path = entry_path.parent / 'src'
    conf_path = entry_path.parent / 'etc' / '${project}.conf'
    if not conf_path.exists():
        conf_path = Path(os.environ['${environ}RC'])
    args = sys.argv + ['-c', str(conf_path)]
    sys.path.append(str(src_path))
    cli = ${appclass}Factory.instance(**factory_kwargs)
    cli.invoke(args[1:])


def proto():
    print('-->proto')
    main(reload_factory=True)


if (__name__ == '__main__'):
    # when running from a shell, run the CLI entry point
    import __main__ as mmod
    if hasattr(mmod, '__file__'):
        main()
    # otherwise, assume a Python REPL and run the prototyping method
    else:
        proto()
