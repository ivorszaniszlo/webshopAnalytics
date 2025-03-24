import duckdb
import pandas as pd
import plotly.express as px
from fpdf import FPDF
from datetime import date
import os

# Mappa, ahová mentünk
charts_dir = "charts"
os.makedirs(charts_dir, exist_ok=True)

try:
    print("🔌 Connecting to DuckDB...")
    con = duckdb.connect("../dev.duckdb")
    print("✅ DuckDB connected")
except Exception as e:
    print("❌ Failed to connect to DuckDB:", e)
    exit(1)
    
try:
    print("📥 Fetching top 10 customer data...")
    df = con.execute("""
        SELECT customer_name, total_spent_usd
        FROM customer_orders_summary
        ORDER BY total_spent_usd DESC
        LIMIT 10
    """).fetchdf()
    print("✅ Data fetched:\n", df.head())
except Exception as e:
    print("❌ Error fetching data:", e)
    exit(1)

try:
    print("📊 Generating chart...")
    fig = px.bar(
        df,
        x="customer_name",
        y="total_spent_usd",
        title="Top 10 Customers by Total Spent (USD)",
        labels={"customer_name": "Customer", "total_spent_usd": "Total Spent (USD)"}
    )
    fig.update_layout(xaxis_tickangle=-45)
    chart_file_html = os.path.join(charts_dir, "top_customers_chart.html")
    fig.write_html(chart_file_html)
    print("✅ HTML chart saved:", chart_file_html)
except Exception as e:
    print("❌ Error generating HTML chart:", e)
    exit(1)

try:
    print("📄 Creating PDF report (text only)...")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Webshop Analytics Report", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"Top 10 Customers by Total Spent - {date.today()}", ln=True, align="C")
    pdf.ln(10)

    for idx, row in df.iterrows():
        pdf.cell(200, 10, f"{idx+1}. {row['customer_name']}: ${row['total_spent_usd']:.2f}", ln=True)

    pdf_file = os.path.join(charts_dir, f"webshop_report_{date.today()}.pdf")
    pdf.output(pdf_file)
    print("✅ PDF saved:", pdf_file)
except Exception as e:
    print("❌ Error creating PDF:", e)
    exit(1)
