from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/calculate', methods=['POST'])
def calculate():

    # Get values from form
    car_km = float(request.form['car'])
    internet_hours = float(request.form['internet'])
    mobile_hours = float(request.form['mobile'])
    streaming_hours = float(request.form['streaming'])
    gaming_hours = float(request.form['gaming'])
    social_hours = float(request.form['social'])
    laptop_hours = float(request.form['laptop'])

    # Emission factors (kg CO2 per unit)
    car_emission = car_km * 0.21
    internet_emission = internet_hours * 0.06
    mobile_emission = mobile_hours * 0.05
    streaming_emission = streaming_hours * 0.055
    gaming_emission = gaming_hours * 0.07
    social_emission = social_hours * 0.04
    laptop_emission = laptop_hours * 0.05

    # Daily total
    daily_total = (
        car_emission +
        internet_emission +
        mobile_emission +
        streaming_emission +
        gaming_emission +
        social_emission +
        laptop_emission
    )

    # Convert to monthly footprint
    total = daily_total * 30

    return render_template(
        "result.html",
        car=round(car_emission * 30, 2),
        internet=round(internet_emission * 30, 2),
        mobile=round(mobile_emission * 30, 2),
        streaming=round(streaming_emission * 30, 2),
        gaming=round(gaming_emission * 30, 2),
        social=round(social_emission * 30, 2),
        laptop=round(laptop_emission * 30, 2),
        total=round(total, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)

