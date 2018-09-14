## todo: need to iterate over dots to expand `packages`--only two levels supported
#set($packages = $namespace.substring(0, $namespace.indexOf(".")))
from pathlib import Path
from zensols.pybuild import SetupUtil

SetupUtil(
    setup_path=Path(__file__).parent.absolute(),
    name="${namespace}",
    package_names=['${packages}', '${namespace}'],
    # package_data={'': ['*.html', '*.js', '*.css', '*.map', '*.svg']},
    description='${project-description}',
    user='${user}',
    project='${project}',
    keywords=['tooling'],
    # has_entry_points=False,
).setup()
