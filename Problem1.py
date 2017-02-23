

def string2freq(x): # x is a string of symbols from alphabet S
    S=vector(x) #list of unique symbols not yet in lexigraphical priority binary heap in an vector
    #store numbers as (key, value) = (leter, frequency)

		#insert:
    for i in (len(x) - 1):
        if (s[i/2] == s[i]): increment f[i]

		if (s[i/2] < S[i]):
			#swap the terms

	#historgram of frequencies of symbols in x, same order:
	f=vector(frequencies) #shorthand

	return S, f;

<<<<<<< HEAD

def huffmanEncode(S, f): # f is a vector of symbol frequencies, from above
	H.empty() #initialize H
	for i=1 in n : H.insert(i,f[i])
	for k=n+1 in 2n-1 :
		i = H.deletmin()
		j= H.deletmin()
		#creat a node numbered k with children i,j
		f[k] = f[i]+f[j]
		H.insert(k,f[k])
	#creat t and return in
	return T


	def encodeString(x,T):
	y = #empty string
	for i=1 to x.len() : y += T[x[i]] # encode each symbol of x
	return y
=======
def encodeString(x,T):ghvgh
    # TODO: Part (iii)


nhhbhb
jh
>>>>>>> origin/master
