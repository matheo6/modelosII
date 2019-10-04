##presentado por
##Luis Miguel castellanos
##Edwin
##Mateo Bohorquez

##def pot(m,n):
##    if(n==0):
##        return 1
##    if(n==1):
##        return m
##    return pot(m,n-1)*m
##print(pot(3,3))

##def fibo(n):
##    if(n<=2):
##        return 1
##    return fibo(n-1)+fibo(n-2)
##print(fibo(6))

##def div(m,n):
##    if(n==0):
##        return 0
##    if(m<n):
##        return 0
##    return div(m-n,n)+1
##print(div(60,2))

##potencia iterativo
##y=int(input('ingrese el numero '))
##x=int(input('ingrese el exponente '))
##resultado=y
##for i in range(x):
##    resultado= resultado+y
##print(resultado)

##fibonachy
##inicial=1
##inicial2=1
##resultado= inicial
##fibonach=int(input('ingrese el numero de fibonacci que desea calcular '))
##for i in range(fibonach-2):
##    resultado=inicial+inicial2
##    inicial=inicial2
##    inicial2=resultado
##print(resultado)

##Division
y=int(input('ingrese el numero '))
x=int(input('ingrese el divisor '))
resultado=0
while(y>=x & x!=0):
    resultado= resultado+1
    y=y-x
print(resultado)

