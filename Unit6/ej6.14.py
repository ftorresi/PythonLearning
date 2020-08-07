from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter

def readhtm(filename):
    citytotxt={}
    with open(filename,"r") as infile:
        alllines=infile.readlines()
        for i in range(len(alllines)):
            if '     mso-list' in alllines[i] and '     href=' in alllines[i+2] : #Most cases
                city=alllines[i].split('<b>')[1].split(' ( ')[0]
                if ' (' in city: #to aviod problems w/ BOMBAY and CHENNAI
                    city=city.split(' (')[0] 
                txt=alllines[i+2].split('>')[1].split('<')[0]
                citytotxt[city]=txt
            elif '     mso-list' in alllines[i] and '     href=' in alllines[i+1] : #Dubai, Abu Dhabi & Taipei
                city=alllines[i].split('<b>')[1].split('<')[0]
                txt=alllines[i+2].split('>')[1].split('<')[0]
                citytotxt[city]=txt
    return citytotxt


def citydata(city, citytotxt):
    filename="ej6.14/"+citytotxt[city]
    citydata={}
    temps=[]
    dates=[]
    with open(filename,"r") as infile:
        for line in infile:
            m,d,y,T=line.split()
            T=float(T)
            if not T==-99.0:
                for data in (m,d,y):
                    data=data.strip() #remove whitespace
                date="-".join([y,m,d])
                dates.append(date)
                temps.append(float(T))
            
        datefmt = "%Y-%m-%d" #date format
        dates = [datetime.strptime(_date, datefmt).date()
             for _date in dates] #Convert to date objects
        temps = np.array(temps)
    return dates, temps        
            

def plotter(cities,citytotxt):
    dates={}
    temps={}
    for city in cities:
        d,t=citydata(city, citytotxt)
        dates[city]= d  
        temps[city]= t
    
    
    fig, ax = plt.subplots()
    legends = []
    for city in temps:
        ax.plot_date(dates[city], temps[city],
                     '-', label=city)
        legends.append(city)
        ax.legend(legends, loc='lower left')
        ax.set_ylabel('Temperature [F]')
        ax.set_xlabel('Date')

       
    # Format the ticks
    years    = YearLocator(2)   # major ticks every 2 years
    months   = MonthLocator(bymonth=(1,7))  # minor ticks every 6 months, for months 1&7
    yearsfmt = DateFormatter('%Y')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsfmt)
    ax.xaxis.set_minor_locator(months)
    ax.autoscale_view()
    fig.autofmt_xdate()
    plt.savefig("ej6.14.png")


      
    

cityfiles=readhtm("ej6.14/citylistWorld.htm")
cities=["Dubai","Buenos Aires", "Oslo"] 
plotter(cities,cityfiles)
#plt.show()        
