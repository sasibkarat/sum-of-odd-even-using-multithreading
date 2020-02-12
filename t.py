import threading
lim=int(input("enter limit "))
global s1,s2

def print_esum(lim):
  etot=0
  for n in range(1, lim+1):
    if(n % 2 == 0):        
        etot = etot + n
  print("The Sum of Even Numbers 1 to{0} = {1} ". format(n,etot))
  global s1
  s1=etot

def print_osum(lim):
   otot=0
   for n in range(1, lim+1):
    if(n % 2 != 0):        
        otot = otot + n
   print("The Sum of Odd Numbers til {0} = {1}". format(n,otot))
   global s2
   s2=otot
def print_sum(lim):
  global s
  s=s1+s2
if __name__=="__main__":
    #creating thread
    t1=threading.Thread(target=print_esum,args=(lim,))
    t2=threading.Thread(target=print_osum,args=(lim,))
    t3=threading.Thread(target=print_sum,args=(lim,))
     
    t1.start()
    t2.start()
    t3.start()

    t1.join()  
    t2.join()
    t3.join()
 
    print(s) 
