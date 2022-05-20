from pathlib import Path
name = input("Please input the title name : ")
programing_language = input("Enter the programing language (py(default), c, cpp etc.) : ")
programing_language = programing_language if programing_language else 'py'

name_split_list = name.split('.')
num = name_split_list[0]
alpha = name_split_list[1].replace(' ', '_')
filename = num + alpha + '.' + programing_language

# you can change the path as you want 
path = 'C:/Users/vincent_liao/Desktop/github/LeetCode/Problems/'
myfile = Path(path + filename)
myfile.touch(exist_ok=True)