
x="the road not taken by robert frost two roads diverged in a yellow wood, and sorry i could not travel both and be one traveler, long i stood and looked down one as far as i could to where it bent in the undergrowth; then took the other, as just as fair, and having perhaps the better claim, because it was grassy and wanted wear; though as for that the passing there had worn them really about the same, and both that morning equally lay in leaves no step had trodden black. oh, i kept the first for another day! yet knowing how way leads on to way, i doubted if i should ever come back. i shall be telling this with a sigh somewhere ages and ages hence: two roads diverged in a wood, and i- i took the one less traveled by, and that has made all the difference."
def string2freq(x): # x is a string of symbols from alphabet S
    S=vector(x) #list of unique symbols not yet in lexigraphical priority binary heap in an vector
    #store numbers as (key, value) = (leter, frequency)

		#insert:
    for i in (len(x) - 1): #increment by i/2, do not want to check all of the inputs
        if (s[i/2] == s[i]): f[i]+=1

        if (s[i/2] < S[i]):
			#swap the terms

            #historgram of frequencies of symbols in x, same order:
    f=vector(frequencies) #shorthand

    return S, f;

def huffmanEncode(S, f): # f is a vector of symbol frequencies, from above
#using a fixed length code
    H.empty() #initialize H
    #buiding the huffman tree from bottom up, but in an array
    n=len(S)
    for i in n : H.insert(i,f[i])
    k=n+1
    for k in 2*n-1 :
        i = H.deletmin()  # pop the right child
        j=  H.deletmin()   #pop the left child
		#creat a node numbered k with children i,j
        f[k] = f[i]+f[j] # frequencies added together
        H.insert(k,f[k])
        #creat T the codebook and return it
        T=[len(H)]
    return T

def encodeString(x,T):
    y = ""#empty string
    for i in len(x) : y += T[x[i]] # encode each symbol of x
    return y

		f[k] = f[i]+f[j]
		H.insert(k,f[k])
	#creat t and return in
	return T