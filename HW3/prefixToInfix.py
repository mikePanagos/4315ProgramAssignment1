import re

def tokenizer(opfunction):
	tokens = re.split("[\(,]", opfunction)
	tokens = [x.strip(")").strip() for x in tokens]
	for i, token in enumerate(tokens):
		try:
			tokens[i] = int(tokens[i])
		except:
			continue
	return tokens

def prefixToInfix(tokens):
	try:
		stack = []
		result = 0
		while len(tokens) != 0:
			token = tokens.pop()
			if type(token) is int:
				stack.append(token)
			elif token == "add":
				opd1 = stack.pop()
				opd2 = stack.pop()
				stack.append(opd1 + opd2)
			elif token == "mult":
				opd1 = stack.pop()
				opd2 = stack.pop()
				stack.append(opd1 * opd2)
		result = stack.pop()
	except Exception as e:
		print("error: %s" % e)
	print(result)

opfunction = raw_input("Op Function: ")
while opfunction != "":
	prefixToInfix(tokenizer(opfunction))
	opfunction = ""
	opfunction = raw_input("Op Function: ")
