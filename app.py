from flask import *
import firebase

app = Flask(__name__)

@app.route("/")
def index():
    #admins = firebase.jus_return("administrators").val()
    admins = []
    return render_template("index.html",current_tab="dashboard",administrators=admins)

@app.route("/products")
def products_view():
    #products = firebase.jus_return("products")
    #print(products)
    products = None
    return render_template("products.html",products=products)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
