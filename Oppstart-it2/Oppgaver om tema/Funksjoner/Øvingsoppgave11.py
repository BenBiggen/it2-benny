

def summer_til(n, summen=0):

    if n == 0:
        print(summen)
    else:
        summen += n
        summer_til(n-1, summen)
        

        

"""""
def summer_til(n,startSum = 0):
    startSum+=n
    if n==0:
        return(startSum)
    endelig = summer_til(n-1,startSum)
    return endelig
"""""

summer_til(7)
