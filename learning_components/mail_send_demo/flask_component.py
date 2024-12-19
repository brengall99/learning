from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages, replace with a strong key in production

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user input from the form
        stock = request.form.get('stock')
        target_price = request.form.get('target_price')

        # Validate the input
        if not stock or not target_price:
            flash("Please enter both a stock ticker and a target price.")
            return redirect(url_for('index'))
        
        try:
            # Try converting target_price to a float to ensure it's a valid number
            target_price = float(target_price)
        except ValueError:
            flash("Please enter a valid number for the target price.")
            return redirect(url_for('index'))

        # If input is valid, process it (e.g., save to a database or perform some action)
        # Here we'll just flash a message as a placeholder
        flash(f"Stock ticker: {stock}, Target price: ${target_price}")
        
        return redirect(url_for('index'))

    return render_template('index.html')