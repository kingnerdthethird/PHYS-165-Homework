def F(y,t):
    dy = [0, 0]
    dy[0] = y[1]
    dy[1] = -y[0]
    return dy