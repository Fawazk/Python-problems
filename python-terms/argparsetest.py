import argparse


# Initializing Parser
parser = argparse.ArgumentParser(description ='sort some integers.')

# Adding Argument
parser.add_argument('integers',
					metavar ='N',
					type = float,
					nargs = '+',
					help ='an integer for the accumulator',
					# default = 1.0,
					)

# parser.add_argument('sum',
# 					action ='store_const',
# 					const = sum)


# parser.add_argument('len',
# 					action ='store_const',
# 					const = len)

print(parser)
args = parser.parse_args()
print(args)
# add = args.sum(args.integers)
# length = args.len(args.integers)
# average = add / length
# print(average)