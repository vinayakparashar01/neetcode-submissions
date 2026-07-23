class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i=0
        k=0
        j=n-1
        while i<m:
            if matrix[i][k]<=target<=matrix[i][j]:
                while k<=j:
                    mid=k+(j-k)//2
                    if matrix[i][mid] == target :
                        return True
                    elif target<matrix[i][mid]:
                        j=mid-1
                    else:
                        k=mid+1
                return False
            else:
                i+=1
                k=0
        return False
        