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
import unittest

import six

from data2args.transformers import _argparse
from data2args import types


DEFAULT_KEYS = ['default', 'help', 'required']


class TestArgparseTransformer(unittest.TestCase):
    def test_parent(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('foo')

        tr = _argparse.Transformer([types.StringArg('dummy')])
        new_parser = tr.transform(parser)
        self.assertEqual(new_parser, parser)
        args = new_parser.parse_args(['--dummy=dummy', 'foo'])
        self.assertTrue(hasattr(args, 'foo'))
        self.assertTrue(hasattr(args, 'dummy'))

        tr = _argparse.Transformer([types.StringArg('dummy')])
        new_parser = tr.transform()
        self.assertNotEqual(new_parser, parser)

    def test_positional(self):
        tr = _argparse.Transformer([])

        param = types.BooleanArg('b')
        key, args = tr._get_args(param)
        self.assertIn('required', args)
        self.assertTrue(key.startswith('--'))

        param = types.BooleanArg('b', positional=True)
        key, args = tr._get_args(param)
        self.assertNotIn('required', args)
        self.assertFalse(key.startswith('--'))

    def _test_args(self, keys, args):
        for key in keys:
            self.assertIn(key, args)

        for arg in six.iterkeys(args):
            self.assertIn(arg, keys)

    def test_string_arg(self):
        tr = _argparse.Transformer([])

        param = types.StringArg('dummy')
        key, args = tr._get_args(param)
        self._test_args(DEFAULT_KEYS, args)

    def test_choice_arg(self):
        tr = _argparse.Transformer([])

        param = types.ChoiceArg('dummy', choices=['a', 'b'])
        key, args = tr._get_args(param)
        self._test_args(DEFAULT_KEYS + ['choices'], args)

    def test_boolean_arg(self):
        tr = _argparse.Transformer([])

        param = types.BooleanArg('dummy')
        key, args = tr._get_args(param)
        self._test_args(['required', 'action', 'help'], args)
        self.assertIn(args['action'], ['store_true', 'store_false'])

    def test_list_arg(self):
        tr = _argparse.Transformer([])

        param = types.ListArg('dummy')
        key, args = tr._get_args(param)
        self._test_args(DEFAULT_KEYS + ['action'], args)
        self.assertEqual(args['action'], 'append')

    def test_integer_arg(self):
        tr = _argparse.Transformer([])

        param = types.IntegerArg('dummy')
        key, args = tr._get_args(param)
        self._test_args(DEFAULT_KEYS + ['type'], args)
        self.assertEqual(args['type'], int)

    def test_float_arg(self):
        tr = _argparse.Transformer([])

        param = types.FloatArg('dummy')
        key, args = tr._get_args(param)
        self._test_args(DEFAULT_KEYS + ['type'], args)
        self.assertEqual(args['type'], float)

    def test_duplicated_keys(self):
        tr = _argparse.Transformer([
            types.StringArg('dummy'),
            types.BooleanArg('dummy')
        ])
        with self.assertRaises(argparse.ArgumentError):
            tr.transform()

    def test_transform(self):
        tr = _argparse.Transformer([
            types.StringArg('string'),
            types.ChoiceArg('choice', choices=['a', 'b']),
            types.ListArg('list'),
            types.BooleanArg('boolean'),
            types.IntegerArg('integer'),
            types.FloatArg('float'),
            types.FloatArg('float', positional=True)
        ])
        parser = tr.transform()
        self.assertIsInstance(parser, argparse.ArgumentParser)
