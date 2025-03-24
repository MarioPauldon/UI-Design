#Mario Pauldon mip2124
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import re

app = Flask(__name__)
app.secret_key = "supersecretkey"  # flashes messages

data = {
    "1": {
    "id": "1",
    "image": "https://1000logos.net/wp-content/uploads/2016/10/Apple-Logo-1536x864.png",
    "company": "Apple Inc.",
    "ticker": "AAPL",
    "sector": "Technology",
    "market_cap": "$3.456T",
    "stock_price": "$185.72",
    "revenue": "$394B",
    "pe_ratio": "28.4",
    "dividend_yield": "0.55%",
    "similar_companies": ["2", "3"]
    
  },
  "2": {
    "id": "2",
    "image": "https://1000logos.net/wp-content/uploads/2017/04/Microsoft-Logo.png",
    "company": "Microsoft Corporation",
    "ticker": "MSFT",
    "sector": "Technology",
    "market_cap": "$3.230T",
    "stock_price": "$310.20",
    "revenue": "$198B",
    "pe_ratio": "35.2",
    "dividend_yield": "0.80%",
    "similar_companies": ["1", "5"]
  },
  "3": {
    "id": "3",
    "image" : "https://1000logos.net/wp-content/uploads/2022/02/NVIDIA_logo.png",
    "company": "NVIDIA Corporation",
    "ticker": "NVDA",
    "sector": "Semiconductors",
    "market_cap": "$2.900T",
    "stock_price": "$720.50",
    "revenue": "$26.9B",
    "pe_ratio": "108.0",
    "dividend_yield": "0.12%",
    "similar_companies": ["2", "10"]
  },
  "4": {
    "id": "4",
    "image": "https://1000logos.net/wp-content/uploads/2016/10/Amazon-Logo-1536x864.png",
    "company": "Amazon.com, Inc.",
    "ticker": "AMZN",
    "sector": "E-commerce",
    "market_cap": "$2.475T",
    "stock_price": "$3,250.00",
    "revenue": "$469.8B",
    "pe_ratio": "60.5",
    "dividend_yield": "N/A",
    "similar_companies": ["5", "7"]
  },
  "5": {
    "id": "5",
    "image": "https://1000logos.net/wp-content/uploads/2021/05/Google-logo.png",
    "company": "Alphabet Inc.",
    "ticker": "GOOGL",
    "sector": "Technology",
    "market_cap": "$2.361T",
    "stock_price": "$2,850.00",
    "revenue": "$257.6B",
    "pe_ratio": "34.8",
    "dividend_yield": "N/A",
    "similar_companies": ["1", "2"]
  },
  "6": {
    "id": "6",
    "image": "https://1000logos.net/wp-content/uploads/2021/10/Saudi-Aramco-logo-1536x864.png",
    "company": "Saudi Aramco",
    "ticker": "2222.SR",
    "sector": "Oil & Gas",
    "market_cap": "$1.800T",
    "stock_price": "$35.20",
    "revenue": "$400.5B",
    "pe_ratio": "17.5",
    "dividend_yield": "3.20%",
    "similar_companies": ["15", "16"]
  },
  "7": {
    "id": "7",
    "image": "https://1000logos.net/wp-content/uploads/2021/10/Meta-Logo.png",
    "company": "Meta Platforms, Inc.",
    "ticker": "META",
    "sector": "Social Media",
    "market_cap": "$1.655T",
    "stock_price": "$375.00",
    "revenue": "$117.9B",
    "pe_ratio": "28.0",
    "dividend_yield": "N/A",
    "similar_companies": ["5", "9"]
  },
  "8": {
    "id": "8",
    "image": "https://1000logos.net/wp-content/uploads/2021/04/Tesla-logo-1536x864.png",
    "company": "Tesla, Inc.",
    "ticker": "TSLA",
    "sector": "Automotive and Clean Energy",
    "market_cap": "$1.274T",
    "stock_price": "$1,050.00",
    "revenue": "$53.8B",
    "pe_ratio": "120.5",
    "dividend_yield": "N/A",
    "similar_companies": ["10", "14"]
  },
  "9": {
    "id": "9",
    "image" : "https://1000logos.net/wp-content/uploads/2018/08/Berkshire-Hathaway-Logo.png",
    "company": "Berkshire Hathaway Inc.",
    "ticker": "BRK.A",
    "sector": "Investment",
    "market_cap": "$1.023T",
    "stock_price": "$425,000.00",
    "revenue": "$276.1B",
    "pe_ratio": "8.5",
    "dividend_yield": "N/A",
    "similar_companies": ["13", "17"]
  },
  "10": {
    "id": "10",
    "image": "https://1000logos.net/wp-content/uploads/2021/08/TSMC-Logo-1536x966.png",
    "company": "Taiwan Semiconductor Manufacturing Company Limited (TSMC)",
    "ticker": "TSM",
    "sector": "Semiconductors",
    "market_cap": "$997.42B",
    "stock_price": "$120.00",
    "revenue": "$57.2B",
    "pe_ratio": "22.0",
    "dividend_yield": "1.60%",
    "similar_companies": ["3", "12"]
  }
}

