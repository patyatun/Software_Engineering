# Software Engineering
## Our Coffee

This project is the first version of the management system for Our Coffee. 
The main goal is to create a user friendly tool for recording and managing the orders.
The project was developed covering the points proposed in class.

### System description

### Programming language
The system is being developed in Python using the tkinter library due to its simplicity and my personal experience.

### GitHub repository
The complete source and documentation can be found in the following GitHub Repository: https://github.com/patyatun/Software_Engineering.git

### Requirements
- Python 3.x
- Tkinter (usually included in standard Python installations)

### Execution instructions
1. Clone or download the repository to your local machine.
2. Make sure you have Python 3.x installed on your system.
3. Run the Coffee.py file to start.
4. Select the desired quantity of each type of beverages.
5. Click the "Total" button to get the total order cost.
6. Click the "Receipt" button to get the receipt with the details.
7. Optionally, click the "Save" button to save the order receipt to a text file.
   

### 1. Git
Before this project, I had only used GitHub's website for simple tasks like creating repositories, making commits and opening pull requests. This project was my first time using Git on my computer, which helped me understand version control better. I now feel more confident in managing bigger projects with Git.

For this project, I used Git to manage my code and track changes. I also have integrated draw.io with GitHub to directly add and manage diagrams from there. Morever, I connected SonarCloud with GitHub to perform a review of the metrics.
You cand find the details of how I used Git here: [1. GIT](https://github.com/patyatun/Software_Engineering/tree/main/1.%20Git)

### 2. UML
You can find the details here: [2. UML](https://github.com/patyatun/Software_Engineering/tree/main/2.%20UML)
1. Use-Case diagram: I created this diagram to represent the different interactions between users (actors) and the system. Also to visualize additional funtionalities beyond what is currently implemented in my code. It serves as a draft for a more advanced system.
2. Sequence diagram: The diagram shows the different interactions between the user (employee) and the actions.
3. Class diagram: I did this diagram using gleek.io to show how are related the different classes and their elements.
   
### 3. DDD
### 4. Metrics
### 5. Clean Code Development
I've created a cheat sheet outlining the principles of how to write clean code and make a concious effort to follow this guideline while writing my code. You can find the cheat sheet here: [4. Clean Code Development](https://github.com/patyatun/Software_Engineering/tree/main/4.%20Clean%20Code%20Development)

### 6. Build Management
### 7. Unit tests
I included unit tests to ensure the proper functioning of the Coffee.py file. You can find them in the file [test_Coffee.py](https://github.com/patyatun/Software_Engineering/blob/main/test_Coffee.py)

*test_save*: This test verifies the functionality of the save() function. It uses the patch decorator to simulate calls to external functions like filedialog.asksaveasfile and messagebox.showinfo. Then it checks if the save() function is able to correctly write to a simulated file and show an information message.

*test_receipt*: This test verifies the receipt() function, which should generate a receipt with totals for tea, non-coffee, and coffee. Values are set for the totals, and then it checks if the generated receipt content correctly contains the expected totals.

*test_grantotal*: This test evaluates the grantotal() function, which calculates the total costs of the different items in your coffee shop. Text inputs for each beverage are simulated, grantotal() is executed, and then the calculations against expected values are verified.

I runned the tests and they all passed successfully. 
![image](https://github.com/patyatun/Software_Engineering/assets/78238491/b9c28106-ecbf-4f01-bbdc-9062aba696de)

### 8. Continuous delivery: Pipeline
### 9. IDE
I utilize Visual Studio Code for this project due to my prior experience with it in other classes, such as Big Data. I find Visual Studio Code to be very user friendly and efficient, which made it my preferred choice over NetBeans, another IDE I had used previously. Some of my favorite key shortcuts in Visual Studio Code are:

- **Ctrl + L**: to clear the console.
- **cmd + B**: to open the sidebar.
- **cmd + /**: to comment or uncomment the selected lines of code.
- **cmd + Shift + P**: to open the command palette.
- **cmd + Shift + F**: to open the search across files.
- **cmd + P**: to quickly open files by name.
- **cmd + J**: toggles the panel (output, terminal, debug console)
- **cmd + Shift + O**: display a list of symbols (functions, classes, variables) in the current file.

### 10. DSL
### 11. Functional programming
