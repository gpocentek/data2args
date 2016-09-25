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

from data2args import readers


@six.add_metaclass(abc.ABCMeta)
class BaseClass(object):
    """Base class for the Transformers.

    Args:
        src (object): Data to transform. 2 object types can be used:

            * a :class:`data2args.readers.BaseClass` object with loaded
              content
            * a list of internal :class:`data2args.types.BaseArg` objects

    Raises:
        ValueError: If the src type is not supported.
    """

    def __init__(self, src):
        if isinstance(src, readers.BaseClass):
            self._params = src.get_source()
        elif isinstance(src, list):
            self._params = src
        else:
            raise ValueError('src should be a list or a reader.')

    @abc.abstractmethod
    def transform(self):
        """Return the result of the tranformation.

        Returns:
            object: Depends on the transformer type.
        """
        return
