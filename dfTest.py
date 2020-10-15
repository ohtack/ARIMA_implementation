#Results of Dickey-Fuller Test

def dfTest(data):
    from statsmodels.tsa import stattools
    adfuller = stattools.adfuller(data)
    print('ADF Statistic: {}'.format(adfuller[0]))
    print('p-value: {}'.format(adfuller[1]))
    print('Critical Values:')
    for key, value in adfuller[4].items():
        print('{}: {}'.format(key, value))

# Dickey-Fuller Test returns the following
# Test Statistic
# p-value
# #Lags Used
# Number of Observations Used
# Critical Value (1%)
# Critical Value (5%)
# Critical Value (10%)