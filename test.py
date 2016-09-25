import pprint

import yaml

import data2args


data = """parameters:
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
    key: blah
  - type: string
    key: pos1
    required: True
    positional: True
"""

parser = data2args.transform('yaml', 'argparse', data)

args = parser.parse_args()
print(vars(args))
