def f(x):
    return x**3 - x - 2

def secant_method (x0, x1, tol=1e-5,max_itr=100 ):

    for i in range (max_itr):
        x= x1 - (f(x1)*(x1 - x0))/(f(x1) - f(x0))

        if( abs(f(x)) < tol):
            return x

        x0=x1
        x1=x

    return x

secant_root=secant_method(1,2)
print(f"Root is : {secant_root}")
