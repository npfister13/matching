import random


def main():
    print("Matching game. Match the cards to win.")

    down_cards = []
    empty_cards = []
    max_cards = 10
    added = 0
    for i in range(0, max_cards):
        down_cards.append('[]')
    cards = create_cards(empty_cards, max_cards, added)

    matched = False

    # continues until all matched
    while matched is not True:
        print_cards(down_cards)
        print("")
        first_choice = check_first(max_cards)
        print("")
        if down_cards[first_choice - 1] == '[]':
            down_cards[first_choice - 1] = str(cards[first_choice - 1])
            print_cards(down_cards)
            print("")
            print("Choose which card to match with.")
            second_choice = check_second(max_cards, first_choice, down_cards)
            if cards[second_choice - 1] == cards[first_choice - 1]:
                down_cards[second_choice - 1] = str(cards[second_choice - 1])
                print("Cards matched!")
            else:
                down_cards[second_choice - 1] = str(cards[second_choice - 1])
                print_cards(down_cards)
                print("")
                print("Cards did not match.\n")

                down_cards[second_choice - 1], down_cards[first_choice - 1] = '[]', '[]'
        else:
            print("already flipped")
        matched = check_if_solved(cards, down_cards)
    print_cards(cards)
    print("You win!")


def check_if_solved(cards, down_cards):
    for i in range(len(down_cards)):
        try:
            down_cards[i] = int(down_cards[i])
        except ValueError:
            pass

    if cards == down_cards:
        return True
    else:
        return False


# check first card input
def check_first(max_cards):
    while True:
        try:
            choice = int(input("> "))
        except ValueError:
            print("Please enter a number.")
        else:
            if choice > max_cards or choice <= 0:
                print("Invalid number. Please enter a number above 0 and below max cards {}.".format(max_cards))
            else:
                return choice


# check second card input
def check_second(max_cards, first_choice, down_cards):
    while True:
        try:
            choice = int(input("> "))
        except ValueError:
            print("Please enter a number.")
        else:
            if choice == first_choice:
                print("You're already looking at that card!")
            elif choice > max_cards or choice <= 0:
                print("Invalid number. Please enter a number above 0 and below max cards {}.".format(max_cards))
            elif down_cards[choice] != "[]":
                print("You've already flipped that card!")
            else:
                return choice


def print_cards(down_cards):
    for i in range(len(down_cards)):
        print(" {}".format(down_cards[i]), end="")


def create_cards(cards, max_cards, added):
    while added != max_cards / 2:
        rand = random.randint(1, 15)
        if rand not in cards:
            cards.append(rand)
            cards.append(rand)
            added += 1
    random.shuffle(cards)
    return cards


main()
