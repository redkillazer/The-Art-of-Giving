import java.util.Scanner;

public class Giving {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in); 

System.out.println("What are your favorite ways of giving? "); 
String answer = scanner.nextLine(); 

System.out.println("The art of giving is about more than just money. It's about making an effort to make someone feel appreciated, special, and loved");

String [] givingMethods = new String [] {"Donating to charity","Volunteering","Making something for someone","Smile and say 'thank you'","Making a charitable donation","Buying someone a gift","Sending a thank you card"};

System.out.println("Some ideas on different ways to give are:");

for (int i = 0; i < givingMethods.length; i++) {
	System.out.println(givingMethods[i]);
}

System.out.println("What do you think is the best form of giving? ");
String bestForm = scanner.nextLine();

System.out.println("It's true that " + bestForm + "is a great form of giving - but there are so many others that can be just as meaningful. It all comes down to the intent and the effort made to make someone else feel appreciated and special");

System.out.println("What ideas do you have on ways to give more meaningfully? ");
String ideas = scanner.nextLine();

System.out.println("That's a great idea! " + ideas + " can be an incredibly meaningful way to show someone how much you care. Other useful ideas could include making a charitable donation, helping someone out with a task, or sending a thank you card. The possibilities are endless!");

System.out.println("Is there anything else you'd like to add about the art of giving? ");
String add = scanner.nextLine();

System.out.println("One of the most powerful things about giving is how it can bring about joy and connection between people. You don't have to spend a lot of money, either- often, a simple gesture or kind word can make all the difference. " + add);

System.out.println("No matter what form of giving you choose, it's important to make sure you're doing it with sincerity and intention. That's the key to the art of giving!");

	}

}