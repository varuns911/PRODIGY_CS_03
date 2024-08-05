import re

def assess_password_strength(password):
    # Criteria variables
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    # Calculate score based on criteria
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])

    # Determine strength of password
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character (e.g., !, @, #, $, %, etc.).")
    
    return strength, feedback

def main():
    password = input("Enter the password to assess: ")
    strength, feedback = assess_password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f" - {suggestion}")

if __name__ == "__main__":
    main()

