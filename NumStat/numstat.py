
def main():
    while True:
        name_of_file = input("Please enter the name of the file: ")
        i = 0
        try:
            file = open(name_of_file, 'r')
            sum_of_numbers = 0
            total_numbers = 0
            average = 0
            maximum = 0
            minimum = 0
            range_of_numbers = 0
            
            
            
            
            
            for line in file:
                i = int(line)
                sum_of_numbers = sum_of_numbers + i
                total_numbers = total_numbers + 1

                if total_numbers == 0:
                    print("file is empty")
                    exit()


                if total_numbers == 1:
                    maximum = i
                    minimum = i
                else:
                    if i > maximum:
                        maximum = i
                    if i < minimum:
                        minimum = i

                if total_numbers > 0:
                    average = sum_of_numbers/total_numbers
                    range_of_numbers = maximum - minimum


            with open(name_of_file) as file_in:
                lines_list = []
                for line in file_in:
                    lines_list.append(line)

            
            lines_list.sort()
            if len(lines_list) % 2 == 0:
                first_median = lines_list[len(lines_list) // 2]
                second_median = lines_list[len(lines_list) // 2 - 1]
                median = (first_median + second_median) / 2
            else:
                median = lines_list[len(lines_list) // 2]
            
            mode = max(lines_list, key = lines_list.count)

            print("File Name: ", name_of_file)
            print("Sum: ", sum_of_numbers)
            print("Count: ", total_numbers)
            print("Average: ", average)
            print("Maximum: ", maximum)
            print("Minimum: ", minimum)
            print("Range: ", range_of_numbers)
            print("Median of above list is: ",median)
            print("mode is: ", mode)
            file.close()
        
        
        except:
            print("file does not exist :(")

        choice = input('want to perform another evaluation? (y/n) ')
        if choice == 'y':
            continue 
        else:
            break
    


main()
