# 使用break跳出循环

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city != 'quit':
        print("I'd love to go to " + city.title() + "!")
    else:
        break
