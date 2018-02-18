from zensols.actioncli import OneConfPerActionOptionsCli
from zensols.actioncli import SimpleActionCli
from ${namespace} import HelloWorld

VERSION='0.1'

# you probably do _not_ want this one
class SimpleAppCommandLine(SimpleActionCli):
    def __init__(self, conf_file=None, use_environ=False, config_mand=False):
        opts = {'message', 'config'}
        manditory_opts = {'message'}
        if config_mand: manditory_opts.update({'config'})
        if use_environ: environ_opts = opts
        else: environ_opts = {}
        executors = {'app_test_key': lambda params: HelloWorld(**params)}
        invokes = {'info': ['app_test_key', 'print_message', 'print hello world']}
        if conf_file: conf = Config(conf_file, robust=True)
        else: conf = None
        super(SimpleAppCommandLine, self).__init__(self, executors, invokes, config=conf,
                                                   opts=opts, manditory_opts=manditory_opts,
                                                   environ_opts=environ_opts)
        
    def config_parser(self):
        parser = self.parser
        self._add_whine_option(parser)
        parser.add_option('-o', '--optname', dest='message')

# recommended app command line
class ConfAppCommandLine(OneConfPerActionOptionsCli):
    def __init__(self):
        cnf = {'executors':
               [{'name': 'hello',
                 'executor': lambda params: HelloWorld(**params),
                 'actions':[{'name': 'doit',
                             'meth': 'print_message',
                             'opts': [['-m', '--message', True, # require argument
                                       {'dest': 'message', 'metavar': 'STRING',
                                        'help': 'a message to print'}]]}]}],
               # uncomment to add a configparse (ini format) configuration file
               # 'config_option': {'name': 'config',
               #                   'opt': ['-c', '--config', False,
               #                           {'dest': 'config', 'metavar': 'FILE',
               #                            'help': 'configuration file'}]},
               'whine': 1}
        super(ConfAppCommandLine, self).__init__(cnf, version=VERSION)

def main():
    cl = ConfAppCommandLine()
    cl.invoke()
