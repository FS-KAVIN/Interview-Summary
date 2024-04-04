from typing import List, Dict
from flask import Flask

app = Flask(__name__)


def check_palindrome(input_str):
    t = input_str
    res = ""
    for i in t:
        res = i + res
    return input_str == res


@app.route('/')
def index() -> str:
    input_str = "rar"
    if check_palindrome(input_str):
        return f"{input_str} is a palindrome"
    else:
        return f"{input_str} is not a palindrome"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
