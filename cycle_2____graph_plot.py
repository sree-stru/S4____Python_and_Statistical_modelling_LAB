import matplotlib.pyplot as plt
import numpy as np


print("Menu.")
print("1. f(x) = 2x")
print("2. f(x) = x^2")
print("3. f(x) = √x")
print("4. f(x) = e^x")
print("5. Exit")

while True:
   choice = int(input("Enter your choice:\n"))

   if (choice==1) :
      
      x= np.linspace(-10, 10 , 400 )
      y = 2*x
      plt.plot ( x , y , label="f(x) = 2x")
      plt.title('Plot of f(x)=2x')
      plt.ylim(-100 ,100)

   elif(choice ==2 ) :
     
      x= np.linspace(-10 , 10 , 400 )
      y = x**2
      plt.plot ( x , y , label = "f(x)=x^2")
      plt.title('Plot of f(x)=x^2')
      plt.ylim(-100, 100)
      

   elif( choice ==3 ):
     
      x= np.linspace(0 , 10 , 400 )
      y = np.sqrt(x)
      plt.plot ( x , y , label = "f(x)=√x")
      plt.title('Plot of sqrt x')
      plt.ylim(0,10)

  
   elif( choice ==4 ):
     
      x= np.linspace(-10 , 10 , 400 )
      y = np.exp(x)
      plt.plot ( x , y , label = "f(x)=e^x")
      plt.title('Plot of f(x) = e^x')
      plt.ylim(-100,100)
      
   elif (choice == 5):
        
        print("Exit.")
        break

   else:
        
        print("Invalid choice. Try again.")
        continue

   plt.xlabel('x')
   plt.ylabel('f(x)')
   plt.grid(True)
   plt.legend()
   plt.show()

