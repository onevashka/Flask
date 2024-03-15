from flask import Flask, render_template


app = Flask(__name__)


footwear = [
    {
        "name" : "Sneakers",
        "firm" : "Nike",
        "price" : "$109",
    },
    {
        "name" : "Shoes ",
        "firm" : "Mango Man",
        "price" : "$99",
    },
    {
        "name" : "Sneakers",
        "firm" : "Puma",
        "price" : "$79",
    },
    
]

clothing = [
    {
        "name" : "Jacket",
        "firm" : "Tommy Hilfiger",
        "price" : "$249",
    },
    {
        "name" : "Coat",
        "firm" : "Mango Man",
        "price" : "$549",
    },
    {
        "name" : "T-shirt",
        "firm" : "Under Armour",
        "price" : "$49",
    },
]


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/catalog/")
def catalog():
    return render_template("catalog.html", clothing=clothing, footwear=footwear) 


@app.route("/catalog/<items_name>/")
def catalog_name(items_name):
    for item in clothing + footwear:
        if item["name"] == items_name:
            return render_template("items.html", item=item)
    return f"Item not found"


