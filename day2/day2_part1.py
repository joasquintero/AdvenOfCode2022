"""
This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
"""
def file():
    with open('input_part1.txt','r') as file:
        return file.read()

def main():
    x = file()[::2]
    aux = ''
    score    = 0

    dec = [1,2,3]
    ev = [0,3,6]
    #A, X = (1,1)#rock
    #B, Y = (2,2)#paper
    #C, Z = (3,3)#scissors

    for i in range(len(x)):
        if i%2 == 0:
            aux = x[i]
        else:
            if x[i] == "X":#rock
                score += dec[0]
                if aux == "C":#scissors
                    score+=ev[2]
                if aux == "A":#rock
                    score +=ev[1]

            elif x[i] == "Y":#paper
                score += dec[1]
                if aux == "A":#rock
                    score += ev[2]
                if aux == "B":#paper
                    score+=ev[1]

            elif x[i] == "Z":#scissors
                score += dec[2]
                if aux == "B":#paper
                    score += ev[2]
                if aux == "C":#scissors
                    score += ev[1]
    
    print(score)
if __name__ == "__main__":
    main()
