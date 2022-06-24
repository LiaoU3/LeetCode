from pathlib import Path
import pathlib
import os
path = str(pathlib.Path(__file__).parent.parent) + '\\Problems\\'

name = input("Please input the title name : ")
programing_language = input("Enter the programing language (py(default), c(0), cpp(1) etc.) : ")
programing_language = programing_language if programing_language else 'py'

name_split_list = name.split('.')
num = name_split_list[0]
alpha = name_split_list[1].replace(' ', '_')
programing_language_dict = {'0': 'c', '1': 'cpp'}
if programing_language in programing_language_dict:
    filename = num + alpha + '.' + programing_language_dict[programing_language]
else:
    filename = num + alpha + '.' + programing_language

myfile = Path(path + filename)
if os.path.isfile(path + filename):
    print('File is already exist')
else:
    print('Created : ' + path + filename)
    myfile.touch()