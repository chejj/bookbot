from stats import get_num_words, get_letter_count, sort_letter_count
import sys

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")

	n_words = get_num_words(book_path)
	print(f"Found {n_words} total words")
	sorted_dict = sort_letter_count(book_path)
	print("--------- Character Count -------")
	character_dict = get_letter_count(book_path)
	for key in sorted_dict:
		if key.isalpha():
			print(f"{key}: {sorted_dict[key]}")
main()
