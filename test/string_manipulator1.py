class StringChecker:
    @staticmethod
    def clean_string(s):
        """Remove non-alphanumeric characters and convert to lowercase."""
        return ''.join(filter(str.isalnum, s)).lower()

    @staticmethod
    def is_palindrome(s):
        """Check if the string is a palindrome."""
        cleaned = StringChecker.clean_string(s)
        return cleaned == cleaned[::-1]

    @staticmethod
    def is_isogram(s):
        """Check if the string is an isogram."""
        cleaned = StringChecker.clean_string(s)
        return len(set(cleaned)) == len(cleaned)

    @staticmethod
    def main():
        # Ask for user input to determine which checker to use
        while True:
            try:
                choice = int(input("Enter 1 to check for palindrome, 2 to check for isogram: "))
                if choice in [1, 2]:
                    break
                else:
                    print("Please enter either 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Get the string to check
        input_string = input("Enter the string to check: ")

        # Check according to user's choice
        if choice == 1:
            result = StringChecker.is_palindrome(input_string)
            print(f"Is '{input_string}' a palindrome? {'Yes' if result else 'No'}")

        elif choice == 2:
            result = StringChecker.is_isogram(input_string)
            print(f"Is '{input_string}' an isogram? {'Yes' if result else 'No'}")


# Run the main method in the class
if __name__ == "__main__":
    StringChecker.main()