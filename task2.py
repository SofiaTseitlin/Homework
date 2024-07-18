def Euclidean_algorithm(maximum, minimum):
    if minimum != 0:
        number = maximum % minimum
        maximum = max(number, minimum)
        minimum = min(number, minimum)
        return(Euclidean_algorithm(maximum, minimum))
    return(maximum)

a = int(input())
b = int(input())
print(Euclidean_algorithm(max(a, b), min(a, b)))