#set ( $prog = $project.substring(0, 1).toUpperCase() + $project.substring(1) )
"""Application domain classes.

"""
__author__ = '${user-name}'

from zensols.util import APIError


class ${prog}Error(APIError):
    """Thrown for any application level error.

    """
