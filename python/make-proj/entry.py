#[[#!/usr/bin/env python]]#

from typing import List
import sys
from pathlib import Path


def configure_from_entry_point(entry_path: Path) -> Path:
    src_path = entry_path.parent / 'src' / 'python'
    conf_path = entry_path.parent / 'resources' / '${project}.conf'
    sys.path.append(str(src_path))
    args = sys.argv + ['-c', str(conf_path)]
    return conf_path, args[1:]


def main(conf_path: Path, args: List[str]):
    from ${namespace} import ConfAppCommandLine, AppConfig
    AppConfig.DEFAULT_APP_ROOT = str(conf_path.parent.parent)
    ConfAppCommandLine().invoke(args)


if __name__ == '__main__':
    conf_path, args = configure_from_entry_point(Path(sys.argv[0]))
    main(conf_path, args)
