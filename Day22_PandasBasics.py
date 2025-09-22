import numpy as np
import pandas as pd

#talking about pandas
#developed in 2008 

#Data structures in pandas
#3 MAIN
#SERIES 1D
#DATAFRAME 2D
#PANEL 3D

#SERIES 1D
def series():
    #in series creation, best used for
    #1.ndarray
    #2.python dictionary
    #3.scalar values

    #1.ndarry
    def ndarray():
        ser=pd.Series(np.random.randn(4))
        print(ser)

        #an index can be used as a string object
        import calendar as cal
        MonthName=[cal.month_name[i] for i in np.arange(1,6)]
        months=pd.Series(np.arange(1,6),index=MonthName)
        print(months)

        print(months.index)
    ndarray()
    
    #2.python dictinary
    #key value pair
    def python_dictionary():
        curr_dict={"US":"dolla","UK":"pound","GERMANY":"euro","MEXICO":"peso","NIGERIA":"naira","CHINA":"yuan","JAPAN":"yen"}
        curr_series=pd.Series(curr_dict)
        print(curr_series)
    python_dictionary()

    #3.scalar values
    def scalarValues():
        #an index must be provided and value repeated as many times as the index value
        dogseries=pd.Series('Chihuahua',index=['bread','countryOfOrigin','name','gender'])
        print(dogseries)
    scalarValues()
series()