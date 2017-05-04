# Formula Student
# Building an interface

# Library needed
import matplotlib.pyplot as plt
import numpy as np 
import datetime as dt 
import matplotlib.dates as mdates
from datetime import datetime


#converting bytes to integer
def bytes_to_int(bytes):
	int.from_bytes(b, byteorder='big', signed=False)


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    

# Variable declaration 
Sensor1 = '222'
Sensor2 = '123'
Sensor3 = '221'
Sensor4 = '242'


# Opening the data for the graph
graph_data = open('log.txt','r').read()
lines = graph_data.split('\n')


# Storing the data of the sensors
Sensors_data1 = []
Sensors_data2=[]
Sensors_data3=[]
Sensors_data4=[]

for line in lines:
        #split_line = line.split('\n')
        #print (split_line)
        if ( Sensor1 in line):
            Sensors_data1.append(line)
            print (type(line))
        elif( Sensor2 in line):
            Sensors_data2.append(line)
        elif( Sensor3 in line):
            Sensors_data3.append(line)
        elif( Sensor4 in line):
            Sensors_data4.append(line)

for line in Sensors_data1:            
      Time,ID,Length_data,Data = np.loadtxt(Sensors_data1,
                                        delimiter = ',',
                                        unpack = True,
                                       converters = {0: bytespdate2num('%H:%M:%S.%f'), 4: bytes_to_int('%ab %cd') })
      
#plt.plot_date(Time, Data1,'-', label='Sensors')
#plt.show

print (Sensors_data1)
print (Sensors_data2)
print (Sensors_data3)
print (Sensors_data4)
