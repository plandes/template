#set ( $prog = $project.substring(0, 1).toUpperCase() + $project.substring(1) )
"""Application domain classes.

"""
__author__ = '${user-name}'

from zensols.cli import ApplicationError


class ${prog}Error(ApplicationError):
    """Thrown for any application level error.

    """
    pass
