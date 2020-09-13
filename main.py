from flask import Flask, render_template, request

app = Flask(__name__)

products_dict = {
  "company_A": ["product_1", "product_4", "product_5"],
  "company_B": ["product_3", "product_5"],
  "company_C": ["product_1", "product_2", "product_3", "product_4", "product_5"],
  "company_D": ["product_1", "product_2", "product_3"]
}

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")
  
@app.route('/products', methods=['GET', 'POST'])
def products():
    username = request.form['username']
    if username in products_dict:
        products_list = products_dict[username]
        return render_template("index1.html", username=username, products = products_list)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)