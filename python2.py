from pathlib import Path
import os
# 1 creating folder
def createfolder():
    readfileandfolder()
    name=input("please tell the name of your folder :-")
    path=Path(name)
    if path.exists():
        print(f"xxxxxxxx {name} is already Exist plz enter another name of folder xxxxxxxxxxx")
    else:    
        path.mkdir()
        print("~~~~~~~~~~~~Sucessfully Done~~~~~~~~~~~~~")
#2
def readfileandfolder():
    path=Path("")
    folders= list(path.rglob("*"))
    
    # for i in folders:
    #     print(i)
    print("NAME OF ALL EXISTING FOLDER ")
    for i,v in enumerate(folders):
        print(f"{i}:{v}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")   
#3 This function use to update the old folder name
def updatefoldername():
        oldname=input("plz tell old file name :-")
        path = Path(oldname)
        if path.exists():
            path.rename(input("tell your new folder name :-"))
            print("~~~~~~~~~~~~Done~~~~~~~~~~~~~~~") 
        else:
            print("~~~~~~~~~~~~~~~file dosent exist~~~~~~~~~~~~~~~")           
#4 for Deleating the file 
def deletefolder():
    foldername = input("plese tell me the existing folder name that you want to delete :- ")
    path = Path(foldername)
    if path.exists():
        path.rmdir()
        print("~~~~~~~~~~~~Sucessfully Done~~~~~~~~~~~~~")
    else:
        print(f"xxxxxxxxxxxxxxx {foldername} file dosent exist xxxxxxxxxxxxxx\nplz enter correct file name")  

#5 This function is use to create a file.
def createfile():
    filepath = Path(input("plz Enter the file name:-"))
    if filepath.exists():
        print(f"The file {filepath} already exists.")
    else:
        with open(filepath,"w")as fs:
                    data=input("write your content that you want to store in file \n:--")
                    fs.write(data) 
            
        print(f"The file {filepath} has been successfully created.")    
#6 This function use to update file name, file content, add new file 
def updatingfile():
    filepath = Path(input("plz Enter the file name :-"))
    if filepath.exists():
        print("press 1 if u want to rename u file ")
        print("press 2 if u want to udate file content ")
        print("press 3 if u want to rewrite your  file")
        j=(input("plz tell your new name"))
        if j=="1":
            newname= input("tell your new name of your file")
            p=Path(newname)
            if not p.exists():
                os.rename(filepath,p)
                print("Sucessfully ")
            else:
                print("alredy ready name exist")
        if j=='2':
            with open(filepath,'a') as fs:
                data=input("please tell your data")
                fs.write(" "+data)
        if j == "3":
            with open(filepath,'w'):
                data=input("Provide your data/n:--")
    else:
        print(f"xxxxxxxx {filepath} file dosent exist xxxxxxxxx\nplz enter correct file name")


# 7 for delete file 
def deletingfile():
    nameoffolder=input("plz enter the file name that u want to delete :-- ")
    path=Path(nameoffolder)
    if path.exists():
        os.remove(path)
    else:
        print(f"xxxxxxxxx {nameoffolder} file dosent exist xxxxxxxx\nplz enter correct file name")    


while True:
    print("\n")
    print("Ther are some option you have to select any one ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Press 1 for creating folder ")
    print("Press 2 for readding a  folder ")
    print("press 3 udateting a folder ")
    print("press 4 deleating folder ")
    print("Press 5 for creating file ")
    print("Press 6 for updating file ")
    print("press 7 for deleting file ")
    print("press 8 for  exit")
    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
    n= input("what do u want to do :- ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
    if n== "1":
        createfolder()
    if n=="2":
        readfileandfolder()
    if n=="3":
        updatefoldername()
    if n=='4':
        deletefolder()
    if n == "5":
        createfile()    
    if n== "6":
        updatingfile()
    if n =="7":
        deletingfile()
    if n =="8":
        print("Now your are outside of program ")
        exit()



