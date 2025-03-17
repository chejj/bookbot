def get_num_words(filepath):
	with open(filepath) as f:
		book_contents = f.read()
		word_list = book_contents.split()
		return len(word_list)

def get_letter_count(filepath):
	char_dict = {}
	with open(filepath) as f:
		book_contents = f.read().lower()
		for c in book_contents:
			if c not in char_dict:
				char_dict[c] = 1
			else:
				char_dict[c] += 1
	return char_dict

def sort_letter_count(filepath):
	unsorted_dict = get_letter_count(filepath)
	sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True))
	return sorted_dict
