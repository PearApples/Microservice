# Test file to see if the microservice is running!
# enter in dummy values, writes them to the graph.txt
import random
import time

def main():

    # example call
    test_x = [1,2,3,4,5,6,7,8,9,10]
    test_y = [5,10,15,20,15,30,22,24,25]
    user_input = int(input("Add safety rating: , -1 to stop"))

    while user_input > 0:
        test_x.append(test_x[-1] + 1)
        test_y.append(user_input)

        # writes input as (x, y) coordinate pairs to a newline in the text file
        text_file = open("graph.txt", 'w+')
        for i in range(0, len(test_x) - 1):
            text_file.writelines(f"{test_x[i]} {test_y[i]}\n")
        print(len(test_x))
        text_file.close()

        # print for testing purposes
        text_file = open("graph.txt", 'r')
        print(text_file.readlines())
        text_file.close()

        # skill rating to be fed by the program
        user_input = int(input("Add safety rating: , -1 to stop"))

    return

if __name__ == ("__main__"):
    main()