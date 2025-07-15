import re

def assess_password_strength(password):
    """
    Assesses the strength of a password based on various criteria.

    Args:
        password (str): The password string to assess.

    Returns:
        dict: A dictionary containing the strength score and a list of feedback messages.
    """
    score = 0
    feedback = []

    # 1. Length
    if len(password) >= 12:
        score += 2
        feedback.append("Excellent length (12+ characters)")
    elif len(password) >= 8:
        score += 1
        feedback.append("Good length (8-11 characters)")
    else:
        feedback.append("Consider a longer password (at least 8 characters recommended)")

    # 2. Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Contains uppercase letters")
    else:
        feedback.append("Add uppercase letters for more strength")

    # 3. Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Contains lowercase letters")
    else:
        feedback.append("Add lowercase letters for more strength")

    # 4. Numbers
    if re.search(r"\d", password):
        score += 1
        feedback.append("Contains numbers")
    else:
        feedback.append("Add numbers for more strength")

    # 5. Special characters
    if re.search(r"[!@#$%^&*()_+={}\[\]:;\"'<,>.?/~`\\-]", password):
        score += 1
        feedback.append("Contains special characters")
    else:
        feedback.append("Add special characters for more strength")

    # 6. Check for common patterns (e.g., "password", "123456") - basic check
    common_passwords = ["password", "123456", "qwerty", "admin", "abcdef"]
    if password.lower() in common_passwords:
        score = max(0, score - 2)  # Significantly reduce score
        feedback.append("Warning: This is a very common and easily guessable password.")

    # Determine overall strength
    overall_strength = ""
    if score >= 6:
        overall_strength = "Very Strong"
    elif score >= 4:
        overall_strength = "Strong"
    elif score >= 2:
        overall_strength = "Moderate"
    else:
        overall_strength = "Weak"

    return {
        "score": score,
        "overall_strength": overall_strength,
        "feedback": feedback
    }

def main():
    print("--- Password Strength Assessor ---")
    while True:
        password = input("Enter a password to assess (or 'exit' to quit): ")
        if password.lower() == 'exit':
            break

        if not password:
            print("Please enter a password.")
            continue

        assessment = assess_password_strength(password)

        print(f"\nPassword: '{password}'")
        print(f"Overall Strength: {assessment['overall_strength']} (Score: {assessment['score']}/6)")
        print("Feedback:")
        for msg in assessment['feedback']:
            print(f"- {msg}")
        print("-" * 30)

if __name__ == "__main__":
    main()