# A recursive method
i=1
n=25;
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
for i in range(n + 1):
      if(i==0):
          continue;
      else:  
        print(fib(i+1),'/',fib(i),'==',fib(i+1)/fib(i))
