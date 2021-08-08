SCRABBLE_LETTER_VALUES = {
	'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORDLIST_FILENAME = "words.txt"
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
import random
def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	
	print("Loading word list from file...")
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# wordlist: list of strings
	wordlist = []
	for line in inFile:
		wordlist.append(line.strip().lower())
	print("  ", len(wordlist), "words loaded.")
	return wordlist
	
def get_word_score(word, n):
	score = 0
	if len(word) > 0:
		for char in word:
			score += SCRABBLE_LETTER_VALUES[char]
			print(SCRABBLE_LETTER_VALUES[char])
		score += max((7*len(word)-3*(n-len(word))),1)
		print(max((7*len(word)-3*(n-len(word))),1))
		print(score)
		
def update_hand(hand, word):
	"""
	Does NOT assume that hand contains every letter in word at least as
	many times as the letter appears in word. Letters in word that don't
	appear in hand should be ignored. Letters that appear in word more times
	than in hand should never result in a negative count; instead, set the
	count in the returned hand to 0 (or remove the letter from the
	dictionary, depending on how your code is structured). 

	Updates the hand: uses up the letters in the given word
	and returns the new hand, without those letters in it.

	Has no side effects: does not modify hand.

	word: string
	hand: dictionary (string -> int)    
	returns: dictionary (string -> int)
	"""
	word = str.lower(word)
	new_hand = hand.copy()
	
	for char in word:
		if char in hand:
			if new_hand[char] - 1 < 0:
				new_hand[char] = 0
			else:
				new_hand[char] = new_hand[char] - 1
	
	print(new_hand)
	return new_hand
	
	
def is_valid_word(word, hand, word_list):
	"""
	Returns True if word is in the word_list and is entirely
	composed of letters in the hand. Otherwise, returns False.
	Does not mutate hand or word_list.
   
	word: string
	hand: dictionary (string -> int)
	word_list: list of lowercase strings
	returns: boolean
	"""
	word = str.lower(word)
	hand_copy = hand.copy()
	wildcard_list = []
	if word.find('*') == -1:
		if word in word_list:
			for char in word:
				if char in hand_copy and hand_copy[char] > 0:
					hand_copy[char] = hand_copy[char] - 1 
				else:
					print('1')
					return False
		else: 
			print('2')
			return False
		print('3')
		return True
		
	else:
		for v in VOWELS:
			wildcard_list.append(word.replace('*',v))
		print(len(wildcard_list))
		for i in range(len(wildcard_list)):
			print(i)
			print(wildcard_list[i])
			if wildcard_list[i] in word_list:
				print('its a word, break')
				break
			elif i == len(wildcard_list) - 1:
				print('not a word')
				return False
		for char in word:
			if char in hand_copy and hand_copy[char] > 0:
				hand_copy[char] = hand_copy[char] - 1 
			else:
				print('1')
				return False
		print('wildcard')
		return True	



def calculate_handlen(hand):
	""" 
	Returns the length (number of letters) in the current hand.
	
	hand: dictionary (string-> int)
	returns: integer
	"""
	hand_length = 0
	values = hand.values()
	hand_length = sum(values)
	return hand_length
		
		
def substitute_hand(hand, letter):
	""" 
	Allow the user to replace all copies of one letter in the hand (chosen by user)
	with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
	should be different from user's choice, and should not be any of the letters
	already in the hand.

	If user provide a letter not in the hand, the hand should be the same.

	Has no side effects: does not mutate hand.

	For example:
		substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
	might return:
		{'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
	The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
	already in the hand.
	
	hand: dictionary (string -> int)
	letter: string
	returns: dictionary (string -> int)
	"""
	hand_copy = hand.copy()
	x = letter
	if letter in hand_copy:
		freq = hand_copy.get(letter, 0)
		if letter in VOWELS:
			while x in hand_copy:
				x = random.choice(VOWELS)
				print(x)
			hand_copy[x] = hand_copy.get(x, 0) + freq
		elif letter in CONSONANTS:
			while x in hand_copy:
				x = random.choice(CONSONANTS)
				print(x)
			hand_copy[x] = hand_copy.get(x, 0) + freq
		else:
			print(letter)
			return hand
		del hand_copy[letter]
	else:
		print(hand)
		print(hand_copy)
		return hand
	print(hand_copy)
	return hand_copy
	
wordlist = load_words()
hand = {'e':2,'v':2,'n':1,'i':1,'l':1,'*':1}
word = '*vil'
letter = str(input('Sub, enter a letter'))
substitute_hand(hand,letter)