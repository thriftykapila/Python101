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
  
  #traverse the res list in reverese and propogate the carry to the digit on the left 
  res1 = 0
  for i in range(len(res)-1,0,-1):
    if res[i]>9:
      res1 = int(res[i]/10)
      res[i]=res[i]%10
      res[i-1]+=res1      
      print(res[i-1],res[i],res1)

  if(res[0]>9):
    res.insert(0,res[0]//10)
    res[1] = res[1]%10
  print("addition with carry ",res) 
  return res[::-1]

# print(addTwoNumbers([2,4,3],[5,6,4]))
print("addition with carry after reversing ",addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))


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


'''
Alternate Solution by @SowmyaaRamesh

'''
'''
def addTwoNumbers(l1,l2):

  carry = 0
  sum = []

  if(len(l1)<len(l2)): # to find which of the two lists is smaller, so that you could pad the rest of the places with 0
    smaller_num = l1
  else:
    smaller_num = l2
  
  for i in range(abs(len(l1)-len(l2))): #padding with 0 to match the length of bigger list
    smaller_num.append(0)
    
  #reversing the two lists since the input is the reversed number
  l1 = l1[::-1] 
  l2 = l2[::-1]

  for i in range(len(l1)-1, -1, -1):
    s = l1[i] + l2[i] + carry
    carry = 0
    if(s > 9): #if it's a two digit number then the Most significant digit should be the carry
      sum.append(s%10)
      carry = s//10
    else:
      sum.append(s)
  if(carry > 0): # carry of the most significant digits should be appended as such
    sum.append(carry)
  return sum

print(addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))

'''