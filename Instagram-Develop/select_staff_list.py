from numpy import False_
import pandas as pd
if __name__ == '__main__':
    df_follows=pd.read_csv('camcolle_koyo_follows_list.csv',header=None, names=['Name'])
    df_staff_list=pd.read_csv('staff_list.csv')
    followes=list(df_follows['Name'])
    staff_list=[]
    df_staff_list=list(df_staff_list['Name'])
    for staff in df_staff_list:
        staff_list.append(staff)

    for list in followes:
        if('camcolle' in list):
            staff_list.append(list)
    df_staff=pd.Series(staff_list,name='Name')
    df_staff.to_csv("staff_list.csv",index=False)