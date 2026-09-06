
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Product data
products = [
    {
        "name": "Mobile",
        "category": "Electronics",
        "price": 20000,
        "stock": 10
    },
    {
        "name": "Pen",
        "category": "Stationery",
        "price": 20,
        "stock": 10
    },
    {
        "name": "Notebook",
        "category": "Stationery",
        "price": 100,
        "stock": 50
    },
    {
        "name": "Keyboard",
        "category": "Electronics",
        "price": 1500,
        "stock": 15
    },
    {
        "name": "Mouse",
        "category": "Electronics",
        "price": 800,
        "stock": 25
    },
    {
        "name": "Laptop",
        "category": "Electronics",
        "price": 55000,
        "stock": 10
    }
]


@app.route("/")
def dashboard():

    total_products = len(products)

    total_stock = sum(product["stock"] for product in products)

    low_stock = sum(
        1 for product in products
        if 0 < product["stock"] <= 10
    )

    out_of_stock = sum(
        1 for product in products
        if product["stock"] == 0
    )

    rows = ""

    for product in products:

        if product["stock"] == 0:
            status = "Out of Stock"
        elif product["stock"] <= 10:
            status = "Low Stock"
        else:
            status = "Available"

        rows += f"""
        <tr>
            <td>{product["name"]}</td>
            <td>{product["category"]}</td>
            <td>₹{product["price"]}</td>
            <td>{product["stock"]}</td>
            <td>{status}</td>
        </tr>
        """

    return f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Inventory Management System</title>

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f4f6f8;
}}

.container {{
    display: flex;
    min-height: 100vh;
}}

.sidebar {{
    width: 240px;
    background: #1f2937;
    color: white;
    padding: 25px 15px;
}}

.sidebar h2 {{
    text-align: center;
    margin-bottom: 35px;
}}

.sidebar a {{
    display: block;
    color: white;
    text-decoration: none;
    padding: 14px;
    margin-bottom: 8px;
    border-radius: 8px;
}}

.sidebar a:hover,
.sidebar .active {{
    background: #374151;
}}

.main {{
    flex: 1;
    padding: 35px;
}}

.header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
}}

.header h1 {{
    margin: 0;
}}

.header p {{
    color: #666;
}}

.add-btn {{
    background: #2563eb;
    color: white;
    padding: 13px 20px;
    border-radius: 8px;
    text-decoration: none;
}}

.cards {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin: 30px 0;
}}

.card {{
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.08);
}}

.card h3 {{
    color: #666;
    margin: 0;
}}

.value {{
    font-size: 32px;
    font-weight: bold;
    margin: 15px 0 0;
}}

.products {{
    background: white;
    padding: 25px;
    border-radius: 12px;
}}

.products h2 {{
    margin-top: 0;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}}

th,
td {{
    padding: 15px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}}

th {{
    background: #f8fafc;
}}

.status {{
    font-weight: bold;
}}

@media (max-width: 900px) {{

    .cards {{
        grid-template-columns: repeat(2, 1fr);
    }}

}}

@media (max-width: 600px) {{

    .container {{
        flex-direction: column;
    }}

    .sidebar {{
        width: 100%;
    }}

    .cards {{
        grid-template-columns: 1fr;
    }}

    .header {{
        flex-direction: column;
        align-items: flex-start;
        gap: 20px;
    }}

    .main {{
        padding: 20px;
    }}

}}

</style>

</head>


<body>

<div class="container">


<aside class="sidebar">

<h2>📦 Inventory</h2>

<a href="/" class="active">🏠 Dashboard</a>

<a href="/add_product">📦 Products</a>

<a href="#">📊 Stock</a>

<a href="#">📋 Categories</a>

<a href="#">📈 Reports</a>

</aside>


<main class="main">


<div class="header">

<div>

<h1>Inventory Management System</h1>

<p>Manage your products and stock efficiently.</p>

</div>


<a href="/add_product" class="add-btn">
+ Add Product
</a>

</div>



<section class="cards">


<div class="card">

<h3>Total Products</h3>

<p class="value">
{total_products}
</p>

</div>


<div class="card">

<h3>Total Stock</h3>

<p class="value">
{total_stock}
</p>

</div>


<div class="card">

<h3>Low Stock</h3>

<p class="value">
{low_stock}
</p>

</div>


<div class="card">

<h3>Out of Stock</h3>

<p class="value">
{out_of_stock}
</p>

</div>


</section>



<section class="products">

<h2>Recent Products</h2>


<table>

<thead>

<tr>

<th>Product</th>

<th>Category</th>

<th>Price</th>

<th>Stock</th>

<th>Status</th>

</tr>

</thead>


<tbody>

{rows}

</tbody>

</table>

</section>


</main>

</div>

</body>

</html>
"""


@app.route("/add_product", methods=["GET", "POST"])
def add_product():

    if request.method == "POST":

        name = request.form["name"]
        category = request.form["category"]
        price = float(request.form["price"])
        stock = int(request.form["stock"])

        products.insert(
            0,
            {
                "name": name,
                "category": category,
                "price": price,
                "stock": stock
            }
        )

        return redirect(url_for("dashboard"))

    return """
<!DOCTYPE html>
<html>

<head>

<title>Add Product</title>

<style>

body {
    font-family: Arial;
    background: #f4f6f8;
    padding: 40px;
}

.form-box {
    background: white;
    max-width: 500px;
    margin: auto;
    padding: 30px;
    border-radius: 12px;
}

input {
    width: 100%;
    padding: 12px;
    margin: 8px 0 18px;
}

button {
    background: #2563eb;
    color: white;
    border: none;
    padding: 12px 20px;
    border-radius: 7px;
    cursor: pointer;
}

a {
    margin-left: 15px;
}

</style>

</head>

<body>

<div class="form-box">

<h1>➕ Add Product</h1>

<form method="POST">

<label>Product Name</label>

<input type="text" name="name" required>


<label>Category</label>

<input type="text" name="category" required>


<label>Price</label>

<input type="number" name="price" min="0" required>


<label>Stock</label>

<input type="number" name="stock" min="0" required>


<button type="submit">
Add Product
</button>

<a href="/">
Cancel
</a>

</form>

</div>

</body>

</html>
"""


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=8000,
        debug=False,
        use_reloader=False
    )