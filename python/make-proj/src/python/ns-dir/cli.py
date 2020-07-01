"""Command line entry point to the application.

"""
__author__ = '${user}'


from zensols.cli import OneConfPerActionOptionsCliEnv
from ${namespace} import (
    ${appclass},
    AppConfig,
)


class ConfAppCommandLine(OneConfPerActionOptionsCliEnv):
    def __init__(self):
        dry_run_op = [None, '--dryrun', False,
                      {'dest': 'dry_run',
                       'action': 'store_true', 'default': False,
                       'help': 'do not do anything, just act like it'}]
        msg_op = ['-m', '--message', True,  # require argument
                  {'dest': 'message', 'metavar': 'STRING',
                   'help': 'a message to print'}]
        outdir_op = ['-o', '--outputdir', False,
                     {'dest': 'out_dir', 'metavar': 'DIRECTORY',
                      'help': 'the directory to output the website'}]
        cnf = {'executors':
               [{'name': 'exporter',
                 'executor': lambda params: ${appclass}(**params),
                 'actions': [{'name': 'doit',
                              'meth': 'print_message',
                              'doc': 'action help explains how to do it',
                              'opts': [dry_run_op, msg_op, outdir_op]}]}],
               'config_option': {'name': 'config',
                                 'expect': True,
                                 'opt': ['-c', '--config', False,
                                         {'dest': 'config',
                                          'metavar': 'FILE',
                                          'help': 'configuration file'}]},
               'whine': 1}
        super().__init__(cnf, config_env_name='${project}rc',
                         pkg_dist='${namespace}',
                         config_type=AppConfig, no_os_environ=True)


def main():
    cl = ConfAppCommandLine()
    cl.invoke()