# Home route 
@app.route('/')
# Finds the 3 companies with the lowest stock prices
def home():
    # Convert stock prices to floats, handling cases where they might already be floats
    for company in data.values():
        stock_price = company["stock_price"]
        if isinstance(stock_price, str):  # Ensure it's a string before calling replace
            stock_price = float(stock_price.replace("$", "").replace(",", ""))
        company["stock_price"] = stock_price  # Store the cleaned float value
        
    lowest_stock_companies = sorted(data.values(), key=lambda x: x["stock_price"])[:3]

    return render_template('home_page.html', companies=lowest_stock_companies)
  
# Add new company route
# AJAX-based Add Company route
@app.route('/add', methods=['GET', 'POST'])
def add_company():
    if request.method == 'POST':
        form_data = request.json  # Get data from AJAX request

        # Validate input fields
        required_fields = ["company", "ticker", "sector", "market_cap", "stock_price", "revenue", "pe_ratio", "dividend_yield", "image"]
        for field in required_fields:
            if not form_data.get(field, "").strip():
                return jsonify({"success": False, "message": f"{field.replace('_', ' ').capitalize()} is required."})

        # Validate stock_price and pe_ratio as numbers
        try:
            stock_price = float(form_data["stock_price"].replace("$", "").replace(",", ""))
            pe_ratio = float(form_data["pe_ratio"])
        except ValueError:
            return jsonify({"success": False, "message": "Stock Price and P/E Ratio must be valid numbers."})

        # Generate a new unique ID
        new_id = str(len(data) + 1)

        # Save new company
        data[new_id] = {
            "id": new_id,
            "image": form_data["image"],
            "company": form_data["company"],
            "ticker": form_data["ticker"],
            "sector": form_data["sector"],
            "market_cap": form_data["market_cap"],
            "stock_price": f"${stock_price:,.2f}",
            "revenue": form_data["revenue"],
            "pe_ratio": str(pe_ratio),
            "dividend_yield": form_data["dividend_yield"],
            "similar_companies": []
        }

        return jsonify({"success": True, "message": "New item successfully created!", "company_id": new_id})

    return render_template('add_company.html')

# Search functionality
@app.route('/search')
def search():
    query = request.args.get('query', '').strip().lower()

    if not query:
        return render_template('search_results.html', query=query, results=[], result_count=0) 

    # Search for matching companies
    results = [
        company for company in data.values()
        if query in company["company"].lower() or query in company["ticker"].lower() or query in company["sector"].lower()
        ]
    

    '''
    if len(results) == 1:
        # Redirect to the company page if only one match is found
        return redirect(url_for('company_page', company_id=results[0]["id"]))
    '''

    # Render search results page if multiple results
    result_count = len(results) # Count the number of results
    return render_template('search_results.html', query=query, results=results, result_count=result_count)

# Autocomplete functionality
@app.route('/autocomplete')
def autocomplete():
    search_term = request.args.get("term", "").lower()
    suggestions = [company["company"] for company in data.values() if search_term in company["company"].lower()]
    return jsonify(suggestions)

# Company details page
@app.route('/view/<company_id>')
def company_page(company_id):
    company = data.get(company_id)

    if not company:
        return "Company not found", 404

    # Find similar companies
    similar_companies = [data.get(str(cid)) for cid in company["similar_companies"] if str(cid) in data]

    return render_template('company_details.html', company=company, similar_companies=similar_companies)
  
# Edit Company Route
@app.route('/edit/<company_id>', methods=['GET', 'POST'])
def edit_company(company_id):
    company = data.get(company_id)

    if not company:
        return "Company not found", 404

    if request.method == 'POST':
        # Get updated form data
        company["company"] = request.form.get("company").strip()
        company["ticker"] = request.form.get("ticker").strip()
        company["sector"] = request.form.get("sector").strip()
        company["market_cap"] = request.form.get("market_cap").strip()
        company["stock_price"] = request.form.get("stock_price").strip()
        company["revenue"] = request.form.get("revenue").strip()
        company["pe_ratio"] = request.form.get("pe_ratio").strip()
        company["dividend_yield"] = request.form.get("dividend_yield").strip()
        company["image"] = request.form.get("image").strip()

        flash("Company details updated successfully!", "success")
        return redirect(url_for('company_page', company_id=company_id))

    return render_template('edit_company.html', company=company)


if __name__ == '__main__':
    app.run(debug=True, port=5001)





