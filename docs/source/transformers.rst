############
Transformers
############

.. _transformers_argparse:

Argparse transformer
====================

The ``argparse`` transformer returns an ArgumentParser object.

Use the following code to create and use the argparse transformer:

.. code-block:: python

   import data2args

   transformer = data2args.get_transformer('argparse', reader)
   parser = transformer.transform()

   # use the parser
   args = parser.parse_args()

.. _transformers_cerberus:

Cerberus transformer
====================

The ``cerberus`` transformer returns a ``cerberus.validator.Validator`` object.

Use the following code to create and use the cerberus transformer:

.. code-block:: python

   import data2args

   transformer = data2args.get_transformer('cerberus', reader)
   validator = transformer.transform()

   # use the parser
   if validator.validate(kwargs):
       return validator.normalized(kwargs)
   else:
       print(validator.errors)
