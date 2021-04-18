# Create a Python project to perform some simple statistics on a list of values.

import statistics
lst = [2, 4, 6, 8, 10, 13, 28, 14, 4, 3]

average_lst = lambda x: statistics.mean(x)
median_lst = lambda x: statistics.median(x)
mode_lst = lambda x: statistics.mode(x)
geometric_mean_lst = lambda x: statistics.geometric_mean(x)
harmonic_mean_lst = lambda x: statistics.harmonic_mean(x)


print(average_lst(lst))
print(median_lst(lst))
print(mode_lst(lst))
print(geometric_mean_lst(lst))
print(harmonic_mean_lst(lst))



