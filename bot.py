class Votehelper:

    def __init__(self):
        # All possible Main Menu options
        self._all_options = {
            1: 'Get the EU Parliament election date.',
            2: 'Check eligibility to vote in the EU Parliament elections.',
            3: 'My voting options',
            4: 'My identity.',
            5: 'Quit.',
            }
        # Country names and voting dates
        self._voting_data = {
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
        self.nationality = None
        self.host_country = None
        self.downs_syndrome = None
        self.age = None
        self.known = False
        self.abroad = None

        # Initiate the bot
        self.main_menu()

    def main_menu(self):
        """The main menu, body of the bot"""
        while True:
            # Print the main menu
            print("Main menu options for EU Parliament 2019 bot:")
            for number, option in self._all_options.items():
                print(f'{number}) {option}')
            # Get the user choice and check if it is viable
            try:
                choice = int(input())
            except ValueError:
                print('Invalid choice')
            # TODO - deal with the problem of being possibly unreferenced.
            if choice not in self._all_options.keys():
                print('Invalid choice.')
            # Get down into the menu tree
            # 1 - Election date tree
            if choice == 1:
                self.election_date()
            # 2 - Eligibility choice tree
            if choice == 2:
                self.eligibility()
            # 3 - Voting options
            if choice == 3:
                pass
            # 4 - Output the identity if known
            if choice == 4:
                if not self.known:
                    print('Information not fully provided yet.')
                else:
                    if self.downs_syndrome == 'y':
                        print(
                            f'Your country of nationality is {self.nationality}, you would be casting your vote for'
                            f' {self.host_country}, you age is {self.age} and you have Down\'s syndrome.')
                    elif self.downs_syndrome == 'n':
                        print(
                            f'Your country of nationality is {self.nationality}, you would be casting your vote for'
                            f' {self.host_country}, you age is {self.age} and you don\'t have Down\'s syndrome.')
            # 5 - Quit choice
            if choice == 5:
                print('Thanks for using Vote Helper!')
                break

    def election_date(self):
        """Prints the date of election for the host country of the user."""
        while True:
            # Get the host country
            print('Please, provide the country name of you would be casting your vote for.')
            self.host_country = input().title()
            if self.host_country not in self._voting_data:
                self.host_country = None
                print('Not a valid EU country name. Would you like to get the list of EU countries? y/n')
                getlist = input().lower()
                if getlist == 'y':
                    for country in self._voting_data:
                        print(country, end=', ')
                    print()
                if getlist == 'n':
                    print('Would you like to return to the main menu? y/n')
                    if input().lower() == 'y':
                        break
            else:
                # Print the voting date based on the host_country
                print(f'The voting date is {self._voting_data[self.host_country]["date"]}')
                break

    def eligibility(self):
        """Checks if the user is eligible to vote.
        Send the user to the identity() function if their identity is not known."""
        # Find out the identity of the person if it is unknown to give the answer.
        if not self.known:
            self.identity()
        # TODO - Add eligibility criteria.
        pass

    def identity(self):
        """Gets the identity information of the user.
        Gets nationality, host country, age, downs syndrome.
        When all of this is receives, known variable is set to True."""
        while not self.known:
            print(
                'To provide you with further information, we would need to find out your nationality, the country you '
                'would vote and your age.')
            # Check if is EU national
            print('Are you a EU national? y/n')
            national = input().lower()
            if national == 'n':
                print('You are not eligible to vote in the EU parliament elections.')
                break
            # Get the nationality
            while self.nationality not in self._voting_data:
                print("Please, provide the country name of your citizenship.")
                self.nationality = input().title()
                # If the nationality (country name) is not in the country list, give error.
                self.is_in_country_list(self.nationality)
            # Get the host country
            while self.host_country not in self._voting_data:
                # Ask if the nationality equals host_country to possibly make the dialogue shorter
                print('Will you be voting in the country of your citizenship? y/n')
                if input() == 'y':
                    self.host_country = self.nationality
                    break
                # If nationality is not the same as the host_country, do the same as in nationality.
                print("Please, provide the country name of the country where you would vote.")
                self.host_country = input().title()
                # If the nationality (country name) is not in the country list, give error.
                self.is_in_country_list(self.host_country)
            # Get the age
            print('What will your age be at the date of voting?')
            while self.age not in range(0, 151):
                try:
                    self.age = int(input())
                    if self.age not in range(0, 151):
                        print('Age has to be between 0 and 150.')
                except ValueError:
                    print('Age has to be a number between 0 and 150.')
            # Get the down syndrome information
            print('Do you have down syndrome? y/n')
            self.downs_syndrome = input()
            while self.downs_syndrome.lower() not in ['y', 'n']:
                print('Do you have down syndrome? y/n')
                self.downs_syndrome = input()
            # Check if the user lives outside of EU
            print('Do you live outside of the EU? y/n')
            self.abroad = input().lower()
            while self.abroad.lower() not in ['y', 'n']:
                print('Do you live outside of the EU? y/n')
                self.abroad = input()
            # Add flag known when the identity is provided fully.
            self.known = True

    def is_in_country_list(self, country_name):
        """Checks if the inputted country is in the country list."""
        if country_name not in self._voting_data:
            print('Country name input is incorrect.')
            print('Would you like to get the country list? y/n')
            if input().lower() == 'y':
                for country in self._voting_data:
                    print(country, end=', ')
                print()

    def voting_options(self):
        """Provides the user with the voting options"""
        if not self.known:
            self.identity()
        print('Your options for voting are:')
        for options, availability in self._all_options[self.nationality]['options']:
            if availability is True:
                print(options, end=', ')

Votehelper()
