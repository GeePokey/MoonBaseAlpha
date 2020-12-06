


def readInput():
    with open(r"C:\Users\Kody\GitExperiment\MoonBaseAlpha\AOC2020\D1_input.txt", "r",) as f:
        data = f.read().split('\n')
    data = convertToInts(data)
    return data
def convertToInts(list_to_convert):
    return [int(i) for i in list_to_convert]


input = readInput()

def bruteforcep1(input,p2=0):
    for i in input:
        for j in input[input.index(i):]:
            if p2 == 1:
                for k in input[input.index(j):]:
                    if i + j + k == 2020:
                        print(f"i+j+k=result {i, j, k, i + j + k}")
                        print(f"Success?! Result: {i * j * k}")
            else:
                if i + j == 2020:
                    print(f"i+j=result {i, j, i + j}")
                    print(f"Success?! Result: {i * j}")


bruteforcep1(input)
bruteforcep1(input,1)