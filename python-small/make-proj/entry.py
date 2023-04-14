#set ( $environ = $project.toUpperCase() )
#!/usr/bin/env python

from zensols.cli import ConfigurationImporterCliHarness


if (__name__ == '__main__'):
    harness = ConfigurationImporterCliHarness(
        src_dir_name='src',
        package_resource='${namespace}',
        config_path='etc/${project}.conf',
        proto_args='proto',
        proto_factory_kwargs={'reload_pattern': r'^${namespace}'},
    )
    harness.run()
