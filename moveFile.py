import shutil
import os
import shutil

from_dir = "C:/Users/lenovo/Downloads"
to_dir = "C:/Users/lenovo/OneDrive/Desktop/sample doc"
list = os.listdir(from_dir)
print(list)

for i in list:
    name,exe = os.path.splitext(i)
    print("NAME:",name)
    print("EXTENSION:",exe)

    if(exe == ""):
         continue
    elif(exe in [".exe",".txt"]):
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "documents"
        path3 = to_dir + "/" + "documents" + i
        print(path1)
        print(path2)
        print(path3)

if(os.path.exists(path2)):
    print("Moving" + i + ".....")
    shutil.copy(path1,path3)

else:
    os.mkdir(path2)
    print("MOVING" + i + ".....")
    shutil.copy(path1,path3)
    
