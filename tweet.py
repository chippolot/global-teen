import goslate
import random
from settings import *
from find_tweet import get_tweet

gs = goslate.Goslate()

while True:
	src_sentence = get_tweet()
	current_sentence = src_sentence

	num_translations = random.randint(MIN_TRANSLATIONS, MAX_TRANSLATIONS)

	languages = open("languages.txt", "r").read().splitlines()

	for i in range(num_translations):

		src_language = 'en'
		dst_language = random.choice(languages)

		current_sentence = gs.translate(current_sentence, dst_language)
		current_sentence = gs.translate(current_sentence, src_language)

	# if nothing changed, try again
	if src_sentence == current_sentence:
		continue

	print "--------------------------------------"
	print src_sentence
	print "--------------------------------------"
	print current_sentence
	print "--------------------------------------"
	break