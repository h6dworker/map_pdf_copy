def main():
    pass

if __name__ == '__main__':
    main()

import os
import glob
import re
import shutil

os.chdir(r"D:\IITATE\IITATE_Phase1\EXPORTJPEG\GRID\20")

r = re.compile("\-\d.pdf")

i  = 1
ii = 0

files_pdf = os.listdir(os.getcwd())
for file in files_pdf:

    kid1 = r.findall(file)
    kid2 = file.replace(".pdf", "")

    kid3 = kid2.replace("MAP_","")
   # kid3 = kid2.replace("AM_1M_","")

    ii += 1

    check = os.path.isdir(r"D:\kanref\grid\\" + kid3)

    if not check:
        os.makedirs(r"D:\kanref\grid\\" + str("".join(kid3)))

    shutil.move(file, r"D:\kanref\grid\\" + str("".join(kid3)) +"\\" + file)
    print file, kid3

##    shutil.copy2(file, r"D:\kanref\grid\\" + str("".join(kid)) +"\\" + file)
##    if ii == 3:
##        break

