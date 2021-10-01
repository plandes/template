#set ( $environ = $project.toUpperCase() )
#set ( $prog = $project.substring(0, 1).toUpperCase() + $project.substring(1) )
#!/usr/bin/env python

from zensols.cli import ConfigurationImporterCliHarness

ConfigurationImporterCliHarness(
    src_dir_name='src/python',
    app_factory_class='${namespace}.${prog}ApplicationFactory',
    config_path='test-resources/${project}.conf',
    proto_args='-c test-resources/${project}.conf doit',
    proto_factory_kwargs={'reload_pattern': r'^${project}'},
).run()
