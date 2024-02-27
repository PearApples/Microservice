Test program is also included in the repository

How to REQUEST data:
  user will be prompted to enter positive values into the text file
  data entered into the text file will be in the form of “x y”, which is x and y coordinate pairs separated by a space, specifically. Each pair will be generated on a separate newline.
  The microservice reads all of the x, y pairs from the text file and separates them into lists of x and y pairs via a delimiter function, which matplotlib then uses to plot the points onto a line graph.

How to RECEIVE data:
  In order for new coordinate pairs to be generated to be displayed on the graph, the program (or test program) must be running at the same time as the microservice. 
  Users will be prompted to either add a new safety rating in the form of a positive number, or be asked if they want to exit the program.

![UML_Diagram](https://github.com/PearApples/Microservice/assets/85377002/48aa7be7-37a0-4c15-9ed8-f0e00b47cc2a)

