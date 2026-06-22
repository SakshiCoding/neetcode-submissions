class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       #sort the position and speed in descending order keeping the correlated values together
       cars = sorted(zip(position, speed), reverse=True)
       #go through and calculate time to reach target for each car (stack)
       stack = []
       #caclulating the time for each car to reach target
       for position, speed in cars:
            t = (target - position) / speed
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

       return len(stack)
       



        
        