class Factors:
    def __init__(self):
        self.mathFactors=[]
        self.squareFactors=[]
        self.oddFactors=[]
        self.evenFactors=[]

    def __order_factors(self, otherFactorList, mainList):
        ''' sorts the two lists so that'''
        while otherFactorList!=[]:
                mainList.append(otherFactorList.pop())
        return mainList


    def math_factors(self, number, ordered=False):
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

            # order the factors
            self.mathFactors=self.__order_factors(otherFactors, self.mathFactors)
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


    def square_factors(self, number, ordered=False):
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
                            
            #  order the factors
            self.squareFactors=self.__order_factors(otherFactors, self.squareFactors)
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

    def even_factors(self, number,ordered=False):
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

            # order the factors
            self.evenFactors=self.__order_factors(otherFactors, self.evenFactors)
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

    def odd_factors(self, number, ordered=False):
        # if ordered output
        if ordered:
            otherFactors=[]
            for num in range(1, int(number**0.5)+1):
                if number %num==0:
                    #if it is odd
                    if num%2!=0:
                        self.oddFactors.append(num)

                        #check if the other factor is odd
                        if number//num != self.oddFactors[-1] and (number//num)%2!=0:
                            otherFactors.append(number//num)

                    #check if other factor is odd
                    else: 
                        if number//num != self.oddFactors[-1] and (number//num)%2!=0:
                            otherFactors.append(number//num)
                        

            # order the factors
            self.oddFactors=self.__order_factors(otherFactors, self.oddFactors)
            return self.oddFactors

        # if unordered output
        else:
            for num in range(1, int(number**0.5)+1):
                if number %num==0:
                    #if it is odd
                    if num%2!=0:
                        self.oddFactors.append(num)
 
                        #check if the other factor is even
                        if number//num != self.oddFactors[-1] and (number//num)%2!=0:
                            self.oddFactors.append(number//num)
                    #check if other factor is even
                    else:
                        if number//num != self.oddFactors[-1] and (number//num)%2!=0:
                            self.oddFactors.append(number//num)
                      
            return self.oddFactors
    
    def prime_factors(self,number):
        #next function
        pass


                    






    










