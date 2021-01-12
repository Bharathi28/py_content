import xlrd
import os

SheetName = 'Content'
script_dir_in = os.path.dirname(__file__)  # <-- absolute dir the script is in


# C:\Users\manibharathi\.jenkins\workspace\py_content


def my_function():
    rel_path = "Input_Output/Content/run_input.xlsx"
    input_file_in = os.path.join(script_dir_in, rel_path)
    print(input_file_in)
    book = xlrd.open_workbook(input_file_in)
    sh = book.sheet_by_index(0)
    # print("Sheetname:{0} Rows:{1} Columns:{2}". format(sh.name, sh.nrows, sh.ncols))
    data = [[sh.cell_value(r, c) for c in range(sh.ncols)] for r in range(sh.nrows)]
    # print(data)
    return data


def driver_path():
    # driver_in = "C://Users\manibharathi//.jenkins//workspace//py_content//Driver//chromedriver.exe"
    drive_path = "Driver/chromedriver.exe"
    input_drive_in = os.path.join(script_dir_in, drive_path)
    print(input_drive_in)
    return input_drive_in


rel_path_in = "Input_Output/run_input.xlsx"
input_file = os.path.join(script_dir_in, rel_path_in)


def getExcelData(input_path, sheet_name):
    book = xlrd.open_workbook(input_path)
    sheet = book.sheet_by_name(sheet_name)

    # data = [[sh.cell_value(r, c) for c in range(sh.ncols)] for r in range(sh.nrows)]
    # print(data)
    # return data

    for i in range(1, sheet.nrows):
        print(i)
