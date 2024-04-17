class StringManipulator:
    def reverse(self, text):
        return text[::-1]

    def capitalize(self, text):
        return ' '.join(word.capitalize() for word in text.split())

    def is_palindrome(self, text):
        cleaned_text = text.replace(" ", "").lower()
        return cleaned_text == cleaned_text[::-1]

    def trim(self, text):
        return text.strip()

    def contains(self, text, substring):
        return substring in text

    def word_count(self, text):
        return len(text.split())

    def reverse_words(self, text):
        return ' '.join(text.split()[::-1])
