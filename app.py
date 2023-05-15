import random

gameChoice = random.randint(1,3)

print("Alex's Mad Libs Game!")

adjective = input('Adjective: ')
verb = input('Verb: ')
color = input('color: ')
animal = input('Animal: ')
number = input('Number: ')
name = input('Name: ')
gender = input(name + 's'+' Gender: [m/f]')
food = input('Food: ')
country = input('Country: ')
emotion = input('Emotion: ')

ml1 = "One sunny day, [name] deacided to take a walk in the park. The sky was [adjective] and there were [number] [color] [animal]s roaming around.\nAs they walked, they came across a food stand selling [food] from [country]. They ordered a serving and savored the delicious flavors.\nFeeling satisfied, [name] continued their walk and stumbled upon a beautiful garden. The flowers were in full bloom and the air was filled with the sweet aroma of [food].\nSuddenly, they heard a noise and turned around to see a [animal] running towards them. At first, they were scared, but then they realized that the [animal] just wanted to play.\nFeeling [emotion], [name] played with the [animal] and had a wonderful time. They even took a selfie to remember the moment.\nAs the day came to an end, [name] headed back home with a smile on their face, feeling grateful for the little moments of joy that made their day so special."
ml2 = "One [adjective] morning, [name] woke up feeling [emotion]. They got out of bed and decided to go for a walk in the nearby forest. As they were walking, they spotted a [color] [animal] up ahead.\nFeeling curious, they approached the [animal] and saw that it was [adjective]. Suddenly, the [animal] started to [verb], surprising [name]. But then, [name] realized that the [animal] was just playing and joined in the fun.\nAfter a while, [name] continued their walk and stumbled upon a clearing where they saw a group of [number] [color] [animal]s. The [animal]s were all [adjective] and seemed to be enjoying themselves.\nAs [name] was watching the [animal]s, they felt their stomach grumble and remembered that they had packed some [food] from [country]. They sat down and enjoyed their meal while admiring the beauty of nature around them.\nFeeling [emotion], [name] decided to spend the rest of the day exploring the forest and enjoying the company of the [animal]s. They returned home feeling refreshed and grateful for the experience."
ml3 = "One day, [name] woke up feeling [adjective]. They decided to go for a walk in the park to [verb] and enjoy the [color] scenery.\nAs they walked, they spotted [number] [adjective] [color] [animal]s playing in the grass. It was such a delightful sight that it lifted their mood even more.\nAfter a while, they grew hungry and stopped by a food cart selling [food] from [country]. The [food] was so tasty that they couldn't help but feel grateful for the experience.\nFeeling [emotion], [name] continued their walk until they found themselves at a [adjective] lake where they saw a family of [animal]s swimming. They felt a sense of peace and tranquility wash over them.\nAs they headed back home, [name] couldn't help but reflect on the wonderful day they had. They went to bed feeling grateful for the simple pleasures in life."

if gender == 'm':
    if gameChoice == 1:
        print(ml1.replace('[adjective]', adjective).replace('[verb]', verb).replace('[color]', color).replace('[animal]', animal).replace('[number]', number).replace('[name]', name).replace('[food]', food).replace('[country]', country).replace('[emotion]', emotion).replace('they', 'he').replace('their', 'his'))
    if gameChoice == 2:
        print(ml2.replace('[adjective]', adjective).replace('[verb]', verb).replace('[color]', color).replace('[animal]', animal).replace('[number]', number).replace('[name]', name).replace('[food]', food).replace('[country]', country).replace('[emotion]', emotion).replace('they', 'he').replace('their', 'his'))
    if gameChoice == 3:
        print(ml3.replace('[adjective]', adjective).replace('[verb]', verb).replace('[color]', color).replace('[animal]', animal).replace('[number]', number).replace('[name]', name).replace('[food]', food).replace('[country]', country).replace('[emotion]', emotion).replace('they', 'he').replace('their', 'his'))
if gender == 'f':
    if gameChoice == 1:
        print(ml1.replace('[adjective]', adjective).replace('[verb]', verb).replace('[color]', color).replace('[animal]', animal).replace('[number]', number).replace('[name]', name).replace('[food]', food).replace('[country]', country).replace('[emotion]', emotion).replace('they', 'she').replace('their', 'her'))
    if gameChoice == 2:
        print(ml2.replace('[adjective]', adjective).replace('[verb]', verb).replace('[color]', color).replace('[animal]', animal).replace('[number]', number).replace('[name]', name).replace('[food]', food).replace('[country]', country).replace('[emotion]', emotion).replace('they', 'she').replace('their', 'her'))
    if gameChoice == 3:
        print(ml3.replace('[adjective]', adjective).replace('[verb]', verb).replace('[color]', color).replace('[animal]', animal).replace('[number]', number).replace('[name]', name).replace('[food]', food).replace('[country]', country).replace('[emotion]', emotion).replace('they', 'she').replace('their', 'her'))