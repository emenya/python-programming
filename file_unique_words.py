import string
def fileUniqueWords(file_path):
	f=open(file_path,'r')
	word_list=f.read().split()
	w_c=[]        #word count
	w_c_l=[]            #wor count list
	word_count=0
		for word in word_list:
			word_count=word_list.count(word)
			for x in word_list:
				if x==word:
                    word_list.remove(word)
					w_c.append(word_count)
				w_c_l.append(word) 

	return w_c
	
fileUniqueWords('C:\\Users\\emenya\\Desktop\\smile.txt')


