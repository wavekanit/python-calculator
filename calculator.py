class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        # return b - a # false !!
        return a - b # fix !!

    def multiply(self, a, b):
        result = 0
        # for i in range(b+1): # false !!
        if a == 0 or b == 0:
            return result
        elif b < 0: # fix edge case !
            a = -a
            b = -b
        for i in range(b): # fix !!
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        if b == 0: # add edge case !
            return "undefined"
        elif a == 0:
            return result
        # while a > b: # false !
        if a > 0 and b > 0: # case both positive
            while a >= b:
                a = self.subtract(a, b)
                result += 1
        elif a < 0 and b < 0: # case both neg
            a = -a
            b = -b
            while a >= b:
                a = self.subtract(a, b)
                result += 1
        else: # case some val is neg
            if a < 0 and b > 0:
                a = -a
            else:
                b = -b
            while a >= b:
                a = self.subtract(a, b)
                result -= 1
        return result
    
    def modulo(self, a, b):
        neg_result = False # bool for check, if divider is neg result will neg
        if b == 0: # add edge case !
            return "undefined"
        elif a == 0:
            return 0
        if a > 0 and b > 0: # case both positive
            while a >= b:
                a = self.subtract(a, b)
        elif a < 0 and b < 0: # case both neg
            neg_result = True
            a = -a
            b = -b
            while a >= b:
                a = self.subtract(a, b)
        else: # case some val is neg
            if a < 0 and b > 0:
                a = -a
            else:
                neg_result = True
                b = -b
            while a >= b:
                a = self.subtract(a, b)
        if neg_result == True:
            return -a
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(-3, 1))
    print("Example: multiplication: ", calc.multiply(-3, -4))
    print("Example: division: ", calc.divide(0, 0))
    print("Example: modulo: ", calc.modulo(1, 0))