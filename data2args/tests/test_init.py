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

import data2args
from data2args import exc
from data2args import readers
import data2args.readers._dummy as r_dummy
from data2args import transformers
import data2args.transformers._dummy as t_dummy
from data2args import types


class TestInit(unittest.TestCase):
    def test_abstract(self):
        with self.assertRaises(TypeError):
            transformers.BaseClass([])

        with self.assertRaises(TypeError):
            readers.BaseClass('fake')

    def test_get_reader(self):
        reader = data2args.get_reader('dummy')
        self.assertIsInstance(reader, r_dummy.Reader)
        self.assertTrue(isinstance(reader, readers.BaseClass))

        reader.load()

        with self.assertRaises(exc.NoSuchReaderError):
            data2args.get_reader('miss')

    def test_get_transformer(self):
        reader = data2args.get_reader('dummy')
        reader.load()

        transformer = data2args.get_transformer('dummy', reader)
        self.assertIsInstance(transformer, t_dummy.Transformer)
        self.assertTrue(isinstance(transformer, transformers.BaseClass))

        src = [types.BooleanArg('dummy')]
        transformer = data2args.get_transformer('dummy', src)
        self.assertIsInstance(transformer, t_dummy.Transformer)
        self.assertTrue(isinstance(transformer, transformers.BaseClass))

        self.assertIs(transformer.transform(), None)

        with self.assertRaises(ValueError):
            data2args.get_transformer('dummy', 'whatever')

        with self.assertRaises(exc.NoSuchTransformerError):
            data2args.get_transformer('miss', [types.BooleanArg('dummy')])

    def test_transform(self):
        with self.assertRaises(exc.NoSuchReaderError):
            data2args.transform('miss', 'miss', [])

        with self.assertRaises(exc.NoSuchTransformerError):
            data2args.transform('dummy', 'miss', [])

        self.assertIs(data2args.transform('dummy', 'dummy',
                                          [types.BooleanArg('dummy')]), None)
