import pandas as pd
import os


EXPORT_FOLDER = "exports"


if not os.path.exists(EXPORT_FOLDER):
    os.makedirs(EXPORT_FOLDER)



def export_csv(data):
    df = pd.DataFrame(data, columns=["Title", "Source", "Date", "URL"])

    path = os.path.join(EXPORT_FOLDER, "news.csv")

    df.to_csv(path, index=False)

    print(f"CSV exported: {path}")



def export_excel(data):
    df = pd.DataFrame(data, columns=["Title", "Source", "Date", "URL"])

    path = os.path.join(EXPORT_FOLDER, "news.xlsx")

    df.to_excel(path, index=False)

    print(f"Excel exported: {path}")