def createlog():
    #creating a logging files
    #logging is tracking events that happens when a program runs
    #first importing the loggin module
    import logging
    #setting up the the logging
    #basic logging example
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        filename="basic.log")
    logging.debug("this is a debug message: ")
    logging.error("this is an info message; ")
    logging.warning("This is a warning message; ")
    logging.error("this is an error message; ")
    logging.critical("this is a critical message; ")
#createlog()
def counting_logs():
    #now we will combine file handling... 
    #to count the number of logs: 
    #practicing exception handling:
    try:
        with open('basic.log','r+') as file:
            #storing the logs in list
            bim=file.readlines()
            #initilizing count for critical logs
            countForCritical=0
            #running for loops to count
            for i in bim:
                #checking the critical using boolean
                MING='CRITICAL' in i
                #setting the counter to read only critical logs
                if MING==True:
                    countForCritical+=1
            #printing out the critical logs 
            print(f"CRITICAL logs have appered {countForCritical} number of times")
            #SENT AN INTENTIONAL ERROR TO THE BASIC LOG
            #AT 21.23 AN ERROR
            #print(1+"TI")
    except:
        import logging
        logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        filename="basic.log")
        logging.error("an error has occured")
        
counting_logs()