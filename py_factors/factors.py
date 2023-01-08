class Factors:
    def __init__(self):
        self.unorderedFactors=[]
        self.orderedFactors=[]

    def unordered_factors(self, number):
        for num in range(1, int(number**0.5)+1):
            if number %num==0:
                    self.unorderedFactors.append(num)
                    if number//num != self.unorderedFactors[-1]:
                        self.unorderedFactors.append(number//num)
                    else:
                        return self.unorderedFactors
        return self.unorderedFactors

    def ordered_factors(self, number):
        right=[]  #numbers that represent number/factor

        for num in range(1, int(number**0.5)+1):
            if number %num==0:
                    self.orderedFactors.append(num)
                    if number//num != self.orderedFactors[-1]:
                        right.append(number//num)
                    else:
                        break

        #append the numbers in right to ordered list
        while right!=[]:
            self.orderedFactors.append(right.pop())
        return self.orderedFactors





