class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      
        
        cars=sorted(zip(position, speed), reverse=True)
        fleet=0
        Current_time=0
        for p,s in cars:
            time=(target-p)/s
            if time>Current_time:
                fleet+=1
                Current_time=time
        return fleet




        