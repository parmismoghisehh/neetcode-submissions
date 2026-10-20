class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      
        cars=sorted(zip(position,speed), reverse=True)
        fleet=0
        CT=0
        for p,s in cars:
            time=(target-p)/s
            if time>CT:
                fleet+=1
                CT=time
        return fleet

        