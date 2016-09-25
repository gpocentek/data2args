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


class Reader(readers.BaseClass):
    def __init__(self):
        self._params = []

    def load(self, data, args_attr='parameters', constraints_attr=None):
        """Parser for yaml input.

        Args:
            data: yaml object
            args_attr: where should we get the interesting data
            constraints_attr: attr holding constraints
        """
        data = yaml.load(data, Loader=yaml.SafeLoader)
        try:
            self._src = data[args_attr]
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