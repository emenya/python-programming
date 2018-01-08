def getWords(file_path):
     f=open(file_path,'r')
     word_list=f.read().split()
     return word_list
	 
getWords('C:\\Users\\emenya\\Desktop\\smile.txt')