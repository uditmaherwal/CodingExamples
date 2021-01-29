import datetime 

def getDay(date): 
    day = datetime.datetime.strptime(date, '%Y %m %d').weekday() 
    return dictConvert[day]
def getDate(value):
    temp = value.split('-')
    return ' '.join(char for char in temp)


dictConvert={0:'Mon',1:'Tue',2:'Wed',3:'Thu',
             4:'Fri',5:'Sat',6:'Sun'}
dictInput = {'2020-01-01':6,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,
             '2020-01-05':2,'2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}
dictOutput = {'Mon':0,'Tue':0,'Wed':0,'Thu':0,'Fri':0,'Sat':0,'Sun':0}

if __name__ == '__main__':
    for key in dictInput.keys():
        days = getDay(getDate(key))
        dictOutput[days] += dictInput[key]
    print(dictOutput)
