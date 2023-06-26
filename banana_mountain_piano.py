#import libraries
import random
import datetime

#define functions
def find_perfect_gift():
	'''
	Generates a perfect gift based on the time of year
	'''
	#find the current date and month
	now = datetime.datetime.now()
	month = now.month
	
	#determine the perfect gift based on the month
	if month == 12:
		perfect_gift = "Christmas present"
	elif month == 11:
		perfect_gift = "Advent calendar"
	elif month == 10:
		perfect_gift = "Halloween spook"
	elif month == 9:
		perfect_gift = "Fall harvest basket"
	elif month == 8:
		perfect_gift = "Summer picnic basket"
	elif month == 7:
		perfect_gift = "Beach blanket and umbrella"
	elif month == 6:
		perfect_gift = "Barbeque accessories"
	elif month == 5:
		perfect_gift = "Flowers for Mother's Day"
	elif month == 4:
		perfect_gift = "Easter basket"
	elif month == 3:
		perfect_gift = "St. Patrick's Day leprechaun"
	elif month == 2:
		perfect_gift = "Valentine's Day card"
	elif month == 1:
		perfect_gift = "New Year's resolutions journal"
	
	return perfect_gift
	
def find_creative_gift():
	'''
	Generates a creative gift based on a random number
	'''
	#find a random number to determine gift
	random_number = random.randint(1, 10)
	
	#determine the creative gift based on the random number
	if random_number == 1:
		creative_gift = "DIY gift basket"
	elif random_number == 2:
		creative_gift = "Personalized mug"
	elif random_number == 3:
		creative_gift = "Coupon book for services"
	elif random_number == 4:
		creative_gift = "Memory jar filled with notes"
	elif random_number == 5:
		creative_gift = "Homemade gift box"
	elif random_number == 6:
		creative_gift = "Unique keychain"
	elif random_number == 7:
		creative_gift = "Origami flower"
	elif random_number == 8:
		creative_gift = "Fleece blanket"
	elif random_number == 9:
		creative_gift = "T-shirt stating a funny message"
	elif random_number == 10:
		creative_gift = "DIY framed photo"
	
	return creative_gift

def find_thoughtful_gift():
	'''
	Generates a thoughtful gift based on the recipient
	'''
	#ask the user for input on the recipient
	recipient = input("Who are you giving the gift to? ")
	
	#determine the thoughtful gift based on the recipient
	if recipient == "child":
		thoughtful_gift = "Customized stuffed animal"
	elif recipient == "parent":
		thoughtful_gift = "Homemade photo album"
	elif recipient == "friend":
		thoughtful_gift = "DIY friendship bracelet"
	elif recipient == "teacher":
		thoughtful_gift = "Handmade thank you card"
	elif recipient == "spouse":
		thoughtful_gift = "Thoughtful handwritten letter"
	
	return thoughtful_gift
	
#main code
if __name__ == "__main__":
	#welcome message
	print("Welcome to The Art of Giving!\n")
	
	#ask the user for input on the type of gift
	gift_type = input("What type of gift would you like to find? Perfect, creative, or thoughtful? ")
	
	#determine the type of gift and generate suggestion
	if gift_type == "perfect":
		perfect_gift = find_perfect_gift()
		print("Consider giving a {}.".format(perfect_gift))
	elif gift_type == "creative":
		creative_gift = find_creative_gift()
		print("Consider giving a {}.".format(creative_gift))
	elif gift_type == "thoughtful":
		thoughtful_gift = find_thoughtful_gift()
		print("Consider giving a {}.".format(thoughtful_gift))
	else:
		print("Sorry, that's not a valid input.")