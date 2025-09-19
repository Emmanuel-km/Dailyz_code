#working with solar data 
#opening csv files cleaning, computing monthly average over 
#the past 30 years monthly
#summerizing the data

#opening csv files
#csv files are commer separated values

#so first;

import csv
with open('vim.csv','+w',newline='') as file:
    spamwriter = csv.writer(file, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])