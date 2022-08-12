#set ( $environ = $project.toUpperCase() )
#!/usr/bin/env python

from zensols.cli import ApplicationFactory as CliApplicationFactory
from zensols.cli import ConfigurationImporterCliHarness


class ApplicationFactory(CliApplicationFactory):
    def __init__(self, *args, **kwargs):
        kwargs['package_resource'] = '${namespace}'
        super().__init__(*args, **kwargs)


if (__name__ == '__main__'):
    harness = ConfigurationImporterCliHarness(
        src_dir_name='src',
        app_factory_class=ApplicationFactory,
        config_path='etc/${project}.conf',
        proto_args='proto',
        proto_factory_kwargs={'reload_pattern': r'^${namespace}'},
    )
    harness.run()
