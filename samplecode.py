import random

import discord


voting_data = {
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
voting_options = {
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

TOKEN = 'NTgxMTM2MjEwMTY0OTczNTgx.XOa3bg.ho7aMEIDEL2gHCHWvRgwOuumbRQ'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Welcome the user if needed.
    if message.content.startswith('!hello'):
        await message.channel.send(f'I heard you, {message.author.display_name}!')

    # Coinflip
    if message.content.startswith('!coinflip'):
        if random.randint(0, 1) == 0:
            await message.channel.send('Heads!')
        else:
            await message.channel.send('Tails!')

    # Eligibility + Options command
    if message.content.startswith('!elections'):
        # Create a list from user input, exclude the !elections, as it is not needed further
        userinput = message.content.split()[1:]
        # Create variables based on user parameters. Titles for country names and lower for downs status
        nationality, hostcountry = userinput[0].title(), userinput[1].title()
        agestr, downs = userinput[2], userinput[3].lower()
        # Create an advice that will be repeated multiple times
        advice = ('Please use the following command structure:\n'
                  '!elections y/n Citizenship Host-Country Age y/n')
        # Start the identity check, create False variables for future to avoid unassignment.
        ageEligible, downsEligible, EUeligible = False, False, False
        # Check if the user has gives enough parameters for the command
        if len(userinput) != 4:
            await message.channel.send(f"To use the elections module, you need to provide the following information: \n"
                                       f"Nationality, Host Country, Age, Down's Syndrome Presence.\n"
                                       f"{advice}")
        # If enough variables are given, start the identity check
        else:
            try:
                # Check if the age is a number
                age = int(agestr)
                # Check if the nationality is in the list of EU countries
                if nationality not in voting_data:
                    await message.channel.send(
                        'You are not eligible to vote, as you are not an EU national or you have input the wrong '
                        'country for nationality.')
                    EUeligible = False
                else:
                    EUeligible = True
                if hostcountry not in voting_data and voting_data[nationality]['withinEU']:
                    # TODO - Add eligible without options
                    await message.channel.send('Given your nationality, you are only allowed to vote inside the EU.')
                # Check if the age is in the range of 0 and 150
                if age in range(0, 151):
                    # If the age in range, check if the age is higher than required by the nationality
                    if age >= voting_data[nationality]['age']:
                        ageEligible = True
                else:
                    # If age not in range of 0 and 150, print below
                    await  message.channel.send('Age has to be a number between 0 and 150.')
                # Check the down's syndrome status
                if downs in ['y', 'yes']:
                    downsEligible = False
                elif downs in ['n', 'no']:
                    downsEligible = True
                else:
                    await  message.channel.send(advice)
            # If the age is not a number, say that to the user
            except ValueError:
                await message.channel.send(f'Age has to be a number between 0 and 150. \n{advice}')
        # Provide options if the user is eligible
        if ageEligible and downsEligible and EUeligible:
            await  message.channel.send('You are eligible to vote, here are your options: ')
            # If in the your country
            if hostcountry == nationality:
                if nationality in voting_options['letters']:
                    await message.channel.send('Voting booth and letter.')
                else:
                    await message.channel.send('Voting booth.')
            # If user lives in a country other than the nationality
            else:
                for option, country in voting_options.items():
                    if nationality in country:
                        await message.channel.send(option.title())
        # If not passed the eligibility, exit.
        else:
            await  message.channel.send('Sorry, you are not eligible to vote due the reasons above.')

    # Elections date command
    if message.content.startswith('!electiondate'):
        if message.content.split()[1].title() not in voting_data:
            await message.channel.send('Not a valid EU nation.')
        else:
            await message.channel.send(voting_data[message.content.split()[1].title()]['date'])


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
