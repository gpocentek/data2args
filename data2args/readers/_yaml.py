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

import yaml

from data2args import exc
from data2args import readers
from data2args import types as _types


def _get_from_path(data, path):
    """Returns the data located at path.

    Path is of the form 'a.b.c' where each item can be either a string
    representing the key of a dict or an integer representing the index in a
    list. Valid examples are 'data.parameters', 'data.0.args'.

    Args:
        data: The data in which we should descend.
        path: The path to follow.

    Returns:
        The value found at path.

    Raises:
        KeyError: When the path is not valid for data.
    """
    def get_data_at_path(data, path):
        if isinstance(data, dict):
            return data[path]
        else:
            return data[int(path)]

    items = path.split('.')
    for item in items:
        try:
            data = get_data_at_path(data, item)
        except (KeyError, ValueError):
            raise KeyError
    return data


class Reader(readers.BaseClass):
    def load(self, data, args_attr='parameters', constraints_attr=None):
        """Parser for yaml input.

        Args:
            data: yaml object
            args_attr: where should we get the interesting data
            constraints_attr: attr holding constraints
        """
        data = yaml.load(data, Loader=yaml.SafeLoader)
        try:
            self._src = _get_from_path(data, args_attr)
        except KeyError:
            raise exc.InvalidDataError('No such key: %s' % args_attr)
        self._constraints = (data[constraints_attr] if constraints_attr
                             else None)
        for param in self._src:
            if 'key' not in param or 'type' not in param:
                raise exc.InvalidDataError('Missing type or key attribute.')
            _type = param.pop('type')

            try:
                param = _types.TYPES[_type](**param)
            except TypeError as e:
                raise exc.InvalidDataError(
                    'Invalid attribute: %s' % str(e).split()[-1])
            self._params.append(param)
