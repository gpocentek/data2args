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

import inspect
import unittest

import six

from data2args import types


DEFAULT_ATTRS = ['key', 'default', 'help', 'required', 'positional']


class TestTypes(unittest.TestCase):
    def test_types_dict(self):
        # Validate that we only have BaseArg-derived classes in types.TYPES
        for key, cls in six.iteritems(types.TYPES):
            self.assertTrue(issubclass(cls, types.BaseArg))
            self.assertIsInstance(key, str)
            self.assertEqual(key, cls.type_str)

        # Validate that we found all the BaseArg-derived classes
        for name, cls in inspect.getmembers(types, inspect.isclass):
            if not issubclass(cls, types.BaseArg) or cls.__name__ == 'BaseArg':
                continue
            self.assertTrue(cls.type_str in types.TYPES)
            self.assertIs(cls, types.TYPES[cls.type_str])

    def test_default_attrs(self):
        for cls in six.itervalues(types.TYPES):
            self.assertTrue(hasattr(cls, 'base_type'))
            self.assertTrue(hasattr(cls, 'type_str'))

    def _test_attrs_exist(self, obj, attrs):
        for attr in attrs:
            self.assertIn(attr, obj._attrs)

    def test_boolean_arg(self):
        obj = types.BooleanArg('dummy')
        self._test_attrs_exist(obj, DEFAULT_ATTRS)

    def test_integer_arg(self):
        obj = types.IntegerArg('dummy')
        self._test_attrs_exist(obj, DEFAULT_ATTRS)

    def test_float_arg(self):
        obj = types.FloatArg('dummy')
        self._test_attrs_exist(obj, DEFAULT_ATTRS)

    def test_string_arg(self):
        obj = types.StringArg('dummy')
        self._test_attrs_exist(obj, DEFAULT_ATTRS)

    def test_list_arg(self):
        obj = types.ListArg('dummy')
        self._test_attrs_exist(obj, DEFAULT_ATTRS)

    def test_choice_arg(self):
        obj = types.ChoiceArg('dummy', choices=['foo', 'bar'])
        self._test_attrs_exist(obj, DEFAULT_ATTRS + ['choices'])

    def test_get_attr(self):
        obj = types.BooleanArg('dummy')
        self.assertEqual('dummy', obj.key)

    def test_inexisting_attr(self):
        obj = types.BooleanArg('dummy')
        with self.assertRaises(KeyError):
            obj.not_there
