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

"""Generate argument parsers from data description.

data2args reads static data (YAML or other serialization languages) and creates
an argument parser (argparse) using this data.

It provides 2 main components:

* ``readers`` parse the data and store them using internal object classes
* ``transformers`` turn internal data to usable objects

The following example describes how you would typically use data2args::

    import data2args

    parser = data2args.transform('yaml', 'argparse', my_yaml_string)
    args = parser.parse_args()

*Supported readers*:

* :ref:`readers_yaml`

*Supported transformers*:

* :ref:`transformers_argparse`
"""

import importlib

from data2args import exc


def get_reader(type):
    """Return a Reader object of the given type.

    Args:
        type (str): Expected input data type. Must be a data2arg known type.

    Returns:
        data2args.readers.BaseClass: A Reader object.

    Raises:
        NoSuchReaderError: If the given type is not known by data2args.
    """
    try:
        module = importlib.import_module('data2args.readers._%s' % type)
    except ImportError:
        raise exc.NoSuchReaderError('No such reader: %s' % type)

    return module.Reader()


def get_transformer(type, src):
    """Return a Transformer object of the given type.

    Args:
        type (str): Expected output type. Must be a data2arg known type.
        src: Source data. Can be a Reader object with loaded data, or a list of
            BaseArg objects

    Returns:
        object: An object whose type depends on the chosen transformer.

    Raises:
        NoSuchTransformerError: If the given type is not known by data2args
    """
    try:
        module = importlib.import_module('data2args.transformers._%s' % type)
    except ImportError:
        raise exc.NoSuchTransformerError('No such transformer: %s' % type)

    return module.Transformer(src)


def transform(reader_type, transformer_type, data):
    """Load data, transform it and return the expected parser.

    Args:
        reader_type (str): Expected input data type. Must be a data2arg known
            type.
        transformer_type (str): Expected output type. Must be a data2arg known
            type.
        data: Data to be fed to the reader.

    Returns:
        object: An object whose type depends on the chosen transformer.

    Raises:
        NoSuchReaderError: If the given reader type is not known by data2args.
        NoSuchTransformerError: If the given transformer type is not known by
            data2args
        InvalidDataError: If the data supplied cannot be used by the reader
    """
    reader = get_reader(reader_type)
    reader.load(data)
    transformer = get_transformer(transformer_type, reader)
    return transformer.transform()
