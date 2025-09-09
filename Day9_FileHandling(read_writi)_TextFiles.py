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
    