import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sbn
import csv



data = pandas.read_csv('API_19_DS2_en_csv_v2_4700503.csv', skiprows=4)
data

data=data.drop(data[['Unnamed: 66']],axis=1)
data

# ### Transpose

'''This  function is created to transpose the value of the variable in which  dataset is stored. For transposing the dataset, here .T is  used and for reading  the csv files pandas used here. '''
def transpose():
    dataTrans = pandas.read_csv('API_19_DS2_en_csv_v2_4700503.csv', skiprows=4, index_col=0, header=None).T
    dataTrans


# ## Handling Null Values

data.isnull().sum()

data.fillna(value = 0, inplace = True)
data.isnull().sum()

data.describe()

data.rename(columns={'Country Name':'CountryName','Country Code':'CountryCode','Indicator Name':'IndicatorName','Indicator Code':'IndicatorCode'},inplace=True)


# # Urban Population

indi = data.groupby(['CountryName']).first()
indi1=indi.head(10)
print(indi1)

indi1 = indi1.reset_index()
indi1

X = ['Afghanistan','Africa Eastern and Southern','Africa Western and Central','Albania','Algeria','American Samoa', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Arab World']
fig = plt.figure(figsize = (30,8))
X_axis = np.arange(len(X))
plt.bar(X_axis - 0.6, indi1['2016'], 0.4, label = '1960')
plt.bar(X_axis - 0.4, indi1['2017'], 0.4, label = '1980')
plt.bar(X_axis - 0.2, indi1['2018'], 0.4, label = '2000')
plt.bar(X_axis + 0.2, indi1['2019'], 0.4, label = '2010')
plt.bar(X_axis + 0.4, indi1['2020'], 0.4, label = '2020')
plt.bar(X_axis + 0.6, indi1['2021'], 0.4, label = '2021')
  
plt.xticks(X_axis, X, rotation = 'vertical')
plt.xlabel("Countries")
plt.ylabel("Urban Population Percentage")
plt.title("Urban Population percentage VS Country")
plt.legend()
plt.show()


data.head(44)

finalData=data.groupby(['CountryName','CountryCode','IndicatorName', 'IndicatorCode','1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']).size().reset_index()
finalData.head()


# # Foreign Direct Investment

finalData.set_index("IndicatorName", inplace=True)
value="Foreign direct investment, net inflows (% of GDP)"
foreign = finalData.loc[value]
foreign = foreign.drop(["CountryCode","IndicatorCode"],axis =1)

foreign.head()

foreignPlot =foreign[::30]
foreignPlot=foreignPlot[["CountryName",'1990', '2000', '2010', '2012', '2014', '2018', '2021']]
foreignPlot=foreignPlot.reset_index(drop=True)
foreignPlot=foreignPlot.set_index(['CountryName'])
foreignPlot

plt.figure(figsize = (14,9))
sbn.heatmap(foreignPlot,annot=True,linewidth=2,cmap="Greens")
plt.title('Country VS Foreign Direct investment(% of GDP)')


# # CO2 emission

co2DataValue="CO2 emissions from liquid fuel consumption (kt)"
co2Data = finalData.loc[co2DataValue]
co2Data = co2Data.drop(["CountryCode","IndicatorCode"],axis =1)
co2Data.head()


xyear=['1990', '2000', '2010', '2012', '2014', '2018', '2021']
co2Data = co2Data[:30]
co2Data.plot(x="CountryName", y=xyear, figsize=(20,12))
plt.title("CO2 emmission by liquid fuel")
plt.ylabel("Amount of CO2 in power of e")


# # Growth  of Population

growthValue="Population growth (annual %)"
growth = finalData.loc[growthValue]
growth.head()


growthYear=['1960', '1980', '1970', '1990', '2000', '2010', '2020', '2021']
growth = growth[:10]
growth.plot(x="CountryName", y=xyear, kind="bar", figsize=(25,12))
plt.title("Growth of population yearly")
plt.ylabel("Growth in  percentage")



