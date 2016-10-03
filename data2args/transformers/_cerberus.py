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

from cerberus import validator

from data2args import transformers


class Transformer(transformers.BaseClass):
    def _get_args(self, param):
        if param.positional is True:
            msg = ('Positional arguments are not supported by the '
                   'cerberus transformer')
            raise NotImplementedError(msg)

        value = {'type': param.type_str,
                 'default': param.default,
                 'required': param.required,
                 'nullable': True}

        if param.type_str == 'choice':
            value.update({'type': 'string',
                          'allowed': param.choices})

        return value

    def transform(self):
        schema = {}
        for param in self._params:
            schema[param.key] = self._get_args(param)

        return validator.Validator(schema)
