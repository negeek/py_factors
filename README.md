# py_factors
A python package that gives the mathematical factors of a number fast.

## Example
A quick example of methods you can access. 

Each of the functions below have additional argument `ordered` which can take value of `True` or `False`. `True` means give an ordered output while `False` means otherwise. By default it is `False`

``` 
   
    from py_factors import Factors

    #initialize the Factor class
    factor_init= Factors()

    # factors of 200
    factor200= factor_init.math_factors(200)
    output: [1, 200, 2, 100, 4, 50, 5, 40, 8, 25, 10, 20]
   
    #square factors of 200 i.e factors of 200 that are perfect squares.
    per_fact200= factor_init.square_factor(200)
    output: [1, 100, 4, 25]

    #even factors of 200
    even_fact200=factor_init.even_factors(200)
    output: [200, 2, 100, 4, 50, 40, 8, 10, 20]

    #odd factors of 200
    odd_fact= factor_init.odd_factors(200)
    output: [1, 5, 25]

```

# Note
 setting `ordered=False` in the functions gives result faster than when `ordered=True`.


