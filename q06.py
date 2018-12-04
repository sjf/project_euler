#!/usr/bin/env python3

N=100
sum_of_sqs = sum([i**2 for i in range(N+1)])
sq_of_sum = pow(sum([i for i in range(N+1)]),2)
print(abs(sum_of_sqs - sq_of_sum))