import numpy as np

list = [1,2,3,4,5]
list2 = [5,5,5,55,5]
list3 = [5,4,4,5,5]
x = np.array(list)
y = np.array([list,list2])
##print(y)


z = np.array([list,list2,list3])
##print(z[1:,2:])


a = np.linspace(0,24,num=25).reshape(5,5)
a

b = a[2:4,1:4]
print(b)
a[a>12]

tfl_18=np.loadtxt('tfl-daily-cycle-hires-2018.csv',usecols=1, skiprows=1, delimiter=',')
tfl_19 = np.loadtxt('tfl-daily-cycle-hires-2019.csv',usecols=1, skiprows=1, delimiter=',')
tfl_1819=np.concatenate([tfl_18,tfl_19], axis=1)
np.sum(tfl_1819,axis=0)
np.mean(tfl_1819,axis=0)
np.max(tfl_1819,axis=0)
