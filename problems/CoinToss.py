import random


def flippingCoin():
    result = random.randint(0, 1)
    return result


def conductExperiment():
    headCounter = 0
    tailCounter = 0
    for i in range(0, 10):
        result1 = flippingCoin()
        if result1 == 0:
            headCounter = headCounter + 1
        elif result1 == 1:
            tailCounter = tailCounter + 1
    return headCounter, tailCounter


def simulation():
    simulationList = []
    headCounter1 = 0
    tailCounter1 = 0
    for i in range(0, 10):
        headCounter1, tailCounter1 = conductExperiment()
        simulationList.append("Heads: %s Tails: %d" % (headCounter1, tailCounter1))
    for i in range(0, 10):
        print("Experiment",i+1,"-->", simulationList[i])


simulation()
