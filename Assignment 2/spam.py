#Program to generate personalised a spam message using user input
#Fulufhelo Mulaudzi
#28 February 2024

first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money_sum = int(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

print(f'''
Dearest {first_name}
It is with a heavy heart that I inform you of the death of my father,
General Fayk {last_name}, your long lost relative from Mapsfostol.
My father left the sum of {money_sum}USD for us, your distant cousins.
Unfortunately, we cannot access the money as it is in a bank in {country}.
I desperately need your assistance to access this money.
I will even pay you generously, 30% of the amount - {money_sum*3/10}USD,
for your help.  Please get in touch with me at this email address asap.
Yours sincerely
Frank {last_name}''')