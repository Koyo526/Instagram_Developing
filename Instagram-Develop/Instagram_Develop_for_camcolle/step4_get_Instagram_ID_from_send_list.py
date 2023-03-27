import pandas as pd
def get_Instagram_ID_from_send_list(self):
        df_guest=pd.read_csv("today_guset_list.csv")
        df_guest=df_guest['Name'].tolist()
        instagram_id=[]
        for guest in df_guest:
            id='@'+guest
            instagram_id.append(id)
        df_id=pd.Series(instagram_id,name='ID')
        df_id.to_csv("Guest_Instagram_ID.csv",index=False)
if __name__=='__main__':
    get_Instagram_ID_from_send_list()