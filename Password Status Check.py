import re

def evaluate_password_strength(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r"\d", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    
    # Criteria checks
    criteria_met = {
        "Length (>= 8 characters)": length_criteria,
        "Contains digit": digit_criteria,
        "Contains uppercase letter": uppercase_criteria,
        "Contains lowercase letter": lowercase_criteria,
        "Contains special character": special_char_criteria
    }
    
    # Count the number of criteria met
    criteria_met_count = sum(criteria_met.values())
    
    # Strength evaluation based on number of criteria met
    if criteria_met_count == 5:
        strength = "Very Strong"
    elif criteria_met_count == 4:
        strength = "Strong"
    elif criteria_met_count == 3:
        strength = "Moderate"
    elif criteria_met_count == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Display the criteria results and overall strength
    for criteria, met in criteria_met.items():
        print(f"{criteria}: {'Met' if met else 'Not met'}")
    
    print(f"\nPassword Strength: {strength}")

# Example usage
password = input("Enter your password: ")
evaluate_password_strength(password)