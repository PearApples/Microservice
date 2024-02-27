import matplotlib.pyplot as plt
import time
# from datetime import datetime
# MAIN MICROSERVICE

def generate_graph(x, y):


    # Create a line chart
    plt.figure(figsize=(10, 5)) # length x width of graph display
    plt.plot(x, y, marker='o', linestyle='-')
    
    # grpah labels
    plt.title('Safety Rating Per Number of Laps')
    plt.xlabel('Number of Laps')
    plt.ylabel('Safety Rating')
    
    plt.grid(True)

    plt.savefig('graph.png')
    plt.show()



def main():
    user_input = int(input("1 to generate a graph, 2 to exit"))

    #TODO: to make this continually run, we can say while (user_input != -1) ?

    while (True):
        if (user_input == 1):
            # get number of lines
            with open("graph.txt", 'r') as line_count:
                for count, line in enumerate(line_count):
                    pass

            x = []
            y = []

            with open('graph.txt') as file:
                for line in file:
                    split = line.split() #split the x,y pairs into their own lists (list = [x, y])
                    x.append(int(split[0]))
                    y.append(int(split[1]))

            generate_graph(x, y)

            user_input = int(input("1 to generate a graph, 2 to exit"))
        elif (user_input == 2):
            open("graph.txt", 'w').close() # clears the text file
            return
        else:
            print("Please try again. Press 1 to generate a graph, or 2 to exit")          


if __name__ == "__main__":
    main()