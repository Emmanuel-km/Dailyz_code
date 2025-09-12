def RunningSecond():
    #errors associated
    #so in this session the user enters the location of 
    #the log files to be accessed will be handling
    #errors such as file not found error
    #as normal
    try:
        #user inputs the location of the files
        user_filePath=input("enter the location of the file: ")
        with open(user_filePath) as file:
            content=file.readlines()
            #counting the error logs
            count=0
            for i in content:
                MING='ERROR' in i
                if MING==True:
                    count+=1
            print(f"the number of errors are {count}")
    except FileNotFoundError:
        print("file has not be found. please enter location path again")
        RunningSecond()
    except FileExistsError:
        print("file does not exist. PLEASE ENTER A VALID LOG FILE")
        RunningSecond()
    except TypeError:
        print("you entered a wrong data type please enter correct file name and path")
        RunningSecond()
    except ValueError:
        print("ENTER THE FILE NAME PATH")
        RunningSecond()
    except:
        print("you have encountered an error please enter correct path")
        RunningSecond()
RunningSecond()