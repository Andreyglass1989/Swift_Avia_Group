#install 
#pip3 install fbprophet

import pandas as pd
from fbprophet import Prophet

df = pd.read_csv('/root/Machine Learning/data-cargo.csv')
df.head()

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=30)
future.tail()


forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()



