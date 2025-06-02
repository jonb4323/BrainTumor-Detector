import os

input_file = "C:/Users/bjon6/OneDrive/Desktop/business eval/Code/num.txt"

def split_file(input_file, max_size_mb=99):
    max_size_bytes = max_size_mb * 1024 * 1024
    part_num = 1
    current_size = 0

    output_path = f"C:/Users/bjon6/OneDrive/Desktop/business eval/Code/num_part{part_num}.txt"
    output_file = open(output_path, "w", encoding="utf-8")

    with open(input_file, "r", encoding="utf-8") as infile:
        print("Splitting in progress...")
        for line in infile:
            line_size = len(line.encode("utf-8"))

            if current_size + line_size > max_size_bytes:
                output_file.close()
                part_num += 1
                current_size = 0
                output_path = f"C:/Users/bjon6/OneDrive/Desktop/business eval/Code/num_part{part_num}.txt"
                output_file = open(output_path, "w", encoding="utf-8")

            output_file.write(line)
            current_size += line_size

    output_file.close()
    print(f"File split into {part_num} parts under {max_size_mb}MB")

split_file(input_file, max_size_mb=99)
