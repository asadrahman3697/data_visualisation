import csv
from matplotlib import pyplot as plt
from datetime import datetime

def map_header_index(header):
    header_map = {}
    
    for index, column_header in enumerate(header):
        header_map[column_header] = index
    
    return header_map

    
#filename = 'sitka_weather_07-2014.csv'
#filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    # map the header name to the position index
    header_map = map_header_index(header_row)
    
    dates, highs, lows = [], [], []
    
    for row in reader:
        
        try:
            #current_date = datetime.strptime(row[header_map['AKST']], "%Y-%m-%d")
            # DV
            current_date = datetime.strptime(row[header_map['PST']], 
                "%Y-%m-%d")
            high = int(row[header_map['Max TemperatureF']])
            low = int(row[header_map['Min TemperatureF']])
            
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


    # Plot data    
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    
    # Format plot
    plt.title("Daily high and Low temperatures - 2014\nDeath Valley, CA", 
        fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()



    
