#Question 1
import datetime as da
print(da.date.today())

#Question 2
import webbrowser
s=input("search video")
webbrowser.open_new_tab('http://youtube.com/search?q=%s'%s)

#Question 3
import os
path = '/Users/samsung/Desktop/python_module'
files = os.listdir(path)
i = 1

for file in files:
    a=input("name of file")
    os.rename(os.path.join(path, file), os.path.join(path, a+'.jpg'))
    i = i+1
