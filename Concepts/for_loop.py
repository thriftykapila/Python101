#coding: utf-8
for fruit in [ "banana", "apple ", "grape" ]:
   print ("Fruit : " + fruit)
print("------------------------------")
for i in range (0,10): #(Includes Zero, DOES NOT INCLUDE 10)
   print ("i = " + str ( i ))
print("------------------------------")
for i in range(0,10):
   print ('Not realized')
   if i == 0:
       break
print ('Realized')