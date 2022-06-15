while True:
    name_of_file = input("Please enter the name of the file: ")
    i = 0
    sum_of_numbers = 0
    total_numbers = 0
    average = 0
    maximum = 0
    minimum = 0
    numbers_list = []
    range_of_numbers = 0
    try:
        file = open(name_of_file, 'r')
        

        for line in file:
            i = int(line)
            numbers_list.append(i)
            sum_of_numbers = sum_of_numbers + i
            total_numbers = total_numbers + 1
            
            if total_numbers == 1:
                maximum = i
                minimum = i
            else:
                if i > maximum:
                    maximum = i
                if i < minimum:
                    minimum = i

        if total_numbers == 0:
            print("file is empty:(")
        else:
            average = sum_of_numbers/total_numbers
            range_of_numbers = maximum - minimum
            numbers_list.sort()
            if total_numbers % 2 == 0:
                median1 = numbers_list[total_numbers//2]
                median2 = numbers_list[total_numbers//2-1]
                median = (median1+median2)/2
            else:
                median = numbers_list[total_numbers//2]
            
            num_count = {}

            for num in numbers_list:
                if num in num_count:
                    num_count[num] += 1
                if num not in num_count:
                    num_count[num] = 1
            
            maxmode = max(num_count.values()) 
            modes = []

            for num in num_count:
                count = num_count[num]
                if count > maxmode:
                    maxmode = count
                if count == maxmode:
                    modes.append(num)
            
            print("File Name: ", name_of_file)
            print("Sum: ", sum_of_numbers)
            print("Count: ", total_numbers)
            print("Average: ", average)
            print("Maximum: ", maximum)
            print("Minimum: ", minimum)
            print("Range: ", range_of_numbers)
            print("median: ", median)
            print("modes: ", modes)
        
        file.close()
    except:
        print("file does not exist :(")

    choice = input('want to perform another evaluation? (y/n) ')
    if choice == 'y':
        continue 
    else:
        break
 

