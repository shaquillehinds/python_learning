# Ask user for their name
name = input("Salut, comment t'appelle?").strip()
# Ask user for their age
age = input("Quel age avez-vous?").strip()
# Ask user for their city
city = input("Où tu habites?").strip()
# Ask user for their hobbies
hobbies = input("Qu'est-ce que tu aimes faire?").strip()
# Create output text
output = "Your name is " + name + " and you are " + age + \
    " years old. You live in " + city + " and you like to " + hobbies
output2 = "Your name is {0} and you are {1} years old. You live in {2} and you like to {3}".format(
    name, age, city, hobbies)
# Print output to screen
print(output2)
