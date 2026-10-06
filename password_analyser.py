import re
import math
import getpass


COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "abc123",
    "password123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "iloveyou",
    "monkey",
    "dragon",
}


def calculate_entropy(password):
    """Calculate estimated password entropy in bits."""

    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26

    if re.search(r"[A-Z]", password):
        charset_size += 26

    if re.search(r"\d", password):
        charset_size += 10

    if re.search(r"[^A-Za-z0-9]", password):
        charset_size += 32

    if charset_size == 0:
        return 0

    return len(password) * math.log2(charset_size)


def calculate_score(password):
    """Calculate password strength score out of 7."""

    score = 0

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    # Character types
    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    # Common password penalty
    if password.lower() in COMMON_PASSWORDS:
        score = 0

    # Repeated character penalty
    if re.search(r"(.)\1\1", password):
        score = max(0, score - 1)

    return score


def get_verdict(score, entropy):
    """Determine the final password verdict."""

    if score <= 2 or entropy < 40:
        return "WEAK"

    elif score <= 4 or entropy < 60:
        return "MODERATE"

    elif score <= 5 or entropy < 80:
        return "STRONG"

    else:
        return "VERY STRONG"


def analyze_password(password):
    """Analyze password and return its results."""

    length = len(password)
    entropy = calculate_entropy(password)
    score = calculate_score(password)
    verdict = get_verdict(score, entropy)

    return length, entropy, score, verdict


def display_result(length, entropy, score, verdict):
    """Display the password analysis results."""

    print("\n" + "=" * 45)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    print(f"\nPassword Length : {length}")
    print(f"Entropy         : {entropy:.2f} bits")
    print(f"Score           : {score}/7")
    print(f"Verdict         : {verdict}")

    print("\n" + "=" * 45)


def main():

    print("Password Strength Analyzer")
    print("---------------------------")
    print("Your password will not be stored or displayed.")

    password = getpass.getpass("\nEnter your password: ")

    if not password:
        print("Password cannot be empty.")
        return

    length, entropy, score, verdict = analyze_password(password)

    display_result(length, entropy, score, verdict)


if __name__ == "__main__":
    main()