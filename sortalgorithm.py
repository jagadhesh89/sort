class SortAlgorithm:
    def __init__(self):
        pass
        
    def BubblesSort(self,InputArray):
        self.InputArray = InputArray
        self.GreaterConditionMet = 0
        for i in range(0,len(self.InputArray)-1):
            if self.InputArray[i] > self.InputArray[i+1]:
                NextElement = self.InputArray[i+1]
                CurElement = self.InputArray[i]
                self.InputArray[i+1] = CurElement
                self.InputArray[i] = NextElement
                self.GreaterConditionMet = 1

        print(self.InputArray)       
        if self.GreaterConditionMet == 1:
            self.BubbleSort(self.InputArray)
        return self.InputArray
        
    def SelectSort(self,InputArray):
        self.InputArray = InputArray
        for i in range(0,len(self.InputArray)):
            self.MinimumVal = 101
            self.MinIndex = 0
            for j in range(i,len(self.InputArray)):
                if self.InputArray[j] < self.MinimumVal:
                    self.MinimumVal = self.InputArray[j]
                    self.MinIndex = j
            CurFirstElement = self.InputArray[i]
            self.InputArray[i] = self.MinimumVal
            self.InputArray[self.MinIndex] = CurFirstElement
            print(self.InputArray)
        return(self.InputArray)
        
