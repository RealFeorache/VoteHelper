class Votehelper:

    def __init__(self):
        # All possible Main Menu options
        self._all_options = {
            1: 'Get the EU Parliament election date.',
            2: 'Check eligibility to vote in the EU Parliament elections.',
            3: 'My voting options.',
            4: 'My identity.',
            5: 'Erase my information.',
            6: 'Quit.',
            }
        # Country names and voting dates
        self._voting_data = {
            'Austria':
                {
                    'date': '26 May 2019',
                    'age': 16,
                    'withinEU': False
                    },
            'Belgium':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Bulgaria':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': True
                    },
            'Croatia':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Cyprus':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Czech Republic':
                {
                    'date': '24-25 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Denmark':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Estonia':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Finland':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'France':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Germany':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Greece':
                {
                    'date': '26 May 2019',
                    'age': 17,
                    'withinEU': True
                    },
            'Hungary':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Ireland':
                {
                    'date': '24 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Italy':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': True
                    },
            'Latvia':
                {
                    'date': '25 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Lithuania':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Luxembourg':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Malta':
                {
                    'date': '25 May 2019',
                    'age': 16,
                    'withinEU': False
                    },
            'The Netherlands':
                {
                    'date': '23 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Poland':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Portugal':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Romania':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Slovakia':
                {
                    'date': '25 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Slovenia':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Spain':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'Sweden':
                {
                    'date': '26 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            'United Kingdom':
                {
                    'date': '23 May 2019',
                    'age': 18,
                    'withinEU': False
                    },
            }

        self._voting_options = {
            'letters':
                [
                    'Belgium', 'Denmark', 'Germany', 'Estonia', 'Spain', 'Latvia', 'Lithuania', 'Luxembourg',
                    'Hungary', 'The Netherlands', 'Austria', 'Slovenia', 'Finland', 'Sweden', 'United Kingdom'
                    ],
            'embassy':
                [
                    'Belgium', 'Bulgaria', 'Denmark', 'Estonia', 'Greece', 'Spain', 'France', 'Croatia', 'Italy',
                    'Cyprus', 'Latvia', 'Lithuania', 'Hungary', 'The Netherlands', 'Austria', 'Poland', 'Portugal',
                    'Romania', 'Slovenia', 'Sweden'
                    ],
            'proxy':
                [
                    'Belgium', 'France', 'The Netherlands', 'United Kingdom'
                    ],
            'evote':
                [
                    'Estonia'
                    ],
            }
        # Starting flags
        self.EUnational = None
        self.nationality = None
        self.host_country = None
        self.downs_syndrome = None
        self.age = None
        self.known = False
        self.outsideEU = None
        self.eligible = None

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
                if choice not in self._all_options:
                    print('Invalid choice.')
                    continue
            except ValueError:
                print('Invalid choice')
                continue
            # Get down into the menu tree
            # 1 - Election date tree
            if choice == 1:
                self.election_date()
            # 2 - Eligibility choice tree
            elif choice == 2:
                self.eligibility()
            # 3 - Voting options
            elif choice == 3:
                self.voting_options()
            # 4 - Output the identity if known
            elif choice == 4:
                # TODO - Add identity output.
                pass
            # 5 - Erase information
            elif choice == 5:
                self.EUnational = self.nationality = self.host_country = self.downs_syndrome = self.age = \
                    self.outsideEU = self.eligible = None
                self.known = False
                print('All of the information has been successfully erased.')
            # 6 - Quit choice
            elif choice == 6:
                print('Thanks for using Vote Helper!')
                break

    def election_date(self):
        """Prints the date of election for the host country of the user."""
        country = self.get_info_on_country("country name.")
        # Print the voting date based on the country
        print(f'The voting date is {self._voting_data[country]["date"]}')

    def eligibility(self):
        """Checks if the user is eligible to vote.
        Send the user to the identity() function if their identity is not known."""
        # Find out the identity of the person if it is unknown to give the answer.
        if not self.known:
            self.identity()
        # Check age eligibility and Down's syndrome eligibility
        if self.eligible:
            print('You are eligible to vote.')
        else:
            self.give_reason('You aren\'t eligible to vote')

    def give_reason(self, message):
        print(f'{message}, because:')
        # Because non-EU
        if not self.EUnational:
            print('1. You are not an European national.')
        else:
            # Prepare to give multiple reasons
            reasonCounter = 1
            # Because of age
            if self.outsideEU:
                if self.age < self._voting_data[self.nationality]['age']:
                    print(f'{reasonCounter}. You are not old enough.')
                    print(f"Note: The minimum age of voting for your choices is "
                          f"{self._voting_data[self.nationality]['age']}.")
                    reasonCounter += 1
            else:
                if self.age < self._voting_data[self.host_country]['age']:
                    print(f'{reasonCounter}. You are not old enough.')
                    print(f"Note: The minimum age of voting for your choices is "
                          f"{self._voting_data[self.host_country]['age']}.")
                    reasonCounter += 1
            # Because of Down's syndrome
            if self.downs_syndrome:
                print(f'{reasonCounter}. You have down\'s syndrome.')

    def identity(self):
        """Gets the identity information of the user.
        Gets nationality, host country, age, downs syndrome.
        When all of this is receives, known variable is set to True."""
        while not self.known:
            print(
                'To provide you with further information, we would need to find out your nationality, the country you '
                'would vote and your age.')
            # Check if is EU national
            while self.EUnational not in ['y', 'n']:
                print('Are you an EU national? y/n')
                self.EUnational = input().lower()
            if self.EUnational == 'n':
                self.eligible = False
                self.EUnational = False
                self.known = True
                break
            # Get the nationality
            self.nationality = self.get_info_on_country("your nationality.")
            # Get the host country
            while self.host_country not in self._voting_data:
                # Ask if the nationality equals host_country to possibly make the dialogue shorter
                print('Will you be voting in the country of your nationality? y/n')
                same_country = input().lower()
                if same_country == 'y':
                    self.host_country = self.nationality
                    break
                elif same_country == 'n':
                    while self.outsideEU not in ['y', 'n']:
                        print('Will you be voting in another EU country? y/n')
                        self.outsideEU = input().lower()
                        if self.outsideEU == 'n':
                            self.outsideEU = True
                            break
                        elif self.outsideEU == 'y':
                            self.outsideEU = False
                            self.host_country = self.get_info_on_country(
                                "country name of the country where you would vote.")
                            break
                    if self.outsideEU is not None:
                        break
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
            while self.downs_syndrome not in ['y', 'n']:
                print('Do you have down syndrome? y/n')
                self.downs_syndrome = input().lower()
            if self.downs_syndrome == 'y':
                self.downs_syndrome = True
            else:
                self.downs_syndrome = False
            # If doesn't live outside EU, check for the age requirement of the host country and the downs syndrome
            if self.outsideEU:
                if self.age >= self._voting_data[self.nationality]['age'] and not self.downs_syndrome:
                    self.eligible = True
                else:
                    self.eligible = False
            else:
                if self.age >= self._voting_data[self.host_country]['age'] and not self.downs_syndrome:
                    self.eligible = True
                else:
                    self.eligible = False
            # Set known on the completion of the identity information gathering
            self.known = True

    def get_info_on_country(self, message):
        country = None
        while country not in self._voting_data:
            print(f"Please, provide the {message}")
            country = input().title()
            # If the country name is not in the country list, give error.
            self.is_in_country_list(country)
        return country

    def is_in_country_list(self, country_name):
        """Checks if the inputted country is in the country list."""
        while country_name not in self._voting_data:
            print('Country name input is incorrect.')
            print('Would you like to get the country list? y/n')
            get_country_list_choice = input().lower()
            if get_country_list_choice == 'y':
                for country in self._voting_data:
                    print(country, end=', ')
                print()
                break
            elif get_country_list_choice == 'n':
                break

    def voting_options(self):
        """Provides the user with the voting options"""
        # Get identity if the user is not known
        if not self.known:
            self.identity()
        # If not eligible, say that there are no options
        if not self.eligible:
            self.give_reason('You don\'t have options to vote')
        # If is eligible, lives outside of the EU, but the nationality requires to be inside of the EU,
        # give a sophisticated answer.
        elif self.eligible and self.outsideEU and self._voting_data[self.nationality]['withinEU']:
            print('You need to be inside of the EU, as you don\'t have any options outside of the EU.')
            print('If you were to be in the EU, in your home country, you could vote in the voting booth.')
            print('If you were to be in the EU, in not your home country, you could vote in the following ways:')
            self.print_voting_options()
        # If eligible and within the EU send into the self.print_voting_options()
        else:
            print('Your options for voting are:')
            # Get all the options for country and print them.
            self.print_voting_options()

    def print_voting_options(self):
        """Print all the voting options based on self.host_country and self.nationality"""
        # If lives in his home country, say that the user can use a voting booth
        if self.host_country == self.nationality:
            print('Voting booth.')
        # If doesn't live in his home country, give out different options.
        else:
            for option, country in self._voting_options.items():
                if self.nationality in country:
                    print(option.capitalize(), end=', ')
                    # If the user is a national and lives within EU, also add the voting booth option.
                    if not self.outsideEU:
                        print('Voting booth.', end='')
                    print()


Votehelper()
