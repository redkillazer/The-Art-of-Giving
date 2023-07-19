package main 

import "fmt"

// Function to define and provide an example of a simple, meaningful gift
func simpleGift() {
	fmt.Println("A simple, meaningful gift could be a handwritten letter or card, expressing thoughts and feelings about the recipient.")
}

// Function to define and provide an example of a thoughtful gift
func thoughtfulGift() {
	fmt.Println("A thoughtful gift could be a framed photo of the two of you together, or a gift that reflects something special between you and the recipient.")
}

// Function to define and provide an example of a practical gift
func practicalGift() {
	fmt.Println("A practical gift could be something the recipient could use for everyday tasks, such as a quality laptop or travel bag.")
}

// Function to prompt user to select a type of gift
func promptUser() {
	fmt.Println("Which type of gift would you like to learn more about? \n1. Simple \n2. Thoughtful \n3. Practical")
}

//Main function to output Examples of gifts based on user selection
func main() {
	promptUser()
	
	// Initialize variable to store user input
	var selection int
	
	// Read integer value from standard input
	fmt.Scanf("%d", &selection)

	// Output example based on user selection
	switch selection {
		case 1:
			simpleGift()
		case 2:
			thoughtfulGift()
		case 3:
			practicalGift()
		default:
			fmt.Println("Invalid selection.")
	}
}