#uses the input function waits for users input
name = input('What is your name? ')

#prints out a string with the f function 
print(f'Welcome {name} to the Cafe!')


#This variable creates the beverages sold in the cafe.
beverages = ['tea', 'fraps', 'coffee']

#This variable creates the list of price for the beverages.
beverage_price = [1,2,3]

#Using the f function to put together both beverages & beverages_price variables in the string to be outputed.
print(f'Here is what is sold in the Cafe: \n | {beverages[0]} ${beverage_price[0]}    | \n | {beverages[1]} ${beverage_price[1]}  | \n | {beverages[2]} ${beverage_price[2]} |')

#This variable waits for the user to input a string.
UserOrder = input('What would you like to order? ')

#conditional function that will be used to figure out the price of the what the user inputs in UserOrder.
if UserOrder == beverages[0]:
    print(f'Your total due is ${beverage_price[0]}.00')
elif UserOrder == beverages[1]:
    print(f'Your total due is ${beverage_price[1]}.00')
elif UserOrder == beverages[2]:
    print(f'Your total due is ${beverage_price[2]}.00')
else:
    print('Sorry we do not sell that drink here. Please try again')
