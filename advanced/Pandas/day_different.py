import pandas as pd

## -- End pasted text --
Out[12]: 'Saturday'

date = pd.to_datetime(['15-10-18', '08-10-18', '08-10-18', '27-09-18', '14-09-18', '05-09-18', '03-09-18', '20-08-18', '10-08-18', '06-08-18', '31-07-18', '30-07-18', '19-07-18', '19-07-18', '13-07-18', '25-06-18', '19-06-18', '16-06-18', '30-05-18', '25-05-18', '24-05-18', '22-05-18', '21-05-18', '19-05-18', '19-05-18', '14-05-18', '12-05-18', '08-05-18', '07-05-18', '02-05-18', '02-05-18', '24-04-18', '27-03-18', '26-03-18', '26-03-18', '14-03-18', '12-03-18'])


#data_dict = pd.DataFrame({'China': listChina, 'English': listEng})


data = pd.Series(listChina, index=listEng)


list_player = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B']
list_date =['2010-01-01', '2010-01-09', '2010-01-11', '2010-01-15', '2010-02-01', '2010-02-10', '2010-02-21', '2010-02-23']


data = pd.DataFrame({'Player': list_player, 'date': list_date})

data['difference'] = data.groupby('Player')['date'].diff().fillna(0)



def date_diff(row):
    index = data.index.get_loc(row.name)
    if index == 0:
        return np.nan
    prev_row = data.iloc[index - 1]
    return datetime.strptime(row['date'], "%Y-%m-%d") - datetime.strptime(prev_row['date'], "%Y-%m-%d")

data['difference'] = data.apply(date_diff, axis=1)
#d = datetime.strptime("2015-04-06", "%Y-%m-%d")