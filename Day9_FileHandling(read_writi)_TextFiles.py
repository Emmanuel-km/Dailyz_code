#opening files and reading files
#exprienced some errors at first
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d 
#in position 608: character maps to <undefined>
#fixed by this command
#Get-Content file.txt | Out-File -FilePath file_utf8.txt -Encoding utf8
def readfiles():
    me=open('story.txt','r')
    print(me.readlines())
#readfiles
def filepointer():
    #opening files with with
    with open('sample.txt','r') as file:
        #so seek goes the character then completes the rest of file in a complete 
        file.seek(62)
        #storing the data in a variable
        data=file.read()
        #printing the output
        print(data)
#filepointer()
def openFile():
    #using with as normal
    #so what happens with the 'w' arguments is that it overwrites the text
    #and if there is no text it creates a new file
    with open('sample2.txt','w') as file:
        #so writing a new line we use the \n for next line
        file.write("this is a new block of code\n this is a new line of text")
        #going to the next line
#openFile()
def AddingContent():
    #without overwriting the the existing file contents
    # the append arguments can be used
    with open('sample2.txt','a') as file:
        #wring a new line below
        file.write("\nThankyou for being part of the journey")
#AddingContent()
def writingMultiple():
    #to write mutiple lines 
    #to be more effective we will store in a list
    #the user will input names of renewable energy sources examples
    #separed by , then split and save the contents in sample2.txt
    user_input=input("input types types of renewable energy sources separated by commers: ")
    listReenSources=user_input.split(',')
    #saving the list to the text file
    for i in listReenSources:
        with open('sample2.txt','a') as file:
            file.writelines(f"\n{i}")
#writingMultiple()

#handling files with try block to handle exceptions
def handlingFiles():
    try:
        with open('file_utf.txt','r') as file:
            #intentionally making an error by opening 
            #empty files
            line=file.readline()
            print(line)
    #catching all errors
    except:
        print("enter correct details in the code") 
    else:
        print("the file had no errors at all")
    finally:
        print("the file has being handled")  
handlingFiles() 