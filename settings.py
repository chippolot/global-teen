import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

MIN_TRANSLATIONS=2
MAX_TRANSLATIONS=4
DEBUG=True