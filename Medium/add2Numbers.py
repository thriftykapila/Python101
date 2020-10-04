# num = 89
# w=num/10                = 8.9
# x=int(num/10)           =  8
# y=num%10                =  9

def addTwoNumbers( l1, l2):
  r1 = l1[::-1]
  r2 = l2[::-1]
  print(r1,r2)
  res = [r1[i] + r2[i] for i in range(len(r1))]
  print(res)
  #start i from i+1
  
  for i in range(1,len(res)):
    if res[i]>9:
      res1 = int(res[i]/10)
      res[i]=res[i]%10
      res[i-1]+=res1      
      # print(res[i-1],res[i],res1) 
  return res

print(addTwoNumbers([2,4,7],[5,6,4]))



# logic to equalize two list of different lengths before adding

# def add2(l1,l2):
#   diff = (len(l1)-len(l2))
#   if diff > 0:
#     print(l2)
#     for i in range(diff):
#       l2.insert(0,0)
#       print(l2)
#   elif diff<0:
#     print(l1)
#     for i in range(abs(diff)):
#       l1.insert(0,0)
#       print(l1)
  
# add2([1,2,3],[1,2,3,4])