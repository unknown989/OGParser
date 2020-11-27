exec = parser
flags = -g -Wall -Wformat-security
compiler = g++
out = a.out


$(exec) : $(exec).cpp
	$(compiler) $(flags) -o $(out) $(exec).cpp

clean:
	rm *.out


