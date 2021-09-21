import base64
import pandas as pd


class OneDriveDataset:
    def __init__(self, onedrive_link, name=None, excel=None):
        self.onedrive_link = onedrive_link
        self.name = name
        self.excel = excel

    
    def onedrive_directdownload (self):#, onedrive_link, excel=None):
        data_bytes64 = base64.b64encode(bytes(self.onedrive_link, 'utf-8'))
        data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
        resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
        if self.excel is not None: df = pd.read_excel(resultUrl)
        else: df = pd.read_csv(resultUrl)
        self.df = df
        return df

    def __getitem__(self, i):
        return self.df[i]

    def __len__(self):
        return 1
