import csv 
# with open('names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     with open('new_names.csv') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#         for line in csv_reader:
#             csv_writer.writerow(line) 

# with open('new_names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')
#     for line in csv_reader:
#         print(line)
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # for line in csv_reader:
    #     print(line['email']) # By using this email key, we can directly get all emails 
    with open('new_names.csv','w') as new_file:
        fieldnames = ['first_name', 'last_name'] # DictWriter needs field names 
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader() # To give the headers i.e. fieldnames in 1st row 
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line) 

    # print(csv_reader)
    # next(csv_reader)
    # for line in csv_reader:
    #     print(line[2]) 