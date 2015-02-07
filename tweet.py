import goslate
import random
import sys
from settings import *
from find_tweet import get_tweet, connect

if __name__ == "__main__":

	if random.random() > CHANCE:
		print "not tweeting this time"
		sys.exit()

	api = connect()
	gs = goslate.Goslate()

	while True:

		# get a random tweet
		src_sentence = get_tweet(api)
		current_sentence = src_sentence

		# start out in english
		src_language = 'en'

		# get a list of supported languages to translate between
		languages = open("languages.txt", "r").read().splitlines()

		# translate to a bunch of different languages
		for i in range(NUM_TRANSLATIONS):
			dst_language = random.choice(languages)
			current_sentence = gs.translate(current_sentence, dst_language)

		# translate back to source language
		current_sentence = gs.translate(current_sentence, src_language)

		# if nothing changed, try again
		if src_sentence == current_sentence:
			continue

		print "--------------------------------------"
		print src_sentence
		print "--------------------------------------"
		print current_sentence
		print "--------------------------------------"

		if DEBUG == False:
			api.PostUpdate(current_sentence)

		sys.exit()