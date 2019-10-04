fibo :: Int->Int
fibo 0 = 0
fibo 1 = 1
fibo n= fibo(n-1)+fibo(n-2)

pot :: Int->Int->Int
pot m 0=1
pot m n=m*(pot m (n-1))

divi:: Float->Float->Float
divi m 0=0
divi m n=(divi (m-n) n)+1