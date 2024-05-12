class StringChecker:
    def clean_string(self, s):
        """Remove non-alphanumeric characters and convert to lowercase."""
        return ''.join(filter(str.isalnum, s)).lower()

    def is_palindrome(self, s):
        """Check if the string is a palindrome."""
        cleaned = self.clean_string(s)
        return cleaned == cleaned[::-1]

    def is_isogram(self, s):
        """Check if the string is an isogram."""
        cleaned = self.clean_string(s)
        return len(set(cleaned)) == len(cleaned)

    def main(self):
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

        # Loop to get the string to check, ensuring it meets the length requirement
        while True:
            input_string = input("Enter the string to check: ")
            input_string = self.clean_string(input_string)
            if len(input_string) >= 2:
                break
            else:
                print("The string must be at least 2 characters long. Please try again.")

        # Check according to user's choice
        if choice == 1:
            result = self.is_palindrome(input_string)
            print(f"Is '{input_string}' a palindrome? {'Yes' if result else 'No'}")
        elif choice == 2:
            result = self.is_isogram(input_string)
            print(f"Is '{input_string}' an isogram? {'Yes' if result else 'No'}")


