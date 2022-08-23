def calcArea(a, b, c):
    return abs((a.real * (b.imag - c.imag) + b.real * (c.imag - a.imag) + c.real * (a.imag - b.imag)) / 2)

def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    a = complex(x1, y1)
    b = complex(x2, y2)
    c = complex(x3, y3)
    p = complex(xp, yp)
    q = complex(xq, yq)
    
    ab = abs(a - b)
    bc = abs(b - c)
    ca = abs(c - a)
    
    if not ((ab + bc > ca) and (bc + ca > ab) and (ca + ab > bc)):
        return 0

    belongs = []
    for point in [p, q]:
        belongs.append(calcArea(a, b, point) + calcArea(b, c, point) + calcArea(c, a, point) == calcArea(a, b, c))
    
    if belongs[0] and belongs[1]:
        return 3
    
    if belongs[0]:
        return 1
    
    if belongs[1]:
        return 2
    
    return 4

print(pointsBelong(2, 2, 7, 2, 5, 4, 4, 3, 7, 4))    
    
    
    
    
    