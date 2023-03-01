X, Y = 1600, 1200
def firstAndLast(imgArray):
    res = [0,0]
    for i in range(X):
        for j in range(Y):
            if imgArray[i][j]:
                if not res[0]: res[0] = (i, j)
                else: res[1] = (i, j)
    return res

def center_point(imgArray):
    res= firstAndLast(imgArray)
    mid_point= [(res[0][0]+res[1][0])/2,(res[0][1]+res[1][1])/2]
    return mid_point