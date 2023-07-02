def factorial(n):
    assert n>=0 and int(n)==n, 'Please enter an iteger'
    if n in [0,1]:
        return 1

    else:
        return n*factorial(n-1)
        