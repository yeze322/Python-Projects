
def f_HASH_to_HASH_list(list_AsciiHash): # I'm wondering if this function is necessary
	for int_Index in range(len(list_AsciiHash)):
		for str_Key in list_AsciiHash[int_Index]:
			sortlist = []
			dic = list_AsciiHash[int_Index][str_Key]
			newlist = c_DictSorter(dic).insertsort() #dic 
			for str_Word in newlist:
				sortlist.append(str_Word)
				sortlist.append(dic[str_Word])
			list_AsciiHash[int_Index][str_Key] = sortlist
	return list_AsciiHash

def f_HASH_list_to_file(ASCII_HASH_list,dict_KeyFreq,int_ThreshouldVal = 5):
	str_FileName = 'Markov_HASH.txt'
	fp_File = open(str_FileName,'w')
	dic = f_KeyFreq_Filter(dict_KeyFreq,int_ThreshouldVal)
	for str_Key in dic:
		int_key_Freq = dict_KeyFreq[str_Key]
		fp_File.write(str_Key+'\t')
		fp_File.write(str(int_key_Freq)+'\t')
		for str_Word in ASCII_HASH_list[ord(str_Key[0])][str_Key]:
			fp_File.write(str(str_Word)+'\t')
		fp_File.write('\n')
	fp_File.close()

def f_HASH_list_to_file_Sorted(HASH_list,dict_KeyFreq,int_ThreshouldVal = 5):
	str_FileName = 'Markov_HASH.txt'
	dict_KeyFreq = f_KeyFreq_Filter(dict_KeyFreq,int_ThreshouldVal)
	#I must del it first
	list_SortedKey_list = c_DictSorter(dict_KeyFreq).qsort()
	fp_File = open(str_FileName,'w')
	for str_Key in list_SortedKey_list:
		int_key_Freq = dict_KeyFreq[str_Key]
		if int_key_Freq < int_ThreshouldVal:
			continue
		fp_File.write(str_Key+'\t'+str(int_key_Freq)+'\t')
		for str_Word in HASH_list[ord(str_Key[0])][str_Key]:
			fp_File.write(str(str_Word)+'\t')
		fp_File.write('\n')
	print len(dict_KeyFreq)
	fp_File.close()


#list_AsciiHash_New = f_HASH_to_HASH_list(list_AsciiHash)
#f_HASH_list_to_file_Sorted(list_AsciiHash_New,dict_KeyFreq,8)
