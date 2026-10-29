class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            x=stones.pop()
            y=stones.pop()
            z=x-y
            if z>0:
                stones.append(z)
        if stones:
            return stones[0]
        else:
            return 0
        