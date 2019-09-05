import numpy as np
import random as rm

states = ["Bull","Bear","Stagnant"]

transition = [["bubu","bube","bust"],["bebu","bebe","best"],["stbu","stbe","stst"]]
transitionMatrix = [[0.9,0.075,0.025],[0.15,0.8,0.05],[0.25,0.25,0.5]]

if sum(transitionMatrix[0])+ sum(transitionMatrix[1]) + sum(transitionMatrix[2]) != 3:
    print("Error, Mismatch Probability sum.")
else:
    def stock_analysis(days):
        currentstate = "Stagnant"

        stateList = [currentstate]
        i = 0

        prob = 1

        while i != days:
            if currentstate == "Bull":
                change = np.random.choice(transition[0],replace=True,p=transitionMatrix[0])
                if change == "bubu":
                    prob = prob * 0.9
                    stateList.append("Bull")
                elif change == "bube":
                    prob = prob * 0.075
                    currentstate = "Bear"
                    stateList.append("Bear")
                elif change == "bust":
                    prob = prob * 0.025
                    currentstate = "Stagnant"
                    stateList.append("Stagnant")
            elif currentstate == "Bear":
                # transitionMatrix = [[0.9,0.075,0.025],[0.15,0.8,0.05],[0.25,0.25,0.5]]
                change = np.random.choice(transition[1],replace=True,p=transitionMatrix[1])
                if change == "bebu":
                    prob = prob * 0.15
                    stateList.append("Bull")
                elif change == "bebe":
                    prob = prob * 0.8
                    currentstate = "Bear"
                    stateList.append("Bear")
                elif change == "best":
                    prob = prob * 0.05
                    currentstate = "Stagnant"
                    stateList.append("Stagnant")

            elif currentstate == "Stagnant":
                change = np.random.choice(transition[2],replace=True,p=transitionMatrix[2])
                if change == "stbu":
                    prob = prob * 0.25
                    stateList.append("Bull")
                elif change == "stbe":
                    prob = prob * 0.25
                    currentstate = "Bear"
                    stateList.append("Bear")
                elif change == "stst":
                    prob = prob * 0.5
                    currentstate = "Stagnant"
                    stateList.append("Stagnant")

            i += 1

        print("Starting State : " + str(stateList))
        print("After days : "+ str(days) + " current state: " + currentstate)
        print("Probability of the possible sequence states of states : " + str(prob))

stock_analysis(300)
