#_author_: W. Bukhsh
#_contact_: wbukhsh[at]gmail.com
#_web_:wbukhsh.com

#===import packages===
import pandas as pd
import matplotlib.pyplot as plt


filename = 'gridwatch.csv'
data = pd.read_csv(filename)
#strip the leading white space from the headers
data =  data.rename(columns=lambda x:x.strip())
for key in data:
    data[key] = data[key].map(lambda x: str(x).strip())

data['timestamp'] = pd.to_datetime(data['timestamp'],
                                   format="%Y-%m-%d %H:%M:%S")
data['demand'] = pd.to_numeric(data['demand'])
data.set_index('timestamp', inplace=True)
data = data[(data.demand>15000) & (data.demand<60000)]
ax = data['demand'].plot()
#plt.show()
plt.savefig('demandGB2016_raw.png')
