# This Was A Class Before, The __init__() cost much time, So Do this
str_const_GLUE = '_+_'
def f_glue_word(str_Word1,str_Word2):
	return str_Word1+str_const_GLUE+str_Word2
def f_cut_glue(str_Word):
	int_Index = str_Word.find(str_const_GLUE)
	str_Word1 = str_Word[ : int_Index]
	str_Word2 = str_Word[int_Index+len(str_const_GLUE):]
	return [str_Word1,str_Word2]
def word_tokenizer(line):
	blankset = '\n\r\b\t\f\v '
	token = []
	word = ""
	for char_i in line:
		if char_i.isalpha() or char_i.isdigit():
			word = word + char_i
			continue
		if char_i in blankset:
			if word != "" :
				token.append(word)
				word = ""
			continue
		if word != "":
			token.append(word)
			word = ""
		token.append(char_i)
	return token
def f_getASCII(str_Word):
	int_Index = ord(str_Word[0])
	return int_Index