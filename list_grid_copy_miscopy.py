def main():
    pass

if __name__ == '__main__':
    main()

import os
import glob
import re
import shutil

grid_csv = open (r'D:\python\grid_mkdir_copy\Phase2_GRID_PT1.csv', 'r')
err_ =           r"D:\python\grid_mkdir_copy\Phase2_GRID_PT1_err.csv"
os.chdir(        r"D:\kanref\grid\Phase1_GRID_P2")

i  = 1
ii = 0

for line_cl in grid_csv:
    ii += 1
    grid_name = line_cl[:-1]
    print ii ,"csv",grid_name

    #cp_path = r"D:\IITATE\IITATE_Phase1\EXPORTJPEG\GRID\20\MAP_" + grid_name + ".pdf"
    cp_path = r"D:\kanref\grid\Phase1_GRID_P2\\" + grid_name
    file = "MAP_" + grid_name + ".pdf"

    if os.path.isdir(cp_path):
        print ii
        if not os.path.isdir(    r"D:\kanref\grid\\" + grid_name):
            print grid_name
            # os.makedirs(         r"D:\kanref\grid\Phase1_GRID_P2\\" + grid_name)
            shutil.move(cp_path, r"D:\kanref\grid\Phase2_GRID_P1\\" + grid_name)
    else :
        print ii
        err_txt = open(err_, "a+")
        err_txt.write(grid_name + "\n")
        err_txt.close()

grid_csv.close()

