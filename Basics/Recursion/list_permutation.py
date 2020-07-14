
def permutation(listt):

	if len(listt) == 0:
		return []

	if len(listt) == 1:
		return listt

	l = []

	for i in range(len(listt)):

		m = listt[i]
		remlist = listt[:i] + listt[i+1:]

		for p in permutation(remlist):

			l.append(m + p)

	return l

strr = list('abc')
print permutation(strr)