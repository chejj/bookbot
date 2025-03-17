from stats import get_num_words, get_letter_count

def main():
	book_path = "books/frankenstein.txt"
	n_words = get_num_words(book_path)
	print(f"{n_words} words found in the document")
	character_dict = get_letter_count(book_path)
	print(character_dict)

main()
