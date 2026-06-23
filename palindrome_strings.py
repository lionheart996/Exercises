words = input().split()
searched_palindrome = input()
list_with_palindromes = []
searched_word_found = 0
for word in words:
    if word == word[::-1]:
        list_with_palindromes.append(word)

    if word == searched_palindrome:
        searched_word_found += 1


print(list_with_palindromes)
print(f"Found palindrome {searched_word_found} times")