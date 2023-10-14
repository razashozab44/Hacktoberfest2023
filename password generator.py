Here's a Python program that generates password combinations and incorporates user suggestions. This version has been extended for more complexity:

```python
import itertools
import string

def generate_password_combinations(length, use_uppercase, use_digits, use_special_chars):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    combinations = []
    for r in range(1, length + 1):
        for combo in itertools.product(chars, repeat=r):
            combinations.append(''.join(combo))

    return combinations

def get_user_suggestions():
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Use uppercase letters (yes/no): ").lower() == 'yes'
    use_digits = input("Use digits (yes/no): ").lower() == 'yes'
    use_special_chars = input("Use special characters (yes/no): ").lower() == 'yes'

    return length, use_uppercase, use_digits, use_special_chars

def main():
    print("Password Combination Generator")
    print("-------------------------------")

    length, use_uppercase, use_digits, use_special_chars = get_user_suggestions()

    combinations = generate_password_combinations(length, use_uppercase, use_digits, use_special_chars)

    print(f"\nGenerated {len(combinations)} password combinations:")
    for combo in combinations:
        print(combo)

if __name__ == "__main__":
    main()
```

This program allows the user to specify the password length and whether to include uppercase letters, digits, and special characters. It then generates all possible combinations of the selected character set up to the specified length and displays them.
