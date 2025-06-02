import csv 

with open(r"C:\Users\bjon6\OneDrive\Desktop\business eval\Code\num_part6.txt", "r", encoding="utf-8") as infile, \
     open(r"C:\Users\bjon6\OneDrive\Desktop\business eval\Code\num_part6.csv", "w", newline='', encoding="utf-8") as outfile:
    tsv_reader = csv.reader(infile, delimiter="\t")
    csv_writer = csv.writer(outfile)
    
    for row in tsv_reader:
        csv_writer.writerow(row)