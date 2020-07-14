def word_list(phrase, list_of_words, output = None):
	
	if output is None:
		output = []

	for word in list_of_words:

		if phrase.startswith(word):

			output.append(word)

			return word_list(phrase[len(word):],list_of_words,output)

	return output

print word_list('themanran',['the','ran','man'])
print word_list('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
print word_list('themanran', ['clown', 'man', 'ran'])

