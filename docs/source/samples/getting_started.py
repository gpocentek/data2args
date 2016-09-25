# simple
import data2args

my_args = """---
parameters:
 - key: direction
   type: choice
   choices: ['north', 'south', 'east', 'west']
   help: the direction to follow
 - key: steps
   type: integer
   default: 1
   help: the number of steps to walk
 - key: who
   type: string
   positional: True
   help: the character you want to move
"""
parser = data2args.transform('yaml', 'argparse', my_args)

args = parser.parse_args()
print(args)
# end simple

# complex
import data2args

my_args = """---
parameters:
 - key: direction
   type: choice
   choices: ['north', 'south', 'east', 'west']
   help: the direction to follow
 - key: steps
   type: integer
   default: 1
   help: the number of steps to walk
 - key: who
   type: string
   positional: True
   help: the character you want to move
"""

reader = data2args.get_reader('yaml')
reader.load(my_args)

transformer = data2args.get_transformer('argparse', reader)
parser = transformer.transform()

args = parser.parse_args()
print(args)
# end complex
