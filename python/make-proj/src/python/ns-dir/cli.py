"""Command line entry point to the application.

"""
__author__ = '${user}'


from zensols.cli import OneConfPerActionOptionsCliEnv
from dataclasses import dataclass, field, InitVar
from pathlib import Path
from zensols.config import ImportConfigFactory
from ${namespace} import ${appclass}, AppConfig


@dataclass
class Cli(object):
    config: AppConfig
    out_dir: InitVar[Path] = field(default=None)
    dry_run: InitVar[bool] = field(default=False)

    def __post_init__(self, out_dir: Path, dry_run: bool):
        self.factory = ImportConfigFactory(self.config)
        self.${appshortname}: ${appclass} = self.factory(
            '${appshortname}', out_dir=out_dir, dry_run=dry_run)

    def print_message(self):
        self.${appshortname}.tmp()


class ConfAppCommandLine(OneConfPerActionOptionsCliEnv):
    def __init__(self):
        dry_run_op = [None, '--dryrun', False,
                      {'dest': 'dry_run',
                       'action': 'store_true', 'default': False,
                       'help': 'do not do anything, just act like it'}]
        outdir_op = ['-o', '--outputdir', False, # does not require argument
                     {'dest': 'out_dir', 'metavar': 'DIRECTORY',
                      'help': 'the directory to output the website'}]
        cnf = {'executors':
               [{'name': 'exporter',
                 'executor': lambda params: Cli(**params),
                 'actions': [{'name': 'doit',
                              'meth': 'print_message',
                              'doc': 'action help explains how to do it',
                              'opts': [dry_run_op, outdir_op]}]}],
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
