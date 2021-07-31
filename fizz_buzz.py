# The concept behind FizzBuzz is as follows:

# Write a program that prints the numbers 1-100,
# For each number that is a multiple of 3, print “Fizz” instead of the number
# For each number that is a multiple of 5, print “Buzz” instead of the number
# For each number that is a multiple of both 3 and 5, print “FizzBuzz”
# instead of the number

# create FizzBuzz class
class FizzBuzz:
    # create a function
    def fizz_buzz(self, n):
        """
        param: int
        return : list
        """
        # result container
        result = []
        # for loop
        for i in range(1, n+1):
            # if statements for conditions
            if i % 15==0:
                result.append('Fizz Buzz')
            elif i % 3 ==0:
                result.append('Fizz')
            elif i % 5==0:
                result.append('Buzz')
            else:
                result.append(i)
        # return call
        return result

# instatiate a new object
new = FizzBuzz()
# call the object with print
print(new.fizz_buzz(100))
