import re
import string


def password_strength(password):
    """
    Evaluate password strength based on various criteria
    """
    strength = 0
    weaknesses = []

    # Length
    if len(password) < 8:
        weaknesses.append("Password is too short (less than 8 characters)")
    else:
        strength += 1

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        weaknesses.append("Password does not contain uppercase letters")

    # Lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        weaknesses.append("Password does not contain lowercase letters")

    # Numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        weaknesses.append("Password does not contain numbers")

    # Special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1
    else:
        weaknesses.append("Password does not contain special characters")

    # Repeated characters
    if re.search(r"(.)\1{2,}", password):
        weaknesses.append("Password contains repeated characters")

    # Common patterns
    common_patterns = ["qwerty", "123456", "abcdef", "password", "iloveyou"]
    for pattern in common_patterns:
        if pattern in password.lower():
            weaknesses.append(f"Password contains common pattern '{pattern}'")

    # Password strength rating
    if strength < 3:
        rating = "Weak"
    elif strength < 5:
        rating = "Medium"
    else:
        rating = "Strong"

    return rating, weaknesses


def recommend_secure_password_practices():
    """
    Provide recommendations for secure password practices
    """
    recommendations = [
        "Use a password manager to generate and store unique, complex passwords",
        "Use a passphrase instead of a single word as your password",
        "Avoid using easily guessable information such as your name, birthdate, or common words",
        "Use a mix of uppercase and lowercase letters, numbers, and special characters",
        "Avoid using the same password across multiple sites",
        "Change your passwords regularly (every 60-90 days)"
    ]
    return recommendations


def main():
    password = input("Enter a password to evaluate: ")
    rating, weaknesses = password_strength(password)
    print(f"Password strength: {rating}")
    if weaknesses:
        print("Weaknesses:")
        for weakness in weaknesses:
            print(f"  * {weakness}")
    print("\nRecommendations for secure password practices:")
    for recommendation in recommend_secure_password_practices():
        print(f"  * {recommendation}")


if __name__ == "__main__":
    main()
