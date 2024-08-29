import pandas as pd
import tabulate

def main():
    file_xlsx = './Architecture_Books.xlsx'

    print("Reading the Excel file...")
    dataframe_book_list = pd.read_excel(file_xlsx)
    
    print("Removing lines with the same 'Identifier'...")
    dataframe_book_list = dataframe_book_list.drop_duplicates(subset=['Identifier'], keep='first')
    
    print("Organizing the dataframe by 'Language'...")
    dataframe_book_list = dataframe_book_list.sort_values(by=['Language'])

    print("Saving the Excel file...")
    dataframe_book_list.to_excel(file_xlsx, index=False)

if __name__ == "__main__":
    main()
