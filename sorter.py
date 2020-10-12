import pandas as pd
from sys import argv

class ExelSorter():
    '''This is an excel sorter class that uses
    that divides an exel file into multiple files
    sorted by a column.  The class takes the file
    name the header column which you want to sort by
    and any variable name you wish to drop as output'''
    def __init__(self, file_name, header_name, *args):
        self.file_name = file_name
        self.header_name = header_name
        self.drop_columns = args[0]


    def read_xcel_file(self):
        return pd.read_excel(self.file_name)

    def output_xlsx(self, df, name):
        return df.to_excel(name, index = False)

    def produce_reports(self, df):
        print(self.drop_columns)
        reports = df[self.header_name].unique()
        for report in reports:
            df1 = df[df[self.header_name]==report]
            df1.drop(axis = 1,columns = self.drop_columns, inplace = True)
            file_name = f'{report}.xlsx'
            self.output_xlsx(df1,file_name)

    def overall_process(self):
        df = self.read_xcel_file()
        self.produce_reports(df)




if __name__ == '__main__':
    file_name = argv[1]
    header_name = argv[2]
    try:
        drop_names = argv[3:]
    except:
        drop_names = None

    print(file_name,header_name)
    xsort = ExelSorter(file_name, header_name,drop_names)
    xsort.overall_process()
