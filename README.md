# py_factors
A python package that gives the mathematical factors of a number fast.

## Example
A quick example. In py_factors you can get your answer in unordered form and ordered form.

``` 
    # for unordered factors 
    from py_factors import factors

    factor200= factors(200, ordered=False)

    output: [1, 200, 2, 100, 4, 50, 5, 40, 8, 25, 10, 20]
   

    #for ordered factors, ordered argument is True by default
    factor200= unordered_factors(200)

    output: [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200]


```


