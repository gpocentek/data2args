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

import argparse

from data2args import transformers


class Transformer(transformers.BaseClass):
    def _get_args(self, param):
        if param.type_str == 'string':
            args = {'default': param.default,
                    'required': param.required,
                    'help': param.help}
        elif param.type_str == 'choice':
            args = {'default': param.default,
                    'required': param.required,
                    'choices': param.choices,
                    'help': param.help}
        elif param.type_str == 'boolean':
            args = {'required': param.required,
                    'action': ('store_false' if param.reverted
                               else 'store_true'),
                    'help': param.help}
        elif param.type_str == 'list':
            args = {'required': param.required,
                    'action': 'append',
                    'default': param.default,
                    'help': param.help}
        elif param.type_str == 'integer':
            args = {'required': param.required,
                    'type': int,
                    'default': param.default,
                    'help': param.help}
        elif param.type_str == 'float':
            args = {'required': param.required,
                    'type': float,
                    'default': param.default,
                    'help': param.help}

        if param.positional:
            args.pop('required')
            arg_key = param.key
        else:
            arg_key = '--%s' % param.key

        return arg_key, args

    def transform(self, parent=None):
        """Generate the argparse parser.

        Args:
            parent (argparse.ArgumentParser): If not None, new argument will be
                                              added to the parser. Otherwise a
                                              new parser will be created.

        Returns:
            argparse.ArgumentParser: The new parser or an updated parser if
                                     ``parent`` is provided.
        """
        parser = parent if parent else argparse.ArgumentParser()
        for param in self._params:
            key, args = self._get_args(param)
            parser.add_argument(key, **args)

        return parser
