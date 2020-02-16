import webbot
import os
import time
import random
os.system('pip3 install pyautogui')
while True:
	driver = webbot.Browser()
	print("")
	driver.go_to('https://kahoot.it/')
	code = '736765'
	input_elements = driver.find_elements(xpath='//input')
	driver.type(driver.Key.TAB,into=input_elements[0].text)
	driver.type(code)
	driver.type(driver.Key.ENTER,into=input_elements[0].text)
	time.sleep(0.2)
	discname1 = ['saucy', 'momma', 'mecha', 'earth', 'barbed', 'prehistoric', 'old','cosmic', 'metallic', 'neat', 'supa', 'haunted', 'ruthless', 'clueless', 'rough', 'killer', 'spooky', 'retro', 'ancient', 'strange', 'astro', 'baren', 'burned', 'chared', 'crap', 'cranky', 'crummy', 'croaked', 'dead', 'daring', 'drunk', 'droopy', 'dank', 'drowned', 'enraged', 'angry', 'good', 'garnished', 'groaning', 'happy', 'hopeful', 'graceful', 'gentle', 'hairy', 'inteligent', 'intergallactic', 'jelly filled', 'jumping', 'kind', 'limp', 'blind', 'lumpy', 'insane', 'meek', 'nocternal', 'artifcial', 'perfect', 'quirky', 'petty', 'rocky', 'sad', 'sorrowful', 'useless', 'sickly', 'unbeatable', 'zesty', 'acrobatic', 'buttered', 'burpy', ]
	noun = ['chair', 'tortoise', 'fruit', 'paper', 'gecko', 'giraffe', 'mountain', 'boy', 'urinal', 'pencil','toenail', 'pug', 'wrangler', 'garbage', 'tugboat', 'bladder', 'viper', 'chicken', 'gnome', 'slayer', 'apple', 'artichoke', 'butter', 'bladder', 'cat', 'coop', 'carp', 'dome', 'door', 'horse', 'dart', 'fart', 'farie', 'garlic', 'goop', 'gunk', 'guild', 'hoop', 'harp', 'handle', 'house', 'cow', 'cake', 'cookie', 'largo', 'armor', 'bow', 'map', 'mayonaise', 'egg', 'napkin', 'octopus', 'park', 'pancake', 'punk', 'queen', 'rock', 'salmon', 'sock', 'syrup', 'tophat', 'viking', 'hipopotomous']
	discname2 = ['saucy', 'momma', 'mecha', 'earth', 'barbed', 'prehistoric', 'old','cosmic', 'metallic', 'neat', 'supa', 'haunted', 'ruthless', 'clueless', 'rough', 'killer', 'spoopy', 'retro', 'ancient', 'strange', 'astro', 'baren', 'burned', 'chared', 'crap', 'cranky', 'crummy', 'croaked', 'dead', 'daring', 'drunk', 'droopy', 'dank', 'drowned', 'enraged', 'angry', 'good', 'garnished', 'groaning', 'happy', 'hopeful', 'graceful', 'gentle', 'hairy', 'inteligent', 'intergallactic', 'jelly filled', 'jumping', 'kind', 'limp', 'blind', 'lumpy', 'insane', 'meek', 'nocternal', 'artifcial', 'perfect', 'quirky', 'petty', 'rocky', 'sad', 'sorrowful', 'useless', 'sickly', 'unbeatable', 'zesty', 'acrobatic', 'buttered', 'burpy',]
	noun2 = ['chair', 'tortoise', 'fruit', 'paper', 'gecko', 'giraffe', 'mountain', 'boy', 'urinal', 'pencil','toenail', 'pug', 'wrangler', 'garbage', 'tugboat', 'bladder', 'viper', 'chicken', 'gnome', 'slayer', 'apple', 'artichoke', 'butter', 'bladder', 'cat', 'coop', 'carp', 'dome', 'door', 'horse', 'dart', 'fart', 'farie', 'garlic', 'goop', 'gunk', 'guild', 'hoop', 'harp', 'handle', 'house', 'cow', 'cake', 'cookie', 'largo', 'armor', 'bow', 'map', 'mayonaise', 'egg', 'napkin', 'octopus', 'park', 'pancake', 'punk', 'queen', 'rock', 'salmon', 'sock', 'syrup', 'tophat', 'viking', 'hipopotomous',]
	rand1 = random.choice(discname1)
	rand2 = random.choice(noun)
	username = (random.choice(discname2) + ' ' + random.choice(discname1) + ' ' + random.choice(noun) + ' ' + random.choice(noun2))
	input_elements = driver.find_elements(xpath='//input')
	driver.type(driver.Key.TAB,into=input_elements[0].text)
	driver.type(username)
	driver.type(driver.Key.ENTER,into=input_elements[0].text)
while True:
  while True:
    url = driver.get_current_url()
    if url == "https://kahoot.it/v2/gameblock":
      break
  input_elements = driver.find_elements(xpath='//input')
  pick = random.randint (1,4)
  if pick == 1:
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    print("Kahoot.it bot picked: Red")
  if pick == 2:
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    print("Kahoot.it bot picked: Blue")
  if pick == 3:
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    print("Kahoot.it bot picked: Yellow")
  if pick == 4:
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    driver.type(driver.Key.TAB,into=input_elements[0].text)
    print("Kahoot.it bot picked: Green")

  driver.type(driver.Key.ENTER,into=input_elements[0].text)

while True:
  time.sleep(0.000001)