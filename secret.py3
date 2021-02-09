import os
import sys

#fill the path of the downloaded folder to know the answer.
#"path to the file"
path = r" "




def rename_files():
	file_list = os.listdir(path)
	os.chdir(path)

	for file_name in file_list:

		os.rename(file_name , file_name.translate(None, "0123456789"))

		print(file_name)


rename_files()