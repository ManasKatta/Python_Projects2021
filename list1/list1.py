def display_list(label, items):
    print(label)
    for i in items:
        print(i)




def main():
    foods = ["pizza", "salad", "hamburger", "steak", "apple", "orange"]
    display_list("\nFood:", foods)
    foods.sort()
    display_list("\nFood in ascending alphabetical order:", foods)
    foods.sort(reverse=True)
    display_list("\nFood in descending alphabetical order:", foods)
    foods2 = sorted(foods)
    display_list("\nFood2 in ascending alphabetical order:", foods2)
    display_list("\nFood still in descending alphabetical order:", foods)
    foods.reverse()
    display_list("\nFood in ascending alphabetical order:", foods)
    foods.append("carrots")
    foods.append("milk")
    display_list("\nsorted foods with carrots and milk appended", foods)
    foods.sort()
    display_list("\nFood in ascending alphabetical order with carrots and milk:", foods)
    pizza_index = foods.index("pizza")
    print("Pizza is at", pizza_index)
    foods.insert(pizza_index, "fries")
    print("Pizza is now at", foods.index("pizza"))
main()