# Imperial to Metric
x = eval(input("Enter length in meters"))

def I(x):
    i = (100)*(x)*(1/2.54)
    return i

def F(x):
    f=I(x)/12
    return f

def Y(x):
    y=F(x)/3
    return y

def M(x):
    m=Y(x)/1760
    return m

print ("Length in {} in, {} ft, {} yds, {} miles.".format(I(x),F(x),Y(x),M(x)))