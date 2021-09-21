import base64
import pandas as pd


class OneDriveDataset:
    def __init__(self, name=None):
        self.name = name
    
    def onedrive_directdownload (self, onedrive_link):
        data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
        data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
        resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
        df = pd.read_csv(resultUrl)
        self.df = df
        return df

    def __getitem__(self, i):
        return self.df

    def __len__(self):
        return 1
