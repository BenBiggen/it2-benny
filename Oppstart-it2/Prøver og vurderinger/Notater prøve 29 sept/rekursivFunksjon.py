def summer_til(n, summen=0):

    if n == 0:
        print(summen)
    else:
        summen += n
        summer_til(n-1, summen)

summer_til(100)

#Her finner jeg summen av alle tall opp til 8