''' 
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
SO we need to find the majority element
'''
#Approach 1

'''
So we could keep the frequency of each occuring element in dictionary and then 
check which element's frequency is greater than n/2.

'''

def majorityElement(self, nums):
        """
        :type nums: List[int] (nums is the input array)
        :rtype: int (return an integer from array)
        """

        dicti = {} # Intiliasing dictionary
        ans = 0 # Intialising answer
        n = len(nums) # length of input array


        for element in nums:
        	# Iterating each element in input array
        	if element in dicti:
        		# if element is present in the dictionary then increment its count
        		dicti[element] += 1
        	else:
        		# If element is not present in dictionary then start by 1 
        		dicti[element] = 1

        for value in dicti:
        	if dicti[value] > n//2:
        		# checking frequency of element greater than n//2
        		ans = value
        		break
        return ans



# Approach 2 
'''
There is another approach in which don't uses dictionary.
It is  based on The Boyer–Moore majority vote algorithm.
In this approach we basically check if the scanned number is same as previous number if so
then we increment the counter.
If number differs then decrement its counter.
if counter becomes zero then checked element is replaced by scanned element
'''


def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = 1 # Initialising frequency
        previous = 0 # Initialising previous
        
        for element in nums:
            if element == previous:
            	# If scanned element iis equal to previous element then increment its frequency.
                freq+=1
            else:
            	# If element differs then decrement its frequency.
                freq-=1
                if freq==0:
                	# If frequency becomes 0 then update with current element.
                    previous = element
                    freq=1
            
        return(previous)
            
''' 
Example : [5,4,3,3,3,3,2]
Freuency = 1
Previous = 0 

Element => 5 , Frequency=>0 (Decrements as not equal to previous) ,Previous => 5 , Frequency=>1
Element => 4 , Frequency=>0 (Decrements as not equal to previous) ,Previous => 4 , Frequency=>1
Element => 3 , Frequency=>0 (Decrements as not equal to previous) ,Previous =>3,Frequency=>1
Element => 3 , Frequency=>2 (Increments as equal to previous)(Increments as equal to previous)
Element => 3 , Frequency=>3 (Increments as equal to previous)
Element => 3 , Frequency=>4 (Increments as equal to previous)
Element => 2 , Frequency=>3 (Decrements as not equal to previous) 

return (previous) => return (3)
which is majority element.