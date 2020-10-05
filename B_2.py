prutor-lang:python
#language used PYTHON
import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 5, 3
import math
r=float(input())   #radius input
d_s=float(input())   #density_solid input
d_f=float(input())   #density_fluid input
a=float(input())   #guess height1 input
b=float(input())   #guess height2 input
s_a=a   #for printing making a copy of a
s_b=b   #for printing making a copy of b
arr_1=[]  #storing mid value
arr_2=[]  #storing error %
arr_3=[]  #storing iteration corresponding to the error%
def funct_cal(h):
 val=(h*h*(3*r-h)*d_f)+(4*r*r*r*(d_s-d_f))
 # on equating weight of fluid displaced  and weight of solid sphere we get val function which when 0 will give h 
 return val
def check(a1,a2):
 if funct_cal(a1)*funct_cal(a2)<0:
  return 1
 else:
  return 0
if check(a,b):
 for i in range(100):#running for maximum 100 iteration or error<0.01%
  mid=(a+b)/2
  if i!=0: #calculating error%
   err=(abs(mid-arr_1[-1])*100)/mid
   arr_3.append(i)
   arr_2.append(err)
  arr_1.append(mid)
  if i!=0 and arr_2[-1]<0.01:
   break
  val=funct_cal(mid)
  if val==0:
   
   break
  if check(a,mid):
   b=mid
  else:
   a=mid
 print("Enter Radius of the Sphere (m) "+str(r))
 print("Enter Density of the Sphere (kg/m3) "+str(d_s))
 print("Enter Density of the Fluid (kg/m3) "+str(d_f))
 print("Enter guess height1 (m): "+str(s_a))
 print("Enter guess height2 (m): "+str(s_b))
 print("Height above water (m) :- "+str(round(arr_1[-1],6)))
 #below is a code for printing error plot
 x,y=arr_3,arr_2
 plt.plot(x,y, 'r.', label = r'$error_percentage$')
 plt.axhline(0, color='k')
 plt.axvline(0, color='k')
 plt.xlabel(r'$x$', fontsize=20)
 plt.ylabel(r'$y$', fontsize=20)
 plt.legend(loc=4)
 plt.tight_layout()
 pl.prutorsaveplot(plt, 'plot2d.pdf')
else:
# If intial guess values produces positive product then they are wrong guess
 print("Wrong guess")
  
  
  


