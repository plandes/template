#set ( $environ = $project.toUpperCase() )
#!/usr/bin/env python

from typing import List, Dict, Any
import sys
import os
from pathlib import Path


def main(args: List[str], **factory_kwargs: Dict[str, Any]):
    entry_path = Path(args[0])
    src_path = entry_path.parent / 'src' / 'python'
    conf_path = entry_path.parent / 'test-resources' / '${project}.conf'
    if not conf_path.exists():
        conf_path = Path(os.environ['${environ}RC'])
    args = args + ['-c', str(conf_path)]
    sys.path.append(str(src_path))
    from ${namespace} import main
    main(args[1:], **factory_kwargs)


def proto():
    print('-->proto')
    try:
        main('_ proto'.split(), reload_pattern=r'^${namespace}')
    except SystemExit as e:
        print(f'exit: {e}')


if (__name__ == '__main__'):
    # when running from a shell, run the CLI entry point
    import __main__ as mmod
    if hasattr(mmod, '__file__'):
        main(sys.argv)
    # otherwise, assume a Python REPL and run the prototyping method
    else:
        proto()
