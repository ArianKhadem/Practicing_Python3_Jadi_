import time

def Time_calculator() :
    return time.time()
def Get_input_number() :
    input_number = int(input('Please enter a positive number: '))
    if input_number >= 0 :
        return input_number

def Prime_number_checker(Positive_number) :
    for i in (2, Positive_number) :
        if (Positive_number % i != 0) :
            return '0', 'Prime'
        else:
            return '1', 'Not Prime'
def Print_answer(Result, Boolean, exact_prime_numbers) :
    if Result == '0' :
        Result = True
    else:
        Result = False
    print('The result is', Result, 'and your number is', Boolean,'!!')
    print('It is',exact_prime_numbers,'PRIME number whithin 0 up to your number!')
def Number_of_Primes ( Positive_number ) :
    exact_prime_numbers = 0
    for i in range (1, Positive_number ) :
        Boolean, Text = Prime_number_checker(i)
        Boolean = int(Boolean)
        if Boolean == 1 :
            exact_prime_numbers += Boolean
    return exact_prime_numbers
def Print_time (Start_time, End_time) :
    print('It took ,',End_time-Start_time,'in mili seconds to check your number')

Start_time = Time_calculator()
Positive_number = Get_input_number()
Answer, Boolean = Prime_number_checker (Positive_number)
Exact_prime_numbers = Number_of_Primes(Positive_number)
Print_answer(Answer, Boolean, Exact_prime_numbers)
End_time = Time_calculator()
Print_time(Start_time, End_time)