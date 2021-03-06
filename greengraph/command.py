from argparse import ArgumentParser
from .makeGraph import MakeGraph # Note python 3 relative import

def process():
	parser = ArgumentParser(description = "Generate a plot of green pixels intensity between two locations.")

	parser.add_argument('--from', '-f', help='start location', type=str, dest="start")
	parser.add_argument('--to', '-t', help='end location', type=str, dest="end")
	parser.add_argument('--steps', '-s', help='Number of steps between locations', type=int, dest="steps")
	parser.add_argument('--out', '-o', help='Output file name (e.g. plot.png)', type=str, dest="out")

	arguments= parser.parse_args()

	MakeGraph(arguments.start, arguments.end, arguments.steps, arguments.out)

if __name__ == "__main__":
	process()