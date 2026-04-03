class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        
        def climb(currentStep):
            if currentStep in cache:
                return cache[currentStep]
            if currentStep > n:
                return 0
            if currentStep == n:
                return 1
            
            r = climb(currentStep + 1) + climb(currentStep + 2)
            cache[currentStep] = r
            
            return r
        
        return climb(0)