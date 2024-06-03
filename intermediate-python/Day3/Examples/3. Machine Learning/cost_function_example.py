import numpy

# SSD squares that difference and sums the result.
def sum_of_square_differences(estimate, actual):
    return numpy.sum((estimate - actual)**2)

# SAD converts differences into absolute 
#  and then sums them.
def sum_of_absolute_differences(estimate, actual):
    return numpy.sum(numpy.abs(estimate - actual))

    