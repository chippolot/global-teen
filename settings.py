import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

NUM_TRANSLATIONS=3
DEBUG=False
CHANCE = 0.25