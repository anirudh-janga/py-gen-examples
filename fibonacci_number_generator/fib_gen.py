def fib_num_gen(gen_series_till_number):
    """ Generator to generate fibonacii numbers"""

    #generate only for positve integers
    if not isinstance(gen_series_till_number, int)\
        or gen_series_till_number < 0:
            raise TypeError("Invalid input")

    a,b = 0,1
    while a <= gen_series_till_number:
        yield a
        a,b = b,a+b



