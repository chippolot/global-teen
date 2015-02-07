import goslate
import random
from settings import *

gs = goslate.Goslate()

source_sentence = "Someone tell my brother to get a less testicular travel pillow"
current_sentence = source_sentence

num_translations = random.randint(MIN_TRANSLATIONS, MAX_TRANSLATIONS)

languages = open("languages.txt", "r").read().splitlines()

for i in range(num_translations):

	src_language = 'en'
	dst_language = random.choice(languages)

	current_sentence = gs.translate(current_sentence, dst_language)
	current_sentence = gs.translate(current_sentence, src_language)

	print current_sentence