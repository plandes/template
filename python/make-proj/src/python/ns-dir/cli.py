from zensols.actioncli import OneConfPerActionOptionsCliEnv
from ${namespace} import ${appclass}


class ConfAppCommandLine(OneConfPerActionOptionsCliEnv):
    def __init__(self):
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
                              'opts': [msg_op, outdir_op]}]}],
               'config_option': {'name': 'config',
                                 'expect': False,
                                 'opt': ['-c', '--config', False,
                                         {'dest': 'config',
                                          'metavar': 'FILE',
                                          'help': 'configuration file'}]},
               'whine': 1}
        super(ConfAppCommandLine, self).__init__(
            cnf, config_env_name='${project}rc', pkg_dist='${namespace}')


def main():
    cl = ConfAppCommandLine()
    cl.invoke()
