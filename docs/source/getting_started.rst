##############################
Getting Started with data2args
##############################

Introduction
============

The data2args library provides an API to transform data (YAML, JSON, python
structures) to argument parsers (command line, kwargs parsers).

It is based on two main components:

**Readers**
    Readers parse the data to transform it into an internal representation.

**Transformers**
    Transformers use the internal representation to generate argument parsers.

Using the API
=============

The ``data2args`` module exposes a basic API that should be enough in most
cases. It hides the internal representation of data and mechanisms.

The steps are:

#. Create a reader object using :func:`data2args.get_reader`
#. Load data in the reader
#. Create a transformer object using :func:`data2args.get_transformer`
#. Use the tranformer to generate a parser

You can choose to explicitely code these steps, or you can use the
:func:`data2args.transform` function to automate everything.

The following example reads data from YAML and generates an
:func:`argparse.ArgumentParser` object:

.. literalinclude:: samples/getting_started.py
   :start-after: # simple
   :end-before: # end simple

The following example describes all the steps involved:

.. literalinclude:: samples/getting_started.py
   :start-after: # complex
   :end-before: # end complex
