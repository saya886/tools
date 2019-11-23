import os
import csv

with open("data.csv", encoding='utf-8') as f:
    file_date_list = csv.reader(f,delimiter='$')
    for row in file_date_list:
        page_header_name = row[0] + " " + row[2]
        os.mkdir(page_header_name)