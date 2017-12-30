import configparser, logging, os

logger = logging.getLogger('${namespace}.config')

class Config(object):
    """
    Application configuration.
    """
    def __init__(self, config_file=None):
        self.config_file = config_file

    def get_options(self, opt_keys=None):
        cfile = self.config_file
        if not os.path.isfile(cfile):
            raise IOError('no such file: %s' % cfile)
        conf = configparser.ConfigParser()
        conf.read(os.path.expanduser(cfile))
        section = 'default'
        opts = {}
        if opt_keys == None:
            opt_keys = conf.options(section)
        else:
            opt_keys = set(opt_keys).intersection(set(conf.options(section)))
        for option in opt_keys:
            opts[option] = conf.get(section, option)
        return opts

    @property
    def options(self):
        return self.get_options()
