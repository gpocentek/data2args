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

import abc

import six


@six.add_metaclass(abc.ABCMeta)
class BaseClass(object):
    """Base class for the Readers."""
    def __init__(self):
        self._params = []

    @abc.abstractmethod
    def load(self, data, args_attr='parameters', constraints_attr=None):
        """Load data for the reader to parse.

        Args:
            data (object): Data to read. Type depends on the reader.
            args_attr (str): Name of the attribute to look for in the data
                to find parameters to use.
            constraints_attr (str): Not used.

        Raises:
            InvalidDataError: If the data could not be parsed by the reader.
        """
        return

    def get_source(self):
        """Return the list of parsed parameters.

        Returns:
            list: The parsed arguments, to be fed to a transformer.
        """
        return self._params
