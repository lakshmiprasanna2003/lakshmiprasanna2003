R = 3
C = 3
def printUtil(arr, m, n, output):
    output[m] = arr[m][n]
    if m==R-1:
        for i in range(R):
            print (output[i],end= " ")
        print()
        return
    for i in range(C):
        if arr[m+1][i] != "":
            printUtil(arr, m+1, i, output)
def printf(arr):
    output = [""] * R
    for i in range(C):
        if arr[0][i] != "":
            printUtil(arr, 0, i, output)
arr = [ ["I", "You",""],
        ["Play", "Love",""],
        ["Cricet", "Ludo",""]]
printf(arr)





output
    I Play Cricket
    I Play Ludo
    I Love Cricket
    I Love Ludo
    You Play Cricket
    You Play Ludo
    You Love Cricket
    You Love Ludo
