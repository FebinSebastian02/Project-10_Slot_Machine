SLOT_MACHINE

Steps done:-
	- Functions were defined and called.
	- Global constants were defined and used.
	- While loop was used to run the program continuously until the user decides to quit.
	- If else conditions were used to take actions based on user's choice.
	- Dictionary was used to store the symbols and symbol values in a slot machine reel.
	- List was used to store reels of different columns
	- Random module was imported to use the choice function to randomly choose a value from a list.
	- Slice operator was used to copy a list and Splat/Unpack operator was used to fetch all values from a list
	- For loops were used to iterate through rows, columns etc.
	- Datetime module was imported to fetch current date and time
	- A receipt with few details was created which was printed in a text file once the user chooses to quit the game.
	- playsound() is used to add sound effect during slot machine spin

Code Walkthrough:-
	- With the calling of main(), the program starts execution.
	- Inputs are taken from user.
	- credit() takes the amount credited by user to play the game.
	- while loop runs the program continuously until the user decides to quit.
	- In startSpin(), inputs for lines and bet are taken. Also based on conditions, further statements are executed.
	- generateValuesInMachine() is used to fill the symbols in reels.
	- printSlotMachine() prints the screen of Slot machine in console. 
	- checkWinnings() calculates the amount won.
	- Once user decides to quit,getDateTime() fetches the current date and time that needs to be printed in the receipt.
	- printReceipt() prints the receipt into a text file.

Status of the project:- Completed