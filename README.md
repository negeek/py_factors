# py_factors
A python package that gives the mathematical factors of a number fast.

## Example
A quick example of methods you can access. 

Each of the functions below have additional ard=gument `ordered` which can take value of `True` or `False`. `True` means give an ordered output while `False` means otherwise. By default it is `True`

``` 
   
    from py_factors import factors, square_factors, even_factors, odd_factors

    # factors of 200
    factor200= factors(200, ordered=False)

    output: [1, 200, 2, 100, 4, 50, 5, 40, 8, 25, 10, 20]
   
    #square factors of 200 i.e factors of 200 that are perfect squares.
    per_fact200= square_factor(200)

    #even factors of 200
    even_fact200=even_factors(200)

    #odd factors of 200
    odd_fact= odd_factors(200)

```

# Note
TIf you want result in faster time set `ordered=False` in the functions.


