class fibonacciCounter:
    def __init__(self):
        print("Initialising fibonacciCounter...")

    def counter(self, amount, display):
        fibList = [0, 1]
        for i in range(amount):
            fibList.append(fibList[-2] + fibList[-1])
        if display == "all":
            return ' '.join(map(str, fibList[1:]))
        elif display == "position":
            return fibList[-1]
