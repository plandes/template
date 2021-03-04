#set ( $environ = $project.toUpperCase() )
#!/usr/bin/env python

import sys
import os
from pathlib import Path


if __name__ == '__main__':
    entry_path = Path(sys.argv[0])
    src_path = entry_path.parent / 'src' / 'python'
    conf_path = entry_path.parent / 'test-resources' / '${project}.conf'
    if not conf_path.exists():
        conf_path = Path(os.environ['${environ}RC'])
    args = sys.argv + ['-c', str(conf_path)]
    sys.path.append(str(src_path))
    if 0:
        import logging
        logging.basicConfig(level=logging.DEBUG)
    from ${namespace} import main
    main(args[1:])
