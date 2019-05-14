def MainMenu():
    """The main menu, body of the bot"""
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
                print(
                    f'Your nationality is {nationality}, you would be voting for country {hostCountry}, '
                    f'you age is {age}')


def electiondate():
    """Prints the date of election for the host country of the user.
    Send the user to the identity() function if their identity is not known."""
    # Find out the identity of the person if it is unknown to give the answer.
    if known is False:
        identity()
    # Print the voting date based on the hostCountry
    print(f'The voting date is {votingData[hostCountry]["date"]}')


def eligibility():
    """Checks if the user is eligible to vote.
    Send the user to the identity() function if their identity is not known."""
    # Find out the identity of the person if it is unknown to give the answer.
    if known is False:
        identity()
    # TODO - Add eligibility criteria
    pass


def identity():
    """Gets the identity information of the user.
    Gets nationality, host country, age. When all of this is receives, known variable is set to True."""
    global nationality, hostCountry, age, known
    print(
        'To provide you with further information, we would need to find out your nationality, the country you would '
        'vote and your age.')
    # Get the nationality
    while nationality not in votingData.keys():
        print("Please, provide the country name of your citizenship.")
        nationality = input()
        # If the nationality (country name) is not in the country list, give error.
        # TODO - Make the nationality capitalized upon the check
        if nationality not in votingData.keys():
            print('Country name input is incorrect.')
            print('Would you like to get the country list? y/n')
            if input() == 'y':
                for country in votingData.keys():
                    print(country, end=' ')
                print()
    # Get the host country
    while hostCountry not in votingData.keys():
        # Ask if the nationality equals hostCountry to possibly make the dialogue shorter
        print('Will you be voting in the country of your citizenship? y/n')
        if input() == 'y':
            hostCountry = nationality
            break
        # If nationality is not the same as the hostCountry, do the same as in nationality.
        print("Please, provide the country name of the country where you would vote.")
        hostCountry = input()
        # If the nationality (country name) is not in the country list, give error.
        # TODO - Make the hostCountry capitalized upon the check
        if hostCountry not in votingData.keys():
            print('Country name input is incorrect.')
            print('Would you like to get the country list? y/n')
            if input() == 'y':
                for country in votingData.keys():
                    print(country, end=' ')
                print()
    # Get the age
    print('What will your age be at the date of voting?')
    age = ''
    while not age:
        try:
            age = int(input())
        except ValueError:
            print('Age has to be a number')
    # Add flag known when the identity is provided fully.
    known = True


# All possible Main Menu options
allOptions = {
    1: 'Get the EU Parliament election date.',
    2: 'Check eligibility to vote in the EU Parliament elections.',
    3: 'My identity.',
    }
# Country names and voting dates
votingData = {
    'Austria':
        {
            'date': '26 May 2019',
            'age': 16
            },
    'Belgium':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Bulgaria':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Croatia':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Cyprus':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Czech Republic':
        {
            'date': '24-25 May 2019',
            'age': 18
            },
    'Denmark':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Estonia':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Finland':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'France':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Germany':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Greece':
        {
            'date': '26 May 2019',
            'age': 17
            },
    'Hungary':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Ireland':
        {
            'date': '24 May 2019',
            'age': 18
            },
    'Italy':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Latvia':
        {
            'date': '25 May 2019',
            'age': 18
            },
    'Lithuania':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Luxembourg':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Malta':
        {
            'date': '25 May 2019',
            'age': 16
            },
    'The Netherlands':
        {
            'date': '23 May 2019',
            'age': 18
            },
    'Poland':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Portugal':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Romania':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Slovakia':
        {
            'date': '25 May 2019',
            'age': 18
            },
    'Slovenia':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Spain':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'Sweden':
        {
            'date': '26 May 2019',
            'age': 18
            },
    'United Kingdom':
        {
            'date': '23 May 2019',
            'age': 18
            },
    }

# Starting flags
nationality = None
hostCountry = None
known = False

if __name__ == '__main__':
    MainMenu()
