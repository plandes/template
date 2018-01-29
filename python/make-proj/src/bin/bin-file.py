#!/usr/bin/env python

from zensols.actioncli import SimpleActionCli
from ${namespace} import HelloWorld

class AppCommandLine(SimpleActionCli):
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
        SimpleActionCli.__init__(self, executors, invokes, config=conf,
                                 opts=opts, manditory_opts=manditory_opts,
                                 environ_opts=environ_opts)

    def config_parser(self):
        parser = self.parser
        self._add_whine_option(parser)
        parser.add_option('-o', '--optname', dest='message')

if __name__ == '__main__':
    cl = AppCommandLine()
    inp = 'info -w 2 -o a_new_message'
    args = inp.split(' ')
    cl.invoke(args)
