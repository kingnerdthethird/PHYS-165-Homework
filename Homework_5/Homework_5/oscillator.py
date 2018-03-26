def G(y, t):
    dy = [0, 0]
    dy[0] = y[1]
    dy[1] = -(w**2)*y[0]
    return dy