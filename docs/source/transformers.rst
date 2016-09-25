############
Transformers
############

.. _transformers_argparse:

Argparse transformer
====================

The ``argparse`` transformer returns an ArgumentParser object.

Use the following code to create and use a transformer:

.. code-block:: python

   import data2args

   transformer = data2args.get_transformer('argparse', reader)
   parser = transformer.transform()

   # use the parser
   args = parser.parse_args()
