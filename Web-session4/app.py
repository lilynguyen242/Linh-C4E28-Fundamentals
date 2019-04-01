from flask import *
from bike import bike_collection
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_bike', methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template('form.html')
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]
        new_bike = {
            "model": model,
            "daily_fee": fee,
            "image": image,
            "year": year
        }
        bike_collection.insert_one(new_bike)
        return redirect('/new_bike')

if __name__ == '__main__':
  app.run(debug=True)
 