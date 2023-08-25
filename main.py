import file_scraper
from file_scraper import the_file_scraper
import linear_reg
from linear_reg import linear_regression_model
import pandas as pd
import datetime as dt


file_data = the_file_scraper("battery-report.html")
charges = the_file_scraper.return_charge()
dates = the_file_scraper.return_date()

columns = list(zip(dates, charges))
df = pd.DataFrame(columns, columns=['Dates','Charge Capacity(mwh)'])
df['Dates'] = pd.to_datetime(df['Dates'])
df['Dates'] = df['Dates'].map(dt.datetime.toordinal)#Lin. Regression doesn't work with string year month time lol


model = linear_regression_model(df)
print(model.return_RMSE())



