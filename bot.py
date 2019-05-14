def MainMenu():
    inMenu = True
    while inMenu:
        # Print the main menu
        print("Main menu options for EU Parliament 2019 bot:")
        for number, option in allOptions.items():
            print(f'{number}) {option}')
        # Get the user choice and check if it is viable
        try:
            choice = int(input())
        except ValueError:
            print('Invalid choice')
        if choice not in allOptions.keys():
            print('Invalid choice')
        # Get down into the menu tree
        # Election choice tree
        if choice == 1:
            electiondate()
        # Eligibility choice tree
        if choice == 2:
            eligibility()
        # Output the identity if known
        if choice == 3:
            if not known:
                print('Information not yet provided.')
            else:
                print(f'Your nationality is {nationality}, you would be voting in {hostCountry}')

def electiondate():
    # Find out the identity of the person if it is unknown to give the answer.
    if known == False:
        identity()

def eligibility():
    pass

def identity():
    global nationality, hostCountry
    print('To provide you with further information, we would need to find out your nationality, and the country where you would vote.')
    # Get the nationality.
    while nationality not in votingDates.keys():
        print("Please, provide the country name of your citizenship.")
        # Get the nationality input
        nationality = input()
        # If the nationality (country name) is not in the country list, give error.
        if nationality not in votingDates.keys():
            print('Country name input is incorrect.')
            print('Would you like to get the country list? y/n')
            if input() == 'y':
                for country in votingDates.keys():
                    print(country, end=' ')
                print()
    # Get the host country.
    while hostCountry not in votingDates.keys():
        # Ask if the nationality equals hostCountry to possibly make the dialogue shorter
        print('Will you be voting in the country of your citizenship? y/n')
        if input() == 'y':
            hostCountry = nationality
            break
        # If nationality is not the same as the hostCountry, do the same as in nationality.
        print("Please, provide the country name of the country where you would vote.")
        hostCountry = input()
        if hostCountry not in votingDates.keys():
            print('Country name input is incorrect.')
            print('Would you like to get the country list? y/n')
            if input() == 'y':
                for country in votingDates.keys():
                    print(country, end=' ')
                print()
    # Add flag known when the identity is provided fully.
    known = True


# All possible Main Menu options
allOptions = {
    1: 'Get the EU Parliament election date.',
    2: 'Check eligibility to vote in the EU Parliament elections.',
    3: 'My identity.',
    }
# Country names and voting dates
votingDates = {
    'Austria': '26 May 2019',
    'Belgium': '26 May 2019',
    'Bulgaria': '26 May 2019',
    'Croatia': '26 May 2019',
    'Cyprus': '26 May 2019',
    'Czech Republic': '24-25 May 2019',
    'Denmark': '26 May 2019',
    'Estonia': '26 May 2019',
    'Finland': '26 May 2019',
    'France': '26 May 2019',
    'Germany': '26 May 2019',
    'Greece': '26 May 2019',
    'Hungary': '26 May 2019',
    'Ireland': '24 May 2019',
    'Italy': '26 May 2019',
    'Latvia': '25 May 2019',
    'Lithuania': '26 May 2019',
    'Luxembourg': '26 May 2019',
    'Malta': '25 May 2019',
    'The Netherlands': '23 May 2019',
    'Poland': '26 May 2019',
    'Portugal': '26 May 2019',
    'Romania': '26 May 2019',
    'Slovakia': '25 May 2019',
    'Slovenia': '26 May 2019',
    'Spain': '26 May 2019',
    'Sweden': '26 May 2019',
    'United Kingdom': '23 May 2019'
    }

# Starting flags
nationality = None
hostCountry = None
known = False

if __name__ == '__main__':
    MainMenu()