def is_inside(a, b):
    xa = a[0]
    ya = a[1]
    xb = b[0]
    yb = b[1]
    w = b[2]
    h = b[3]
    if xa in range(xb,xb+h):
        if ya in range(yb, yb+w):
            return True
        else: return False
    else: return False
    
if is_inside([100,100],[50,50,100,100]) == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
