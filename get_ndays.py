import numpy as np
import calendar

shuffled_yrs = np.array([1970, 1971, 1972, 1973, 1974,
                         1975, 1976, 1977, 1978, 1979,
                         1980, 1981, 1982, 1983, 1984,
                         1985, 1986, 1987, 1988, 1989])


len_shuffled_yrs = 20

odays = 0
for k in range(len_shuffled_yrs):
    yr_to_get = shuffled_yrs[k]
    if calendar.isleap(yr_to_get):
        odays += 366
    else:
        odays += 365

print(odays)
