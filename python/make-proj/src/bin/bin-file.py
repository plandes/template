#!/usr/bin/env python

from ${namespace} import ConfAppCommandLine

if __name__ == '__main__':
    cl = ConfAppCommandLine()
    #cl.invoke('info -w 2 -o a_new_message'.split(' '))
    cl.invoke()
