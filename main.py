#!/usr/bin/python3


# Modules
import sys
import src.Parser as Parser
import src.CHARACTERS as C

Chars = {
	"semi":C.SEMI_COLON,
	"print":C.PRINT,
	"func exec":C.FUNCTION_RUN,
	"STRINGS":C.STRING_QUOTES
}


# Getting The Source File
source_file = sys.argv[1] if len(sys.argv) > 1 else ""

# Checking if source_file is empty (a.k.a == "")
if not source_file:
	sys.exit("Please Insert a file.og")

else:
	with open(source_file,"r") as f:
		lines = f.readlines()

	lines = [i.strip() for i in lines]
	

	parsing = Parser.lexer(lines,dict(Chars))
	
	print(parsing)


print("Filename : "+source_file)
