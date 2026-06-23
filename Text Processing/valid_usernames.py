def is_valid_username(username):
    if not 3 <= len(username) <= 16:
        return False
    for ch in username:
        if not (ch.isalnum()or ch in "_-"):
            return False
    return True


usernames = input().split(", ")
for username in usernames:
    if is_valid_username(username):
        print(username)

