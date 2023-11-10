import csv

# write there name of your file where you want to save all symbols
output_file = open('symbols_file_name.csv', 'w', newline='')
writer = csv.writer(output_file)

# function that extract only symbols from csv file
with open('data_file_name.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        first_param = row[0]
        writer.writerow([first_param])

output_file.close()