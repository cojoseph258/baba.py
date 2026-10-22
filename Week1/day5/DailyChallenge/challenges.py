"""Daily Challenge : tri de mots et recherche du premier mot le plus long."""


def sort_words(text):
    return ",".join(sorted(text.split(",")))


def longest_word(sentence):
    longest = ""
    for word in sentence.split():
        # > conserve le premier mot en cas d'égalité. La ponctuation est gardée.
        if len(word) > len(longest):
            longest = word
    return longest


if __name__ == "__main__":
    print(sort_words(input("Entre des mots séparés par des virgules : ")))
    print(longest_word(input("Entre une phrase : ")))
