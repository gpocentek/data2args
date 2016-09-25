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


class Data2ArgsError(Exception):
    """Base class for all data2args exceptions."""


class NoSuchTransformerError(Data2ArgsError):
    """The tranformer could not be found."""


class NoSuchReaderError(Data2ArgsError):
    """The reader could not be found."""


class InvalidDataError(Data2ArgsError):
    """Data supplied to the reader could not be parsed."""
