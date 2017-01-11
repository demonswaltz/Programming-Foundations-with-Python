import os


def rename_files():
	#get names of files in a folder
	file_list = os.listdir("/home/knits4/Udacity/Programming Foundations With Python/prank")
	print file_list
	saved_path = os.getcwd()
	os.chdir("/home/knits4/Udacity/Programming Foundations With Python/prank")
	#rename the files
	for file_name in file_list:
		os.rename (file_name, file_name.translate(None, "1234567890"))
	os.chdir(saved_path)
		

rename_files()
