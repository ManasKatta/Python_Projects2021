while True:
    
    while True: 
        try:
            square_feet = float(input('\nEnter size in square feet: '))
            if (square_feet < 0):
                print('\nno negative size allowed')
            else:
                break
        except ValueError:
            print('\nplease enter a float')
    
    while True: 
        try:
            paint_price = float(input('Enter price of paint in cost per gallon: '))
            if(paint_price < 0):
                print('\nno negative price allowed')
            else:    
                break
        except ValueError:
            print('\nplease enter a float')
    import math
    
    gallons_of_paint = math.ceil(float(square_feet)/350)
    hours_of_labor = (float(square_feet)/350)*6
    cost_of_paint = float(gallons_of_paint)*float(paint_price)
    cost_of_labor = float(hours_of_labor)*62.25
    total_cost = float(cost_of_labor) + float(cost_of_paint)

    print('\nResults\n')
    print('Gallons of paint: ', gallons_of_paint)
    print("Hours of Labor: {:.1f}".format(hours_of_labor));
    print("Cost of paint: ${:.2f}".format(cost_of_paint));
    print("Cost of labor: ${:.2f}".format(cost_of_labor));
    print("Total cost: ${:.2f}\n".format(total_cost));
    
    
    
    
    choice = input('want to perform another calculation? (y/n) ')
    if choice == 'y':
        continue 
    else:
        break
 
