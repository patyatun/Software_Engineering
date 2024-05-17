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
You can find the diagrams here: [2. UML](https://github.com/patyatun/Software_Engineering/tree/main/2.%20UML)
1. Use-Case diagram: I created this diagram to represent the different interactions between users (actors) and the system. Also to visualize additional funtionalities beyond what is currently implemented in my code. It serves as a draft for a more advanced system.
2. Sequence diagram: The diagram shows the different interactions between the user (employee) and the actions.
3. Class diagram: I did this diagram using gleek.io to show how are related the different classes and their elements.
   
### 3. DDD
### 4. Metrics
### 5. Clean Code Development
I've created a cheat sheet outlining the principles of how to write clean code and make a concious effort to follow this guideline while writing my code. You can find the cheat sheet here: [4. Clean Code Development](https://github.com/patyatun/Software_Engineering/tree/main/4.%20Clean%20Code%20Development)

### 6. & 8. Build Management & Continuos Delivery

I used GitHub Actions as a continuos integration and deployment (CI/CD) tool, I decided to use this one because allows me to automate custom workflowa directly from my GitHub repository. 

#### Build Management
While developing this project I learned that effective build management is important to ensure maintainable code quality. In this project I used PyInstaller, by adding it to my GitHub Action workflow I automated the process of building and packaging my python app, making it easier to run on different systems.

Additionally, I included unit testing in the build process, ensuring that my code works as expected. The workflow automatically runs the unit tests using *python -m unittest test_Coffee.py* before the build step, catching any potential issues early.

#### Continuous delivery: Pipeline
Continuous delivery is a software development practice that enables the automatic deployment or code changes to production environments. To achieve this, I implemented a continuous delivery pipeline using GitHub Actiones.

Configuring the pipeline was challenging, after several iterations I successfully set up a workflow that automatically build, tests, and deploys my app to GitHub Pages whenever changes are pushed to the repository.

HitHub Pages allows developers to host their projects directly from a GitHub repository. By using it, I can easily share and showcase my development with others, without needing a separate hosting solution.

To see the functionality of my build management and continuos delivery pipeline you can find the configuration file here: [python-app.yml](https://github.com/patyatun/Software_Engineering/tree/main/.github/workflows) and some details here: [6. CI/CD]()

### 7. Unit tests
I included unit tests to ensure the proper functioning of the Coffee.py file. You can find them in the file [test_Coffee.py](https://github.com/patyatun/Software_Engineering/blob/main/test_Coffee.py)

*test_save*: This test verifies the functionality of the save() function. It uses the patch decorator to simulate calls to external functions like filedialog.asksaveasfile and messagebox.showinfo. Then it checks if the save() function is able to correctly write to a simulated file and show an information message.

*test_receipt*: This test verifies the receipt() function, which should generate a receipt with totals for tea, non-coffee, and coffee. Values are set for the totals, and then it checks if the generated receipt content correctly contains the expected totals.

*test_grantotal*: This test evaluates the grantotal() function, which calculates the total costs of the different items in your coffee shop. Text inputs for each beverage are simulated, grantotal() is executed, and then the calculations against expected values are verified.

I runned the tests and they all passed successfully. 


### 9. IDE
I utilized Visual Studio Code for this project due to my prior experience with it in other classes, such as Big Data. I find Visual Studio Code to be very user friendly and efficient, which made it my preferred choice over NetBeans, another IDE I had used previously. Some of my favorite key shortcuts in Visual Studio Code are:

- **Ctrl + L**: to clear the console.
- **cmd + B**: to open the sidebar.
- **cmd + /**: to comment or uncomment the selected lines of code.
- **cmd + Shift + P**: to open the command palette.
- **cmd + Shift + F**: to open the search across files.
- **cmd + P**: to quickly open files by name.
- **cmd + J**: toggles the panel (output, terminal, debug console)
- **cmd + Shift + O**: display a list of symbols (functions, classes, variables) in the current file.

### 10. DSL
As an additional feature to the management system, I implemented a Domain Specific Language to demonstrate how a custom language can be used to define and process the orders in a structured and readable manner. While not directly integrated into the main application, this DSL helped me understand the concept of create a domain specific language.

The DSL is defined using regular expressions using re module in Python. The grammar rules speify the structure of a valid coffee order, consisting of an "Order:" keyword followed by a list of order items. Each order item is composed of a quantity and a product type (Tea, Non-Coffee, or Coffee). The *parse_order* function takes a string representing an order and analizes it according to the defined grammar rules. It then calculates the total cost based on the quantities and corresponding product prices.

By leveraging a DSL, users can express coffee orders in an intuitive way, without having to navigate through a GUI. You can find the code here: [DSL](https://github.com/patyatun/Software_Engineering/blob/main/DSL_Coffee.py)

### 11. Functional programming
Following the guidelines, I wrote a code to apply the principles of functional programming. You can find the file here: [functional_programming.py](https://github.com/patyatun/Software_Engineering/blob/main/Functional_programming.py)

- Only final structures: In the code, the *MenuItem* class is an immutable data structure representing a menu item with a name and price. This ensures that instances of *MenuItem* are final structures, meaning their state cannot be modified after creation.

- Side-effect-free functions: The *filter_menu* and *sort_menu* functions are side-effect-free. They don't modify the original *menu* list but instead return a new filtered or sorted list, respectively. This adheres to the functional programming principle of avoiding side effects.

- Higher-order functions: The *apply_discount* function is a higher-order function because it takes another function (discount_func) as a parameter and applies it to the given price.

- Functions as parameters and return values: The *calculate_total* function takes a list of menu items and an optional discount function as parameters. It also returns the total cost after applying the discount, if provided. This demonstrates the use of functions as parameters and return values.

- Closures/ anonymous functions: The *create_discount_func* function returns a lambda function (an anonymous function) that calculates the discounted price based on the provided discount rate. This lambda function is a closure because it captures and remembers the *discount_rate* value from the enclosing scope.

- Example usage: I demonstrate how these functional programming concepts are applied:
  1. The *filter_menu* function is used to filter the menu based on a category (e.g. "coffee")
  2. The *sort_menu* function is used to sort the filtered menu by price in descending order.
  3. The *calculate_total* function is used to calculate the total cost of an order, with the option to apply different discount functions (student discount, senior discount, or a custom discount created with *create_discount_func*).
 
I was able to understand how to apply programming principles in a practical context. Even if this example is not directly integrated into the main system, it serves as an exercise to apply the principles of functional programming.
