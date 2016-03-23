def main():
    pass

if __name__ == '__main__':
    main()

import os
import glob
import re
import shutil

grid_csv = open (r'D:\python\grid_mkdir_copy\Phase1_GRID_P3_US.csv', 'r')
err_ =           r"D:\python\grid_mkdir_copy\Phase1_GRID_P3_err.csv"

i  = 1
ii = 0

for line_cl in grid_csv:
    ii += 1
    grid_name = line_cl[:-1]

    cp_path = r"D:\IITATE\IITATE_Phase1\EXPORTJPEG\GRID\20\MAP_" + grid_name + ".pdf"
    file = "MAP_" + grid_name + ".pdf"

    if os.path.isfile(cp_path):
        if not os.path.isdir(    r"D:\kanref\grid\Phase1_GRID_P3\\" + grid_name):
            print grid_name, ii
            os.makedirs(         r"D:\kanref\grid\Phase1_GRID_P3\\" + grid_name)
            shutil.move(cp_path, r"D:\kanref\grid\Phase1_GRID_P3\\" + grid_name +"\\" + file)
    else :
        err_txt = open(err_, "a+")
        err_txt.write(grid_name + "\n")
        err_txt.close()

grid_csv.close()

