import sys
import os
import random
from nltk import ngrams
def immediate_subdirectories (path_to_directory):
	return [name for name in os.listdir(path_to_directory)
			if os.path.isdir(os.path.join(path_to_directory, name))]

path_to_root_directory = sys.argv[1]
variable = immediate_subdirectories (path_to_root_directory)
print(variable)
random.shuffle(variable)
print(variable)
array7 = variable[0:7]
array3 = variable[7:10]
print(array3)
print(array7)


def get_file_data(path_to_file):
	file_object= open(path_to_file, "r")
	file_data = file_object.read()
	return file_data

def get_dir_data(path_to_dir):
	dir_file_list = os.listdir(path_to_dir)
	print(dir_file_list)
	dir_data = ""
	for file_name in dir_file_list:
		path_to_file = os.path.join(path_to_dir, file_name)
		file_data = get_file_data(path_to_file)
		dir_data += file_data
	return dir_data

def get_train_data(array7 = [], *args):
	train_data = ""
	for dir_name in array7:
		path_to_dir = os.path.join(path_to_root_directory, dir_name)
		dir_data = get_dir_data(path_to_dir)
		train_data += dir_data
	return train_data

#print(get_train_data(array7))

file_content=get_train_data(array7)
file_ngrams=[]

for f in ngrams(file_content.split(),5):
        file_ngrams.append(f)

'''
for i in file_ngrams:
	print (i, file_ngrams.count(i))
'''

dictionary={}
for i in file_ngrams:
	dictionary[i]=file_ngrams.count(i)
#print (dictionary)

Sorted_List = sorted(dictionary, key=dictionary.__getitem__, reverse =True)

for x in Sorted_List:
	print (x,file_ngrams.count(x))

for x in range(0,int(0.7*len(Sorted_List)),1):
	Sorted_List.pop()
print("\n")
for x in Sorted_List:
	print (x,file_ngrams.count(x))


Writing_file_Reference=open("Kotta_Text_File.txt","w")

Writing_file_Reference.write("\n".join(map(lambda x: str(x),Sorted_List)))
	
#print (SortedDictionary)
'''
Length_Dictionary = len(SortedDictionary)

while (len(dictionary) > 0.3*Length_Dictionary):
	del 
	'''


file_content_test= get_train_data(array3)
test_ngrams=[]
for f in ngrams(file_content_test.split(),5):
    test_ngrams.append(f)
test_ngrams_string=[]
for f in test_ngrams:
	test_ngrams_string.append(str(f))
with open("Kotta_Text_File.txt") as Reading_Reference:
	Read_Content = Reading_Reference.readlines()

Read_Content = [Element.rstrip('\n') for Element in Read_Content]
Read_Content_String= [str(Element) for Element in Read_Content]
#Read_Content = tuple(open("Kotta_Text_File.txt",'r'))
for f in Read_Content_String:
	print (f, test_ngrams_string.count(f))
