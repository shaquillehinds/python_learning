# Ask user for their name
name = input("Salut, comment t'appelle?")
# Ask user for their age
age = input("Quel age avez-vous?")
# Ask user for their city
city = input("Où tu habites?")
# Ask user for their hobbies
hobbies = input("Qu'est-ce que tu aimes faire?")
# Create output text
output = "Your name is " + name + " and you are " + age + \
    " years old. You live in " + city + " and you like to " + hobbies
output2 = "Your name is {0} and you are {1} years old. You live in {2} and you like to {3}".format(
    name, age, city, hobbies)
# Print output to screen
print(output2)
