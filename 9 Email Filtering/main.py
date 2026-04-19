import re

def is_valid_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.
    
    A valid email has:
    - A username (alphanumeric, plus some special characters: . _ % + -)
    - The '@' symbol
    - A domain name (alphanumeric and dots)
    - A top-level domain (at least 2 characters)
    """
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))

def main():
    emails = [
        "test@gmail.com",
        "wrong@.com",
        "user123@yahoo.com",
        "abc#mail.com",
        "hello.world@gmail.com",
        "noatsymbol.com",
        "user@domain",
        "valid_email123@outlook.com",
        "name@company.org",
        "bademail@com",
        "another.user@domain.co.in",
        "space in@email.com",
        ".startsdot@test.com",
        "double@@at.com"
    ]

    print("\n" + "Email Filter & Processor".center(40, "=") + "\n")

    valid_emails = []
    invalid_emails = []

    for email in emails:
        if is_valid_email(email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)

    # Display results
    print(" Valid Emails:")
    if not valid_emails:
        print("  - None")
    else:
        for email in valid_emails:
            print(f' "{email}"')

    print("\n Invalid Emails:")
    if not invalid_emails:
        print("  - None")
    else:
        for email in invalid_emails:
            print(f' "{email}"')

    # Summary
    print("\n" + "="*44)
    print(f" Summary: {len(valid_emails)} Valid | {len(invalid_emails)} Invalid | Total: {len(emails)}")
    print("="*44 + "\n")

# if __name__ == "__main__":
main()