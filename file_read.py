import string
def fileRead(file_path):
    f=open(file_path,'r')
    content=f.read()
	translator = str.maketrans('', '', string.punctuation)
	u_content=content.translate(translator)
	return u_content
	
fileRead('C:\\Users\\emenya\\Desktop\\smile.txt')