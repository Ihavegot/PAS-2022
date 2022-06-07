import requests

data = {
    'custname': '',
    'custtel': '',
    'size': '',
    'custemail': '',
    'topping': '',
    'delivery': '',
    'comments': '',
}

# Customer name
data['custname'] = input('Customer name: ')

# Customer phone
data['custtel'] = input('Customer phone: ')

# Customer email
data['custemail'] = input('Customer email: ')

# Pizza size
sizes = {
    's': 'small',
    'm': 'medium',
    'l': 'large'
}
print('Avalible sizes\ns - small\nm - medium,\nl - large\n')
while True:
    which_size = input('Pizza size: ')
    if which_size in sizes:
        data['size'] = sizes[which_size]
        break

# Pizza toppings
topping = {
    'b': 'bacon',
    'c': 'extra cheese',
    'o': 'onion',
    'm': 'mushroom',
}
choosen_toppings = []
print('Avalible toppings\nb - bacon\nc - extra Cheese,\no - onion\nm - mushroom\nType q to end choosing toppings\n')
while True:
    which_topping = input('Add topping: ')
    if which_topping not in choosen_toppings and which_topping in topping:
        choosen_toppings.append(topping[which_topping])
    if which_topping == 'q':
        data['topping'] = choosen_toppings
        break

# Delivery time
hour = input("Hour: ")
minute = input("Minute: ")

data['delivery'] = f'{hour}:{minute}'

# Delivery info
data['comments'] = input('Comments: ')

res = requests.post('https://httpbin.org/post', data=data)
print(res.text)
