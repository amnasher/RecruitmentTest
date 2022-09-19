# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

myList = []
class Solution:
    def removeNthFromEnd(self,head, n):
      
        head.pop(-n)
        return head


print('Note:Please do not enter numbers greater than 100 and the elements should not be more than 30')

# take number from user, how many element in list
n_elements = int (input ("How many elements in list :- "))

if n_elements > 30 or n_elements <= 0:
    print('The size of list is Incorrect please input again')
    n_elements = int (input ("How many elements in list :- "))

# append element into list using list.append
for i in range (n_elements) :
    storeElement = int (input ("Enter an integer node :- "))
    if storeElement > 100 or storeElement < 0:

        print('Numbers greater than 100 and less than 0 are not acceptable. Please enter an integer num again:-')
        storeElement = int (input ("Enter an integer node :- "))
    myList.append (storeElement)

print('Input head =',myList)

n = int(input ("Please enter the nth node to remove from the end of the list :- "))

if n > n_elements or n < 1 :
    print('Incorrect input. The nth node cannot be greater than the size of list and cannot be less than 1')
    n = input ("Please enter the nth node to remove from the end of the list :- ")


Solution = Solution()
head = Solution.removeNthFromEnd(myList,n)

print('After Deletion:')
print(head)
