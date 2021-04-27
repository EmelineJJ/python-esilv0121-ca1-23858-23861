# Loopy String
# Francoise RUCH - 23861
# Emeline JJ - 23858
# Salut
word = input("Enter a word: ")
print("\nHer's  each letter in your word")
for letter in word:
    print(letter)

word = input("Enter a word: ")


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)