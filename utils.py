
import os
import sys
import pandas as pd
import pyexcel as pe

home_dir = os.path.expanduser("~")
bot_dir = os.path.join(home_dir, "NSE BOT")

def refresh_excel_file(excel_file):
    excel_file_path = os.path.join(bot_dir, excel_file)
    
    book = pe.get_book(file_name=excel_file_path)
    book.refresh()
    book.save_as(excel_file_path)

def write_dataframe_to_excel(dataframe, excel_file):

    if not os.path.exists(bot_dir):
        os.makedirs(bot_dir)    

    excel_file_path = os.path.join(bot_dir, excel_file)
    
    if os.path.exists(excel_file_path):
        # Append the new dataframe to the existing Excel file
        with pd.ExcelWriter(excel_file_path, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            last_sheet = writer.book.worksheets[-1] # get the last sheet object
            startrow = last_sheet.max_row + 1 # get the next row to start writing at
            dataframe.to_excel(writer, header=False, startrow=startrow, index=False, engine='openpyxl')
        
    else:
        dataframe.to_excel(excel_file_path, header=True, index=False, engine='openpyxl')


