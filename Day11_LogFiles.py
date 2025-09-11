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
    filename="basic.log"
)
logging.debug("this is a debug message: ")
logging.error("this is an info message; ")
logging.warning("This is a warning message; ")
logging.error("this is an error message; ")
logging.critical("this is a critical message; ")