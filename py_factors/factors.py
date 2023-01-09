class Factors:
    def __init__(self):
        self.mathFactors=[]
        self.squareFactors=[]
        self.oddFactors=[]
        self.evenFactors=[]

    def factors(self, number, ordered=True):
        # if ordered output
        if ordered:
            otherFactors=[]  #numbers that represent number/factor

            for num in range(1, int(number**0.5)+1):
                if number %num==0:
                        self.mathFactors.append(num)
                        if number//num != self.mathFactors[-1]:
                            otherFactors.append(number//num)
                        else:
                            break

            # update factors list
            while otherFactors!=[]:
                self.mathFactors.append(otherFactors.pop())
            return self.mathFactors 
        
        # if unordered output
        else:
            for num in range(1, int(number**0.5)+1):
                if number %num==0:
                        self.mathFactors.append(num)
                        if number//num != self.mathFactors[-1]:
                            self.mathFactors.append(number//num)
                        else:
                            return self.mathFactors
            return self.mathFactors


    def square_factors(self, number, ordered=True):
        # if ordered output
        if ordered:
            otherFactors=[]
            for num in range(1, int(number**0.5)+1):
                int_root= int(num**0.5)
                if number %num==0:
                    #if it is a perfect square
                    if num**0.5==int_root:
                        self.squareFactors.append(num)
 
                        #check if the other factor is a perfect square
                        int_root=int((number//num)**0.5)
                        if number//num != self.squareFactors[-1] and (number//num)**0.5==int_root:
                            otherFactors.append(number//num)
                    else:
                        #check if the other factor is a perfect square
                        int_root= int((number//num)**0.5)
                        if number//num != self.squareFactors[-1] and (number//num)**0.5==int_root:
                            otherFactors.append(number//num)
                            
            # update square factors list
            while otherFactors!=[]:
                self.squareFactors.append(otherFactors.pop())
            return self.squareFactors

        # if unorderd output
        else:
            for num in range(1, int(number**0.5)+1):
                int_root= int(num**0.5)
                if number%num==0:
                    # if it is a perfect square
                    if num**0.5==int_root:
                        self.squareFactors.append(num)

                        #check if the other factor is a perfect square
                        int_root= int((number//num)**0.5)
                        if number//num != self.squareFactors[-1] and (number//num)**0.5==int_root:
                            self.squareFactors.append(number//num)
                       
                    else:
                        #check if the other factor is a perfect square
                        int_root= int((number//num)**0.5)
                        if number//num != self.squareFactors[-1] and (number//num)**0.5==int_root:
                            self.squareFactors.append(number//num)
            return self.squareFactors










