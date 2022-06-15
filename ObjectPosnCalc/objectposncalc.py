while True:
    
    while True: 
        try:
            initial_position = float(input('\nEnter initial position in meters: '))
            if (initial_position < 0):
                print("\nno negative initial position allowed")
            else:
                break
        except ValueError:
            print('\nplease enter a float')
    
    while True: 
        try:
            initial_velocity = float(input('Enter initial velocity in meters/second: '))
            break
        except ValueError:
            print('\nplease enter a float')
    
    while True: 
        try:
            acceleration = float(input('Enter acceleration in meters/second squared: '))
            break
        except ValueError:
            print('\nplease enter a float')
    
    while True: 
        try:
            time = float(input('Enter time in seconds: '))
            if (time < 0):
                print("\nno negative times allowed")
            else:
                break
        except ValueError:
            print('\nplease enter a float')

    final_position = float(initial_position) + float(initial_velocity) * float(time) + 0.5 * float(acceleration) * float(time) * float(time)
    print('\n\nThe final position of the object is', final_position, 'meters\n')
    choice = input('want to perform another calculation? ')
    if choice == 'y':
        continue 
    else:
        break
 
