# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Gauvain Pocentek <gauvain@pocentek.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Internal representation for arguments.

The data2args.types module provides object classes representing the various
types of argument that data2args know about. When a reader parsers data, it
generates a list of objects whose class is defined here.
"""


class BaseArg(object):
    """Base class for the internal argument classes.

    Args:
        key (str): Name of the argument.
        positional (bool): Whether the argument should be treated as
            positional when parsing command line.
        required (bool): Whether the argument is required. Considered True
            if `positional` is True.
        default: Default value if the argument is not defined.
        help (str): Help string.
    """

    def __init__(self, key, positional=False, required=False, default=None,
                 help=None):
        self._attrs = {}
        self._attrs['key'] = key
        self._attrs['default'] = default
        self._attrs['help'] = help
        self._attrs['required'] = required
        self._attrs['positional'] = positional

    def __getattr__(self, key):
        return self._attrs[key]


class BooleanArg(BaseArg):
    """Represents a boolean argument.

    Args:
        key (str): Name of the argument.
        positional (bool): Whether the argument should be treated as
            positional when parsing command line.
        reverted (bool): If True, and the argument is provided without
            value, the generated value will be False.
        required (bool): Whether the argument is required. Considered True
            if `positional` is True.
        default: Default value if the argument is not defined.
        help (str): Help string.
    """
    base_type = bool
    type_str = 'boolean'

    def __init__(self, key, positional=False, reverted=False, required=False,
                 default=None, help=None):
        super(BooleanArg, self).__init__(key,
                                         positional=positional,
                                         required=required,
                                         default=default,
                                         help=help)
        self._attrs['reverted'] = reverted


class IntegerArg(BaseArg):
    """Represents an integer argument."""
    base_type = int
    type_str = 'integer'


class FloatArg(BaseArg):
    """Represents a float argument."""
    base_type = float
    type_str = 'float'


class StringArg(BaseArg):
    """Represents string argument."""
    base_type = str
    type_str = 'string'


class ListArg(BaseArg):
    """Represents a list argument."""
    base_type = list
    type_str = 'list'


class ChoiceArg(BaseArg):
    """Represents a choice argument.

    Args:
        key (str): Name of the argument.
        choices (list): List of available choices to pick from.
        positional (bool): Whether the argument should be treated as
            positional when parsing command line.
        required (bool): Whether the argument is required. Considered True
            if `positional` is True.
        default: Default value if the argument is not defined.
        help (str): Help string.
    """
    base_type = str
    type_str = 'choice'

    def __init__(self, key, choices, positional=False, required=False,
                 default=None, help=None):
        super(ChoiceArg, self).__init__(key,
                                        positional=positional,
                                        required=required,
                                        default=default,
                                        help=help)
        self._attrs['choices'] = choices


TYPES = {cls.type_str: cls for cls in locals().values()
         if hasattr(cls, 'base_type')}
