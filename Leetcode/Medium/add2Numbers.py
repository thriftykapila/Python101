
def addTwoNumbers( l1, l2):
  r1 = l1[::-1]
  r2 = l2[::-1]
  diff = (len(r1)-len(r2))
  if diff > 0:
    print("Shorter List",r2)
    for i in range(diff):
      r2.insert(0,0)
    print("adding these 2 lists",r1,r2)
  elif diff<0:
    print("Shorter List",r1)
    for i in range(abs(diff)):
      r1.insert(0,0)
    print("adding these 2 lists",r1,r2)
  res = [r1[i] + r2[i] for i in range(len(r1))]
  print("addition without carry ",res)
  #start i from i+1
  
  for i in range(1,len(res)):
    if res[i]>9:
      res1 = int(res[i]/10)
      res[i]=res[i]%10
      res[i-1]+=res1      
      print(res[i-1],res[i],res1) 
  print("addition with carry ",res) 
  return res[::-1]

# print(addTwoNumbers([2,4,3],[5,6,4]))
print("addition with carry after reversing ",addTwoNumbers([9,9,9,9],[9,9]))



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


# num = 89
# w=num/10                = 8.9
# x=int(num/10)           =  8
# y=num%10                =  9