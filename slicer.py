# get user email
email = input('Quel est ton E-mail?').strip()
# get username by slicing up to @
username = email[:email.find('@')]
# get domain name by slicing from @+1
domain = email[email.find('@')+1:]
# create formatted output string
output = 'Your username is {0} and your domain is {1}'.format(username, domain)
# print formatted output
print(output)
