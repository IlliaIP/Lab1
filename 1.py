import numpy as np

def WALD_meth(mat):
    MIN = mat.min(axis=1)
    return MIN

def MAXIMUM_meth(mat):
    MAX = mat.max(axis=1)
    return MAX

def LAPLACE_meth(mat):
    res = np.sum(mat, axis=1)
    res = np.divide(res, 3)
    return np.round(res, 2)

def HURWITZ_meth(mat):
    y = 0.5
    MAX = MAXIMUM_meth(mat)
    MIN = WALD_meth(mat)
    MIN = np.multiply(MIN, y)
    MAX = np.multiply(MAX, 1 - y)
    res = np.add(MIN, MAX)
    return res

def BAYECE_LAPLACE_meth(mat):
    p = np.array([0.5, 0.35, 0.15])
    res = np.multiply(mat, p)
    res = res.sum(axis=1)
    return res

data = np.loadtxt("1.txt", dtype=int)

value_WALD = WALD_meth(data)
value_MAXIMUM = MAXIMUM_meth(data)
value_LAPLACE = LAPLACE_meth(data)
value_HURWITZ = HURWITZ_meth(data)
value_BAYECE_LAPLACE = BAYECE_LAPLACE_meth(data)

print("  Matrix   |\tWald|    Max | Laplace|\tHurwitz| Bayece-Laplace\t")
print("----------------------------------------------------------")
for i in range(len(value_WALD)):
    print(*data[i], sep='\t', end =" "),
    print("|  %3.2f |\t %3d | \t%3.2f |\t %3.2f |\t %3.2f" 
          %(value_WALD[i], value_MAXIMUM[i],value_LAPLACE[i], 
            value_HURWITZ[i], value_BAYECE_LAPLACE[i]))
print("----------------------------------------------------------")
print("  Max:\t   |  %3.2f |\t %3d |   %3.2f|  %3.2f | \t %3.2f"
      %(max(value_WALD), max(value_MAXIMUM), max(value_LAPLACE), max(value_HURWITZ),
        max(value_BAYECE_LAPLACE)))
