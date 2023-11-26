import pandas as pd

def dataFrameConjunction(df1, df2, lb1, lb2, equipment_window, time_window, pattern_data, pattern_new):
    twindow = pd.Timedelta(days=time_window)
    ewindow = pd.Timedelta(days=equipment_window)
    for i in range(pattern_data.shape[0]):
        timenow = pattern_data.iloc[i]['FaultDateTime']
        temp = 0
        for j in range(i, pattern_data.shape[0]):
            temp = j
            if pattern_data.iloc[j]['FaultDateTime'] - timenow > ewindow:
                break
            inner_eq = pattern_data.iloc[j]['Equipment']
            df1[inner_eq][i] += 1
        cur_dt = pattern_data.iloc[temp]['FaultDateTime']
        for j in range(temp, pattern_data.shape[0]):
            inner_eq = pattern_data.iloc[j]['Equipment']
            inner_dt = pattern_data.iloc[j]['FaultDateTime']
            if inner_eq == 'ion source':
                lb1.iloc[i]['Label'] = 1
                break
            if (inner_dt - cur_dt) >= twindow:
                break

    for i in range(pattern_new.shape[0]):
        timenow = pattern_new.iloc[i]['FaultDateTime']
        temp = 0
        for j in range(i, pattern_new.shape[0]):
            temp = j
            if pattern_new.iloc[j]['FaultDateTime'] - timenow > ewindow:
                break
            inner_eq = pattern_new.iloc[j]['Equipment']
            df2[inner_eq][i] += 1
        cur_dt = pattern_new.iloc[temp]['FaultDateTime']
        for j in range(temp, pattern_new.shape[0]):
            inner_eq = pattern_new.iloc[j]['Equipment']
            inner_dt = pattern_new.iloc[j]['FaultDateTime']
            if inner_eq == 'ion source':
                lb2.iloc[i]['Label'] = 1
                break
            if (inner_dt - cur_dt) >= twindow:
                break
    return df1, df2, lb1, lb2