def isPalindrome( x):
  # x1=str(x)
  return (True if str(x)==str(x)[::-1] else False)

print(isPalindrome(12321))