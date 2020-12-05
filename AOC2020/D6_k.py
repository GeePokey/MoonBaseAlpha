
def readInput():
    with open(r"C:\Users\Kody\GitExperiment\MoonBaseAlpha\AOC2020\D6_kinput.txt", "r",) as f:
    # with open(r"C:\Users\Kody\GitExperiment\MoonBaseAlpha\AOC2020\good.txt", "r",) as f:
        data = f.read().split('\n')
    # input = [list(i) for i in data]
    return data

input = readInput()
print(input)