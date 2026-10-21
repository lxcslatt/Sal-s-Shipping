#This code is for a shipping company they charge depending on the weight of the package and also the type of delivery
'''
Here are the prices:

Ground Shipping

Weight of Package	                        Price per Pound	               Flat Charge
2 lb or less	                               $1.50	                       $20.00
Over 2 lb but less than or equal to 6 lb	   $3.00             	           $20.00
Over 6 lb but less than or equal to 10 lb  	 $4.00	                       $20.00
Over 10 lb	                                 $4.75	                       $20.00

Ground Shipping Premium

Flat charge: $125.00

Drone Shipping

Weight of Package	                       Price per Pound	               Flat Charge
2 lb or less	                               $4.50	                        $0.00
Over 2 lb but less than or equal to 6 lb	   $9.00                         	$0.00
Over 6 lb but less than or equal to 10 lb	   $12.00	                        $0.00
Over 10 lb	                                 $14.25	                        $0.00
'''


# the flat charge for ground shipping premium this has no weight charge
gsp = 125.00
# lets user input their weight of package and changes their response to a float for calculation
weight = float(input("How much does your package weigh in lb. Respond in numbers"))
# lets user choose what option they want the .lower code lets them write the option in any capitalisation
option = input("Choose shipping: ground, premium or drone: ").lower()
gs = (0.0) # the ground shipping (gs) variable set to 0 
drone = (0.0) # the drone shipping (drone) variable set to 0
# Calculation using the information in the table above 
# The if,elif statements run specific calculation depending on the weight of the package and stores it in the gs or drone variable waiting to be called upon 
if weight <= 2:
	gs = ( weight * 1.50 + 20)
elif weight > 2 and weight <= 6:
	gs = ( weight * 3.00 + 20)
elif weight > 6 and weight <= 10:
	gs = ( weight * 4 + 20)
else:
	gs = (weight * 4.75 + 20)

if weight <=2:
	drone = (weight * 4.50)
elif weight > 2 and weight <= 6:
	drone = (weight * 9.00)
elif weight > 6 and weight <= 10:
	drone = (weight * 12)
else:
	drone = (weight * 14.25)
# depending on what option was chosen ground drone or premium var with the calculation is printed 
if option == "ground" :
	print (f"you have selected ground shipping. Your weight: {weight} lb and your price is : £{gs}")
elif option == "drone" :
	print (f"you have selected drone shipping. Your weight: {weight} lb and your price is : £{drone}")
elif option == "premium" :
	print (f"you have selected ground premium shipping. Your weight: {weight} lb and your price is : £{gsp}")
else:
	print ("sorry thats not an option")
