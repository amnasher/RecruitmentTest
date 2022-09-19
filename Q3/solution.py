class Solution:

    def findMedianSortedArrays(self,nums1,nums2) :
       
        A,B = nums1,nums2
        total = len(A) +len(B)
        half = total // 2


        if len(A) > len(B):
            A, B = B, A
        

        left,right = 0,len(A)-1

        while True :
            i = (left+right) // 2 # A
            j = half - i -2 # B

            #Left value of A :

            AL = A[i] if i >=0 else float("-infinity")
            print('AL')
            print(AL)
            #Right value of A :
            AR = A[i+1] if (i+1) < len(A) else float('infinity')
            print('AR')
            print(AR)
            BL = B[j] if j >=0 else float("-infinity")
            print('BL')
            print(BL)
            BR =  B[j+1] if j+1 < len(B) else float("infinity")
            print('BR')
            print(BR)
            #partition is correct
            if AL <= BR and BL <= AR:
                # for odd :
                if total % 2 :
                    return(min(AR,BR))

                #for even 
                return (max(AL,BL) + min(AR,BR)) / 2
            # If we are too far on the right, we need to go to left side
            elif AL > BR:
                right = i-1
            # If we are too far on the left, we need to go to right side
            else : 
                left = i + 1


arr1 = [1,2]
arr2 = [3,4]
Solution = Solution()
median = Solution.findMedianSortedArrays(arr1,arr2)
print('Median')
print(median)
