class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        1 2 5 7 8 10 12 14
        3 6 11
        """

        """ 
        Sol 1 : Brute force -  
        merge 2 arrays and sort them. Find the median
        O(m+n (log(m+n)))
        """

        """ 
        Sol 2 : since 2 arrays are sorted. Use principle of merging 2 sorted arrays. 
        Reach to the min indexes and find median
        O(m+n)
        """

        """ 
        Sol 3 : since 2 arrays are sorted. Use principle of merging 2 sorted arrays. 
        Reach to the min indexes and find median
        O(log(min(m+n))
        """

        A = nums1
        B = nums2
        if len(B) < len(A):
            A,B = nums2, nums1
        
        l, r = 0, len(A)-1
        tL = len(A) + len(B)
        hL = tL//2

        while True:
            Am = l + (r-l)//2

            Bm = hL - Am - 2

            Al = A[Am] if Am >= 0 else float("-inf")
            Ar = A[Am+1] if Am +1 < len(A) else float("inf")
            Bl = B[Bm] if Bm >= 0 else float("-inf")
            Br = B[Bm+1] if Bm +1 < len(B) else float("inf")

            if Al <= Br and Ar >= Bl:
                if tL % 2:
                    return min(Ar, Br)
                return (max(Al, Bl)+ min(Ar, Br))/2

            elif Ar < Bl:
                l = Am+1
            else:
                r = Am -1

        # #  check for size A = 0
        # print("here")
        # return B[len(B)//2]
