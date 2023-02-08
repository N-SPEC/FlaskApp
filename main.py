from flask import Flask, jsonify

from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World"

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10

    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": True,
            "Server IP": "132.224.20.94"
        }
    else:
        print(f"{copy_n} is not an armstrong number")
    result = {
            "Number": copy_n,
            "Armstrong": False,
            "Server IP": "132.224.20.94"
        }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)