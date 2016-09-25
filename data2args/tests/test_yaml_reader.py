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

import yaml

from data2args import exc
from data2args.readers import _yaml
from data2args import types


simple_sample = '''---
parameters:
    - type: integer
      key: i
'''

missing_key_sample = '''---
parameters:
    - type: integer
'''

unknown_key_sample = '''---
parameters:
    - type: integer
      key: i
      dunno: lol
'''

other_args_attr_sample = '''---
args:
    - type: integer
      key: i
'''

invalid_yaml_sample = '''---
parameters:
    no: valid
      yaml: here
'''


class TestYAMLReader(unittest.TestCase):
    def setUp(self):
        self.reader = _yaml.Reader()

    def test_invalid_yaml(self):
        with self.assertRaises(yaml.error.YAMLError):
            self.reader.load(invalid_yaml_sample)

    def test_load_valid_sample(self):
        self.reader.load(simple_sample)
        self.assertEqual(len(self.reader._params), 1)
        self.assertTrue(isinstance(self.reader._params[0], types.IntegerArg))
        self.assertEqual(self.reader._params[0].key, 'i')

    def test_load_invalid_sample(self):
        with self.assertRaises(exc.InvalidDataError):
            self.reader.load(missing_key_sample)

        with self.assertRaises(exc.InvalidDataError):
            self.reader.load(unknown_key_sample)

    def test_load_args_attr(self):
        self.reader.load(other_args_attr_sample, args_attr='args')
        self.assertEqual(len(self.reader._params), 1)

    def test_invalid_args_attr(self):
        with self.assertRaises(exc.InvalidDataError) as cm:
            self.reader.load(simple_sample, args_attr='foo')

        self.assertEqual('No such key: foo', str(cm.exception))
