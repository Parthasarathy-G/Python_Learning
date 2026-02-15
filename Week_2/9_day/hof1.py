def gmail_email(username, domain="gmail.com"):
    return f"{username}@{domain}"

def ymail_email(username, domain="ymail.com"):
    return f"{username}@{domain}"

def hotmail_email(username, domain="hotmail.com"):
    return f"{username}@{domain}"


def build_email(username, email_func):
    return email_func(username) # ! gmail_email(gowtham)

print(build_email("Gowtham",gmail_email))
print(build_email("Rahul",ymail_email))
print(build_email("Parthasarathy",hotmail_email))
