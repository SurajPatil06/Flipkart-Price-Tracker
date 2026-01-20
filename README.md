# Web Scraper & Price Trend Analyzer (Python)

## 📌 Project Overview
This project is a Python-based web scraper that collects product price data from a public website at regular intervals and analyzes price trends over time using data visualization.

It demonstrates real-world Python skills such as web scraping, data storage, automation concepts, and data analysis.

---

## 🚀 Features
- Scrapes product price from a website
- Stores price data along with date in a CSV file
- Analyzes historical price data
- Visualizes price trends using graphs
- Clean and modular Python code

---

## 🛠️ Tech Stack
- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib

---

## 📁 Project Structure
web-scraper-analyzer/
│
├── scraper.py # Scrapes product price data
├── analyzer.py # Reads CSV and plots trends
├── data.csv # Stored price history
├── requirements.txt # Python dependencies
└── README.md


---

## ⚙️ How It Works
1. `scraper.py` sends an HTTP request to the target website
2. Product price is extracted using BeautifulSoup
3. The current date and price are saved in a CSV file
4. `analyzer.py` reads the CSV file
5. Price trends are visualized using Matplotlib

---

## ▶️ How to Run

```bash
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Run the scraper
python scraper.py
3️⃣ Analyze the data
python analyzer.py
