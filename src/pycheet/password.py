def pas(password):
    with open('password.txt', 'w') as f:
        f.write(password)
def get_pas():
    with open('password.txt', 'r') as f:
        return f.read()