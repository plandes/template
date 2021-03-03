#!/usr/bin/env python

import sys
from pathlib import Path


if __name__ == '__main__':
    entry_path = Path(sys.argv[0])
    src_path = entry_path.parent / 'src' / 'python'
    conf_path = entry_path.parent / 'test-resources' / '${project}.conf'
    args = sys.argv + ['-c', str(conf_path)]
    sys.path.append(str(src_path))
    if 0:
        import logging
        logging.basicConfig(level=logging.DEBUG)
    from ${namespace} import main
    main(args[1:])
