from flask import Flask

app = Flask(__name__)

storage = {}
# storage = {'20021122': 150, '20021022': 150, '20031122': 150, '20021115': 150, '20021123': 150,
#           '20020922': 150, '20031022': 150, '20021113': 150}
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', "NOV", 'DEC']


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int) -> str:
    if date[0:4].isdigit() and 1 < int(date[4:6]) <= 12 and 1 < int(date[6:]) < 32:
        storage[date] = number
        print(storage)
        return "saved to storage"
    raise ValueError
    # return "404 - wrong date"


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    result = 0
    for i in storage:
        if int(i[:4]) == year:
            result += storage[i]
    return f"you lost {result}UAH in {year}"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    result = 0
    for i in storage:
        if int(i[:4]) == year and int(i[4:6]) == month:
            result += storage[i]
    return f"you lost {result}UAH in {months[month - 1]}-{year}"

@app.route("/add/",methods=['GET'])
def search():
    pass


if __name__ == "__main__":
    app.run(debug=True)
