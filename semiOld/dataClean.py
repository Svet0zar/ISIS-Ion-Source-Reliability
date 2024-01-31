import pandas as pd

def cleanData(downtime_data, downtimeNew):
    downtime_data['FaultDate'] = pd.to_datetime(downtime_data['FaultDate'], errors='coerce').dt.date
    downtimeNew['FaultDate'] = pd.to_datetime(downtimeNew['FaultDate'], errors='coerce').dt.date

    downtime_data['FaultTime'] = downtime_data['FaultTime'].apply(lambda x: x.strftime('%H:%M:%S') if len(str(x)) > 8 else x)
    downtimeNew['FaultTime'] = downtimeNew['FaultTime'].apply(lambda x: x.strftime('%H:%M:%S') if len(str(x)) > 8 else x)

    downtimeNew = downtimeNew.dropna(subset=['FaultDate', 'FaultTime'])

    pattern_data = downtime_data.iloc[:, :14]
    pattern_data = pattern_data.drop(['ID', 'DutyOfficer', 'Manager email address'], axis=1)
    pattern_data['FaultDateTime'] = pd.to_datetime(pattern_data['FaultDate'].astype(str) + ' ' + pattern_data['FaultTime'].astype(str))
    dt2010 = pd.to_datetime('2010-01-01 00:00:00')
    pattern_data.drop(['FaultDate', 'FaultTime'], axis=1, inplace=True)
    pattern_data.sort_values(by=['FaultDateTime'], inplace=True)
    pattern_data = pattern_data[pattern_data['FaultDateTime'] >= dt2010]
    pattern_data = pattern_data.drop(['LogEntry', 'DutyOfficer comments', 'Managerscomments', 'FaultRepair', 'FaultDescription', 'Group', 'Downtime', 'User Run'], axis=1)

    pattern_new = downtimeNew.iloc[:, :14]
    pattern_new = pattern_new.drop(['ID', 'DutyOfficer', 'Manager email address'], axis=1)
    pattern_new['FaultDateTime'] = pd.to_datetime(pattern_new['FaultDate'].astype(str) + ' ' + pattern_new['FaultTime'].astype(str))
    dtnew = pd.to_datetime('2023-08-04 06:00:00') ## change month to 8
    pattern_new.drop(['FaultDate', 'FaultTime'], axis=1, inplace=True)
    pattern_new.sort_values(by=['FaultDateTime'], inplace=True)
    pattern_new = pattern_new[pattern_new['FaultDateTime'] >= dtnew]
    pattern_new = pattern_new.drop(['LogEntry', 'DutyOfficer comments', 'Managerscomments', 'FaultRepair', 'FaultDescription', 'Group', 'Downtime', 'User Run'], axis=1)

    pattern_data['Equipment'] = pattern_data['Equipment'].str.lower()
    pattern_data['Equipment'] = pattern_data['Equipment'].str.replace('[^\w\s]', '')

    pattern_new['Equipment'] = pattern_new['Equipment'].str.lower()
    pattern_new['Equipment'] = pattern_new['Equipment'].str.replace('[^\w\s]', '')

    return pattern_data, pattern_new