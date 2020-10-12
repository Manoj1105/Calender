year=int(input("YEAR: "))
date=int(input("DATE:"))
previous_year=year-1
x=previous_year%400
#print(x)
if (x>300):
    x=x%300
    #print (x)
    y=((x//4)+x+1)
    #print(y)
elif (x>200):
    x=x%200
    #print (x)
    y=((x//4)+x+3)
    #print(y)
elif (x>100):
    x=x%100
    #print (x)
    y=((x//4)+x+5)
    #print(y)
else:
    #print (x)
    y=((x//4)+x)
    #print(y)
a=y%7
#print(a)
z=(date+a)%7
#print(z)
months=(int(input("MONTH:")))
month=months-1
#print(month)
if (month==1):
    t=3
    #print(t)
elif (month==2):
    t=3+0
    #print(t)
elif (month==3):
    t=3+0+3
    #print(t)
elif (month==4):
    t=3+0+3+2
    #print(t)
elif (month==5):
    t=3+0+3+2+3
    #print(t)
elif (month==6):
    t=3+0+3+2+3+2
    #print(t)
elif (month==7):
    t=3+0+3+2+3+2+3
    #print(t)
elif (month==8):
    t=3+0+3+2+3+2+3+3
    #print(t)
elif (month==9):
    t=3+0+3+2+3+2+3+3+2
    #print(t)
elif (month==10):
    t=3+0+3+2+3+2+3+3+2+3
    #print(t)
elif (month==11):
    t=3+0+3+2+3+2+3+3+2+3+2
    #print(t)
elif (month==12):
    t=3+0+3+2+3+2+3+3+2+3+2+3
    #print(t)
else:
    t=0
    #print(t)
if((year%4==0)and (month>2)):
    t=t+1
    e=(t+z)%7
    #print(e)
else:
    e=(t+z)%7
    #print(e)
if (e==0):
    print("DAY:SUNDAY")
elif (e==1):
    print("DAY:MONDAY")
elif (e==2):
    print("DAY:TUESDAY")
elif (e==3):
    print("DAY:WEDNESDAY")
elif (e==4):
    print("DAY:THURSDAY")
elif (e==5):
    print("DAY:FRIDAY")
else:
    print("DAY:SATURDAY")
    