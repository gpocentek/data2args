#######
Readers
#######

.. _readers_yaml:

YAML reader
===========

The ``yaml`` reader consumes a YAML string. It supports the following
argument types:

* ``interger``
* ``float``
* ``string``
* ``boolean``
* ``list``
* ``choice``

Use the following code to create and use a YAML loader:

.. code-block:: python

   import data2args

   reader = data2args.get_reader('yaml')
   reader.load(yaml_string)

The expected data is a list of hashes. Each hash can contain the following
keys:

.. list-table::
   :widths: 25 25 10 40
   :header-rows: 1

   * - Key name
     - Type
     - Mandatory
     - Detail
   * - ``key``
     - string
     - yes
     - The name of the argument
   * - ``type``
     - string
     - no
     - The type of the argument (see above list)
   * - ``default``
     -
     - no
     - Default value when the argument is not used
   * - ``help``
     - string
     - no
     - Help string the the end user
   * - ``required``
     - string
     - no
     - Whether the argument will be required (default: False)
   * - ``positional``
     - boolean
     - no
     - Whether the argument is positional (default: False)
   * - ``reverted``
     - boolean
     - no
     - Whether the argument is positional (default: False). Only valid with
       ``boolean`` type
   * - ``choices``
     - list
     - no
     - List of accepted values (default: []). Only valid with ``choice`` type

The YAML reader expects to find the list of arguments in a ``parameters``
variable at the root of the YAML tree. If you choose another key, you need to
define it when you load the data:

.. code-block:: python

   reader = data2args.get_reader('yaml')
   reader.load(your_yaml, args_attr='params')

YAML example:

.. code-block:: yaml

   parameters:
     - type: integer
       key: i
     - type: float
       key: f
     - type: string
       key: name
     - type: choice
       key: orientation
       choices: [north, south, east, west]
     - type: boolean
       key: noconfirm
       default: False
       reverted: True
     - type: list
       key: more
     - type: string
       key: who
       positional: True

You can use a path instead of a string. Separate the items with the ``.`` (dot)
character. Items can be strings for dict keys, or integers for list indexes.

For example:

.. code-block:: python

   data = '''
   foo:
     - bar
     - params:
         - type: integer
           name: i
   '''

   reader = data2args.get_reader('yaml')
   reader.load(data, args_attr='foo.1.params')
