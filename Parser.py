#!/usr/bin/python3
import sys
from src import *
source_file = sys.argv[1] if len(sys.argv) > 1 else ""

if not source_file:
	sys.exit("Please Insert a file.og")

else:
	with open(source_file,"r") as f:
		lines = f.readlines()

	lines = [i.strip() for i in lines]




	print(lines)


print("Filename : "+source_file)
