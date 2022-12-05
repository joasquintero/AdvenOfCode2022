"""
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

"""




def file():
    with open('input_part2.txt','r') as file:
        x = file.read()
        return x

def main():
    x = file()
    pack = x.split("\n")
    result = 0
    d = {}
    counter = 0
    aux = []
    for i in pack:
        if i == '':
            counter+= 1
            result = 0
        else:
            result = int(result) + int(i)
            d[counter] = result

    for _,v in d.items():
        aux.append(v)

    print(sum(sorted(aux, reverse=True)[:3]))

if __name__ == "__main__":
    main()
