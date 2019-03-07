def select_cards(possible_cards, hand):
    counter = 0
    while counter <= len(possible_cards):
        for index, current_card in enumerate(possible_cards, 0):
            if index == counter:
                print("Do you want to pick up {}?".format(current_card))
                answer = input()
                if answer.lower() == 'y':
                    hand.append(current_card)
                    counter += 1
                else:
                    counter += 1
                    continue
        return hand


available_cards = ['queen of spades', '2 of clubs', '3 of diamonds', 'jack of spades', 'queen of hearts']

new_hand = select_cards(available_cards, [])

display_hand = "\n".join(new_hand)

print("Your new hand is: \n{}".format(display_hand))
