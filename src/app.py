import hashlib


def secure_function(user_input: str) -> str:
    password_hash = hashlib.sha256(user_input.encode("utf-8")).hexdigest()
    return password_hash


if __name__ == "__main__":
    print(secure_function("admin"))
