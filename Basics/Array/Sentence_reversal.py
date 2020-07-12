
## reverse a string after removing whitespaces

def rev_word(s):
	s.strip()
	res = s.split()
	for i in range(len(res)-1,-1,-1):
		print res[i],

def rev_word2(s):
	return " ".join(reversed(s.split()))

def rev_word3(s):
	return " ".join(s.split()[::-1])

def rev_word4(s):

	words = []
	length = len(s)
	spaces = [' ']
	i = 0
	while i < length:
		if s[i] not in spaces:
			word_start = i;
			while i<length and s[i] not in spaces:
				i+=1

			words.append(s[word_start:i])
		i +=1
	return words

def final_output(words):

	for i in range(len(words)-1,-1,-1):
		words.append(words[i])
		words.pop(i)

	return " ".join(words)




rev_word('This string is being reversed')
print '\n'
print rev_word2('  Hi How are you ')
print rev_word3(' I have no idea what I am doing ')
print final_output(rev_word4(' This is a more manual approach'))
