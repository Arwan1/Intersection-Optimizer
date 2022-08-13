import time
def car_r(x,light,i):
    if (i==0)or(x[i-1]-x[i]>=40):
        if light==("red")and(x[i]==230):
            x[i]+=0
        else:
            x[i]+=1
    else:
        x[i]+=0
    #time.sleep(0.0001)
    return x[i]
    
def car_l(x,light,i):
    if (i==0)or(x[i]-x[i-1]>=40):
        if light==("red")and(x[i]==390):
            x[i]-=0
        else:
            x[i]-=1
    else:
        x[i]-=0
    #time.sleep(0.0001)
    return x[i]

def car_d(y,light,i):
    if (i==0)or(y[i-1]-y[i]>=40):
        if light==("red")and(y[i]==150):
            y[i]-=0
        else:
            y[i]+=1
    else:
        y[i]-=0
    #time.sleep(0.0001)
    return y[i]

def car_u(y,light,i):
    if (i==0)or(y[i]-y[i-1]>=40):
        if light==("red")and(y[i]==310):
            y[i]-=0
        else:
            y[i]-=1
    else:
        y[i]-=0
    #time.sleep(0.0001)
    return y[i]
