def valid_email(email):
  
    if email.count('@') != 1:
        return False

    username, domain = email.split('@')

    if not username or username.startswith('.') or username.endswith('.') or '.' in username:
        return False

    special_char_count = 0
    for char in username:
        if not char.isalnum() and char in {',', '.', '_'}:
            special_char_count += 1
    if special_char_count > 2:
        return False

    if not domain or domain.startswith('.') or domain.endswith('.') or '.' not in domain:
        return False

    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._@")
    for char in email:
        if char not in allowed_chars:
            return False

    return True



e_mail = input("Enter the E-mail Address:\n")
if valid_email(e_mail):
    print("Valid E-mail.\n")
else:
    print("Invalid E-mail.\n")

