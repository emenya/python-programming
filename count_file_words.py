import string
def countFileWords(file_path):
    f=open(file_path,'r')
	word_list=f.read().split()
    total_words=len(word_list)
    return total_words
countFileWords('C:\\Users\\emenya\\Desktop\\smile.txt')