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

import unittest

import cerberus
import six

from data2args.transformers import _cerberus
from data2args import types


DEFAULT_KEYS = ['type', 'default', 'required', 'nullable']


class TestArgparseTransformer(unittest.TestCase):
    def test_positional(self):
        tr = _cerberus.Transformer([])

        param = types.BooleanArg('b', positional=True)
        with self.assertRaises(NotImplementedError):
            tr._get_args(param)

    def _test_args(self, keys, args):
        for key in keys:
            self.assertIn(key, args)

        for arg in six.iterkeys(args):
            self.assertIn(arg, keys)

    def test_string_arg(self):
        tr = _cerberus.Transformer([])

        param = types.StringArg('dummy')
        args = tr._get_args(param)
        self._test_args(DEFAULT_KEYS, args)
        self.assertEqual(args['type'], 'string')

    def test_choice_arg(self):
        tr = _cerberus.Transformer([])

        param = types.ChoiceArg('dummy', choices=['a', 'b'])
        args = tr._get_args(param)
        self._test_args(DEFAULT_KEYS + ['allowed'], args)
        self.assertEqual(args['type'], 'string')

    def test_boolean_arg(self):
        tr = _cerberus.Transformer([])

        param = types.BooleanArg('dummy')
        args = tr._get_args(param)
        self._test_args(DEFAULT_KEYS, args)
        self.assertEqual(args['type'], 'boolean')

    def test_list_arg(self):
        tr = _cerberus.Transformer([])

        param = types.ListArg('dummy')
        args = tr._get_args(param)
        self._test_args(DEFAULT_KEYS, args)
        self.assertEqual(args['type'], 'list')

    def test_integer_arg(self):
        tr = _cerberus.Transformer([])

        param = types.IntegerArg('dummy')
        args = tr._get_args(param)
        self._test_args(DEFAULT_KEYS, args)
        self.assertEqual(args['type'], 'integer')

    def test_float_arg(self):
        tr = _cerberus.Transformer([])

        param = types.FloatArg('dummy')
        args = tr._get_args(param)
        self._test_args(DEFAULT_KEYS, args)
        self.assertEqual(args['type'], 'float')

    def test_transform(self):
        tr = _cerberus.Transformer([
            types.StringArg('string'),
            types.ChoiceArg('choice', choices=['a', 'b']),
            types.ListArg('list'),
            types.BooleanArg('boolean'),
            types.IntegerArg('integer'),
            types.FloatArg('float'),
        ])
        validator = tr.transform()
        self.assertIsInstance(validator, cerberus.validator.Validator)
