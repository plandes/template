#set ( $environ = $project.toUpperCase() )
#!/usr/bin/env python

from zensols.cli import ConfigurationImporterCliHarness

if (__name__ == '__main__'):
    harness = ConfigurationImporterCliHarness(
        src_dir_name='src/python',
        app_factory_class='${namespace}.ApplicationFactory',
        config_path='test-resources/${project}.conf',
        proto_args='doit',
        proto_factory_kwargs={'reload_pattern': r'^${namespace}'},
    )
    harness.run()
