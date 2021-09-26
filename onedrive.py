import base64
import pandas as pd


class OneDriveDataset:
    """Download one drive data via the share link. Specify if the file is excel format by passing excel=True."""

    def __init__(self, onedrive_link, name=None, excel=None, sheet=0, header=0):
        self.onedrive_link = onedrive_link
        self.name = name
        self.excel = excel
        self.sheet = sheet
        self.header = header

    def onedrive_directdownload(self):
        """Download and return dataframe"""
        data_bytes64 = base64.b64encode(bytes(self.onedrive_link, "utf-8"))
        data_bytes64_String = (
            data_bytes64.decode("utf-8").replace("/", "_").replace("+", "-").rstrip("=")
        )
        resultUrl = (
            f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
        )
        if self.excel is not None:
                df = pd.read_excel(resultUrl, sheet_name=self.sheet, header=self.header)
        else:
            df = pd.read_csv(resultUrl)
        self.df = df
        return df

    def __getitem__(self, i):
        return self.df[i]

    def __len__(self):
        return len(self)
