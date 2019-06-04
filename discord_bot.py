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
    'Netherlands':
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
            'Hungary', 'Netherlands', 'Austria', 'Slovenia', 'Finland', 'Sweden', 'United Kingdom'
            ],
    'embassy':
        [
            'Belgium', 'Bulgaria', 'Denmark', 'Estonia', 'Greece', 'Spain', 'France', 'Croatia', 'Italy',
            'Cyprus', 'Latvia', 'Lithuania', 'Hungary', 'Netherlands', 'Austria', 'Poland', 'Portugal',
            'Romania', 'Slovenia', 'Sweden'
            ],
    'proxy':
        [
            'Belgium', 'France', 'Netherlands', 'United Kingdom'
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
    elif message.content.startswith('!hello'):
        await message.channel.send(
            f"I heard you, {message.author.display_name}, I'm here! Use !help to understand how to use me to the "
            f"fullest!.")

    # Help command for the bot (instructions)
    elif message.content.startswith('!help'):
        # TODO - Add a proper !help command
        advice = "XXXXXXXXXX"
        await message.channel.send(advice)

    # Eligibility + Options command
    elif message.content.startswith('!elections'):
        # Create a list from user input, exclude the !elections, as it is not needed further
        # TODO - Solve problem when the country name has two words (two parameters are created)
        user_input = message.content.split()[1:]
        # Start the identity check, create False variables for future to avoid unassignment.
        age_eligible = downs_eligible = eu_eligible = correct_input = False
        # Check if the user has gives enough parameters for the command
        if len(user_input) != 4:
            await message.channel.send(
                "The input is incorrect. Please use !help to get the information on how to use the bot.")
        # If enough variables are given, start the identity check
        else:
            reason_counter = 1
            correct_input = True
            # Create variables based on user parameters. Titles for country names and lower for downs status
            nationality, host_country, agestr, downs = [info.title() for info in user_input]
            try:
                # Check if the age is a number
                age = int(agestr)
                # Check if the nationality is in the list of EU countries
                if nationality not in voting_data:
                    await message.channel.send(f'#{reason_counter} You are not an EU national.')
                    reason_counter += 1
                else:
                    eu_eligible = True
                # Check if the age is in the range of 0 and 150
                if age in range(0, 151):
                    # If the age in range, check if the age is higher than required by the nationality
                    if eu_eligible:
                        if age >= voting_data[nationality]['age']:
                            age_eligible = True
                        else:
                            await message.channel.send(f'#{reason_counter} You are not eligible by age.')
                            reason_counter += 1
                    else:
                        await message.channel.send(
                            f'#{reason_counter} It is unknown if you are eligible by age as you are not an EU '
                            f'national.')
                        reason_counter += 1
                else:
                    # If age not in range of 0 and 150, print below
                    await message.channel.send(
                        f'#{reason_counter} Your age is outside the bounds of possibilities (0-150).')
                    reason_counter += 1
                # Check the down's syndrome status
                if downs in ['N', 'NO']:
                    downs_eligible = True
                elif downs in ['Y', 'YES']:
                    await message.channel.send(f"#{reason_counter} You have Down's syndrome.")
                    reason_counter += 1
                else:
                    await message.channel.send("The input for the Down's syndrome is incorrect. Please use !help.")
            # If the age is not a number, say that to the user
            except ValueError:
                await message.channel.send(
                    'Age has to be a number between 0 and 150. If you are not sure of how to use the bot, '
                    'please use !help.')
        # Provide options if the user is eligible
        if age_eligible and downs_eligible and eu_eligible:
            await message.channel.send('You are eligible to vote, here are your options:')
            # If in the your country
            if host_country == nationality:
                if nationality in voting_options['letters']:
                    await message.channel.send('Voting booth and letter.')
                else:
                    await message.channel.send('Voting booth.')
            # If user lives in a country other than the nationality
            else:
                if host_country not in voting_data and voting_data[nationality]['withinEU']:
                    await message.channel.send(
                        'Given your information, you have no options to vote if you reside outside of the EU. These '
                        'would be your options if you lived in a EU country other than your home country.')
                optioncounter = 1
                for option, country in voting_options.items():
                    if nationality in country:
                        await message.channel.send(f'#{optioncounter} - {option.title()}.')
                        optioncounter += 1
        # If not passed the eligibility, exit.
        else:
            if correct_input:
                await message.channel.send('Sorry, you are not eligible to vote due the reasons above.')

    # Elections date command
    elif message.content.startswith('!electiondate'):
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
