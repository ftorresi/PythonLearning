from datetime import datetime

def read_file(filename):
    infile = open(filename, 'r')
    infile.readline()  # read column headings
    dates = [];  prices = []
    for line in infile:
        words = line.split(',') #columns separated by comma
        dates.append(words[0])
        prices.append(float(words[-1]))
    infile.close()
    dates.reverse() #reverse lists to get chronological order
    prices.reverse()
    # Convert dates on the form 'YYYY-MM-DD' to date objects
    datefmt = "%Y-%m-%d" #date format
    dates = [datetime.strptime(_date, datefmt).date()
             for _date in dates] #Convert to date objects
    prices = np.array(prices)
    return dates[1:], prices[1:]

dates = {}   #dict with {company:[dates]}
prices = {}  #dict with {company:[prices]}
import glob, numpy as np
filenames = glob.glob('unit6.1.7_*.csv') #import companies' data
companies = []
for filename in filenames:
    company = filename[10:-4] #get company name
    d, p = read_file(filename) #process file
    dates[company] = d  #asign to dict.
    prices[company] = p

# Normalize prices by the price when the most recent
# stock was introduced (normalize_date).
first_months = [dates[company][0] for company in dates] #get 1st date of each company from dates dict.
normalize_date = max(first_months)  #get later date of release of a company
for company in dates:  #for each company
    index = dates[company].index(normalize_date)  #get index of occurence of normalize_date in the list dates[company]
    prices[company] /= prices[company][index] #divide each value of array prices[company] for the value on the normalize_date

# Plot log of price versus years

import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter

fig, ax = plt.subplots()
legends = []
for company in prices:
    ax.plot_date(dates[company], np.log(prices[company]),
                 '-', label=company)
    legends.append(company)
ax.legend(legends, loc='upper left')
ax.set_ylabel('logarithm of normalized value')

# Format the ticks
years    = YearLocator(5)   # major ticks every 5 years
months   = MonthLocator(6)  # minor ticks every 6 months
yearsfmt = DateFormatter('%Y')
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsfmt)
ax.xaxis.set_minor_locator(months)
ax.autoscale_view()
fig.autofmt_xdate()

plt.savefig('unit6.1.7.png')
#plt.show()
