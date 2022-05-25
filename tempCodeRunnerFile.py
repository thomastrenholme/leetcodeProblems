

#given a num return all primes lower than that

def primes(x):
    arr = [True]*x

    for i in range(2, x):

        if arr[i] == True:
            print(i)
            
            curr=i**2
            
            while curr<x:
                arr[curr]=False
                curr+=i

    return arr

print(primes(50))