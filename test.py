import COVID19Py
covid19 = COVID19Py.COVID19()
# x = covid19.getLatest()
# y = covid19.getLatestChanges()
# print('all: ' + str(covid19.getAll()))
# print('latest: ' + str(x))
# print('latest changes: ' + str(y))

# def get_top_by_infections(country_amount):

data = covid19.getLocationByCountryCode("KG")
print(data) # all info
print(data[0]['latest']['confirmed']) #confirmed
print(data[0]['latest']['deaths']) #deaths