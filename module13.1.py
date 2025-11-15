from flask import Flask
app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

@app.route("/prime_number/<int:n>")
def prime_number(n):
    result = {
        "Number": n,
        "isPrime": is_prime(n)
    }
    return result


if __name__ == "__main__":
    app.run()


