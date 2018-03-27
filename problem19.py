from datetime import *
import math
 
def counters(d1,d2,y0,m0):
    counter = 0
    while(d1 <= d2):
        if(d1.weekday() == 6):
            counter += 1
        if(m0+1 == 13):
            m0 = 1
            y0 += 1
        else:
            m0 += 1
        d1 = date(y0,m0,1)
    return counter
 
def invert_year(yr):
    x = math.ceil((yr-1900)/400)
    yr = yr - (400*x)
    return yr
 
for _ in range(int(input())):
    y0, m0, d0 = map(int, input().strip().split())
    yf, mf, df = map(int, input().strip().split())
    rep = int((yf-y0)/400)
    rem = (yf-y0)%400
 
    if rep > 0:
        if y0 > 9599:
            y0 = invert_year(y0)
        if yf > 9599:
            yf = invert_year(yf)
        d1 = date(y0,m0,d0)
        d2 = date(yf,mf,df)
        c1 = counters(d1,date(y0+399,12,31),y0,m0)*rep
        c2 = counters(date(yf-rem,1,1),d2,yf-rem,1)
    else:
        diff = yf - y0
        if y0 <= 9599:
            d1 = date(y0,m0,d0)
            d2 = date(yf,mf,df)
            c1 = counters(d1,d2,y0,m0)
            c2 = 0
        else:
            y0 = invert_year(y0)
            yf = y0+diff
            d1 = date(y0,m0,d0)
            d2 = date(yf,mf,df)
            c1 = counters(d1,d2,y0,m0)
            c2 = 0
           
    print(c1+c2)