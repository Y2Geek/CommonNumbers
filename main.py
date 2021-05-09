import fileio

# Read in the called numbers from called_numbers.txt
contents = fileio.read_contents("called_numbers.txt")

# Perform inital set up
main_numbers = []
bonus_ball = []

for i in range(0, 40):
    # Create a list with 39 indexes with value 0
    main_numbers.append(0)

for i in range(0, 15):
    # Create a list with 39 indexes with value 0
    bonus_ball.append(0)

# Take each line, and for each number add 1 to the matching index
if contents:
    for line in contents:
        numbers = line.split('\t')

        # Ignore first index of numbers as it is a date
        for number in numbers[1:6]:
            number = int(number)
            main_numbers[number] += 1
        
        # The last number will be the bonus ball
        number = int(numbers[6])
        bonus_ball[number] += 1

main_results= []
bonus_results = []

for i in range(1,40):
    main_results.append(f"{main_numbers[i]} times for {i}")

for i in range(1,15):
    bonus_results.append(f"{bonus_ball[i]} times for {i}")

# Save all results in reverseorder based on number of calls
all_results = [f"There were {len(contents)} draws counted\n\n","Main Numbers\n"]

for result in sorted(main_results, reverse=True):
    all_results.append(result)

all_results.append("\n\nBonus Ball\n")

for result in sorted(bonus_results, reverse=True):
    all_results.append(result)

fileio.write_list_to_file("results.txt", all_results)