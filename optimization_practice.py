# This is a easy python code to just practice the use of Scipy optimization

from scipy.optimize import minimize

def objective(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return x1*x4*(x1 + x2 + x3) + x3
def constraint1(x):
    return x[0]*x[1]*x[2]*x[3] - 25.0
def constraint2(x):
    sum_eq = 40
    for i in range(4):
        sum_eq -= x[i]**2
    return sum_eq


x0 = [1,5,5,1]
bd = (1.0,5.0)
bnds = (bd,bd,bd,bd)
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'eq', 'fun': constraint2}
cons = [con1, con2]
sol = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)


def objective2(x):
    return x**4 - 2*x**2 -3

x_i = 1
newsol = minimize(objective2, x_i, method='SLSQP')

print(newsol)
