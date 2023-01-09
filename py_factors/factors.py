class Factors:
    def __init__(self):
        self.mathFactors=[]
        self.squareFactors=[]
        self.oddFactors=[]
        self.evenFactors=[]

    def __update_factors(self, otherFactorList, mainList):
        while otherFactorList!=[]:
                mainList.append(otherFactorList.pop())
        return mainList


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
    def even_factors(self, number,ordered=True):
        #if number is odd
        if number%2!=0:
            return self.evenFactors
        # if ordered output
        if ordered:
            otherFactors=[]
            for num in range(1, int(number**0.5)+1):
                if number %num==0:
                    #if it is even
                    if num%2==0:
                        self.evenFactors.append(num)
 
                        #check if the other factor is even
                        if number//num != self.evenFactors[-1] and (number//num)%2==0:
                            otherFactors.append(number//num)
                    #check if other factor is even
                    else:
                        try:
                            if number//num != self.evenFactors[-1] and (number//num)%2==0:
                                otherFactors.append(number//num)
                        except IndexError:
                            otherFactors.append(number//num)
            self.evenFactors=self.__update_factors(otherFactors, self.evenFactors)
            return self.evenFactors

        # if unordered output
        else:
            for num in range(1, int(number**0.5)+1):
                if number %num==0:
                    #if it is even
                    if num%2==0:
                        self.evenFactors.append(num)
 
                        #check if the other factor is even
                        if number//num != self.evenFactors[-1] and (number//num)%2==0:
                            self.evenFactors.append(number//num)
                    #check if other factor is even
                    else:
                        try:
                            if number//num != self.evenFactors[-1] and (number//num)%2==0:
                                self.evenFactors.append(number//num)
                        except IndexError:
                            self.evenFactors.append(number//num)
            return self.evenFactors

    def odd_factors(self, number, ordered=True):
        # if ordered output
        if ordered:
            otherFactors=[]
            for num in range(1, int(number**0.5)+1):
                if number %num==0:
                    #if it is even
                    if num%2!=0:
                        self.oddFactors.append(num)
 
                        #check if the other factor is even
                        if number//num != self.oddFactors[-1] and (number//num)%2!=0:
                            otherFactors.append(number//num)
                    #check if other factor is even
                    else:
                        try:
                            if number//num != self.oddFactors[-1] and (number//num)%2!=0:
                                otherFactors.append(number//num)
                        except IndexError:
                            otherFactors.append(number//num)
            self.evenFactors=self.__update_factors(otherFactors, self.oddFactors)
            return self.evenFactors

        # if unordered output
        else:
            for num in range(1, int(number**0.5)+1):
                if number %num==0:
                    #if it is even
                    if num%2!=0:
                        self.oddFactors.append(num)
 
                        #check if the other factor is even
                        if number//num != self.oddFactors[-1] and (number//num)%2==0:
                            self.oddFactors.append(number//num)
                    #check if other factor is even
                    else:
                        try:
                            if number//num != self.oddFactors[-1] and (number//num)%2==0:
                                self.oddFactors.append(number//num)
                        except IndexError:
                            self.oddFactors.append(number//num)
            return self.oddFactors




s=Factors()
print(s.factors(10000, ordered=True))
                    






    










