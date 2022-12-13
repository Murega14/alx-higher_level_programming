#1/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    new_tup = ()
    for x in range(2):
        if x >= len_a:
            a = 0
        else:
            a = tuple_a[x]
        if x >= len_b:
            b = 0
        else:
            b = tuple_b[x]

        if (x == 0):
            new_tup =  (a + b)
        else:
            new_tup = (new_tup, a + b)

    return(new_tup)
