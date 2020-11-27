def lexer(code:list,Chars:dict):
	tokens = list()
	for i in code:
		for k in Chars:
			if type(Chars.get(k)) is not list:
				if i.find(Chars.get(k)) >= 0:
					tokens.append(Chars.get(k))
			else:
				for s in range(len(Chars.get(k))-1):
					if i.find(Chars[k][s]) >= 0:
						tokens.append(Chars[k][s])

	return tokens
		
