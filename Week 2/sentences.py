"""
Welcome to Week 02, Project 02: Writing Functions.
We were asked to make a program that will randomly generate a sentence.
We were supposed to make functions that will take lists of words and then randomly choose a word from each list and return a sentence.
We display a sentence for each quantity (singular or plural) and tense (present, past, or future), so six sentences total to be printed.
"""

# ///

# Additions for this assignment: I followed the Exceeding the Requirements steps in the assingment by calling the function get_prepositional_phrase,
# so that each sentence includes two prepositional phrases.
# I make the function get_adjective and get_adverb and I called them in the function make_sentence. So now each sentence includes an adjective and an adverb.
# I also added an option for the user to continue the program by prompting the user if they want more sentences, and if they do the program
# will randomly choose new senteces. The whole program will continue to loop until the user chooses to quit the program.
# The last thing I added was an introduction of the program to the grader (just above) and then to the user (just bellow)
# 
#  explaining
# what we were asked to do and to the user how to use the program and what the user should expect from the program.

# ///

"""
Hello there! Welcome to the Random Sentence Generator!
We will made a program that will randomly generate a sentence. We have a list of words that will be used to make the sentence.
We will display a sentence for each quantity (singular or plural) and tense (present, past, or future), 
so six sentences total to be printed.
This program will choose the words randomly from the lists of nouns, verbs, adjectives, adverbs, and prepositions.
Each sentence contains two prepositional phrases. Some of the sentences might not make sense, 
but that's okay! Because what matters is that the program works correctly and it's hilarious to read!
By default, the program will generate six sentences, but you will be asked if you want to generate more. Feel free to continue
generating more sentences, but if you don't want to, just say "no" and the program will end.
Enjoy the program!
"""

import random

def main():
  print(make_sentence(1, "past"))
  print(make_sentence(1, "present"))
  print(make_sentence(1, "future"))
  print(make_sentence(2, "past"))
  print(make_sentence(2, "present"))
  print(make_sentence(2, "future"))
  loop_main()

def get_determiner(quantity):
  """Return a randomly chosen determiner. A determiner is
  a word like "the", "a", "one", "some", "many".
  If quantity is 1, this function will return either "a",
  "one", or "the". Otherwise this function will return
  either "some", "many", or "the".
  Parameter
    quantity: an integer.
    If quantity is 1, this function will return a
    determiner for a single noun. Otherwise this
    function will return a determiner for a plural
    noun.
  Return: a randomly chosen determiner.
  """
  if quantity == 1:
    determiners = ["the", "a", "one"]
  else:
    determiners = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  determiner = random.choice(determiners).capitalize()
  return determiner

def get_adjective():
  """Return a randomly chosen adjective.
  """
  adjectives = ["adorable", "beautiful", "clean", "drab", "elegant", "fancy", "glamorous", "handsome", "long", "magnificent", "plain", "quaint", "sparkling", "ugly"]
  adjective = random.choice(adjectives)
  return adjective

def get_noun(quantity):
  """Return a randomly chosen noun.
  If quantity is 1, this function will
  return one of these ten single nouns:
    "bird", "boy", "car", "cat", "child",
    "dog", "girl", "man", "rabbit", "woman"
  Otherwise, this function will return one of
  these ten plural nouns:
    "birds", "boys", "cars", "cats", "children",
    "dogs", "girls", "men", "rabbits", "women"
  Parameter
    quantity: an integer that determines if
      the returned noun is single or plural.
  Return: a randomly chosen noun.
  """
  if quantity == 1:
    nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
  else:
    nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
  noun = random.choice(nouns)
  return noun

def get_adverb():
  """Return a randomly chosen adverb.
  """
  adverbs = ["abruptly", "quickly", "slowly", "carefully", "easily", "nicely", "excitingly", "beautifully", "soon"]
  adverb = random.choice(adverbs)
  return adverb

def get_verb(quantity, tense):
  """Return a randomly chosen verb. If tense is "past",
  this function will return one of these ten verbs:
    "drank", "ate", "grew", "laughed", "thought",
    "ran", "slept", "talked", "walked", "wrote"
  If tense is "present" and quantity is 1, this
  function will return one of these ten verbs:
    "drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"
  If tense is "present" and quantity is NOT 1,
  this function will return one of these ten verbs:
    "drink", "eat", "grow", "laugh", "think",
    "run", "sleep", "talk", "walk", "write"
  If tense is "future", this function will return one of
  these ten verbs:
    "will drink", "will eat", "will grow", "will laugh",
    "will think", "will run", "will sleep", "will talk",
    "will walk", "will write"
  Parameters
    quantity: an integer that determines if the
      returned verb is single or plural.
    tense: a string that determines the verb conjugation,
      either "past", "present" or "future".
  Return: a randomly chosen verb.
  """
  if tense == "past":
    verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
  elif tense == "present" and quantity == 1:
    verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
  elif tense == "present" and quantity != 1:
    verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
  elif tense == "future":
    verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
  verb = random.choice(verbs)
  return verb

def get_preposition():
  """Return a randomly chosen preposition
  from this list of prepositions:
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"
  Return: a randomly chosen preposition.
  """
  prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
  preposition = random.choice(prepositions)
  return preposition


def get_prepositional_phrase(quantity):
  """Build and return a prepositional phrase composed
  of three words: a preposition, a determiner, and a
  noun by calling the get_preposition, get_determiner,
  and get_noun functions.
  Parameter
    quantity: an integer that determines if the
      determiner and noun in the prepositional
      phrase returned from this function should
      be single or pluaral.
  Return: a prepositional phrase.
  """
  if quantity == 1:
    prepositional_phrase = f"{get_preposition()} {get_determiner(quantity).lower()} {get_noun(quantity)}"
  else:
    prepositional_phrase = f"{get_preposition()} {get_determiner(quantity).lower()} {get_noun(quantity)}"
  return prepositional_phrase


def make_sentence(quantity, tense):
  """Build and return a sentence with four words:
  a preposition, a determiner, a noun, and a verb. The grammatical
  quantity of the determiner and noun will match the
  number in the quantity parameter. The grammatical
  quantity and tense of the verb will match the number
  and tense in the quantity and tense parameters.
  """
  if quantity == 1:
    sentence = f"{get_determiner(quantity)} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)} {get_adverb()} {get_verb(quantity, tense)} {get_determiner(quantity).lower()} {get_adjective()} {get_noun(quantity)} {get_preposition_phrase(quantity)}."
  else:
    sentence = f"{get_determiner(quantity)} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)} {get_adverb()} {get_verb(quantity, tense)} {get_determiner(quantity).lower()} {get_adjective()} {get_noun(quantity)} {get_preposition_phrase(quantity)}."
  return sentence

def loop_main():
  """Ask the user if they want to generate more sentences. 
  Use the answer to determine whether to call the main() function again
  or to end the program.
  """
  answer = 0
  while answer == 0:
    again = input("\nDo you want to generate more sentences? (y/n) ").lower()
    if again == "y":
      # loop main()
      print()
      main()
      answer = 1
    elif again == "n":
      # end program
      print("Goodbye!")
      answer = 1
    else:
      print("Please enter 'y' or 'n'.")
      answer = 0

main()