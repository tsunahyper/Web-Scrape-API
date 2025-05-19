# 🕷️ Web Scrape API - Spider-Man Villains Collector

A lightweight Python-based API that scrapes a list of villains from a Spider-Man wiki page and converts it into downloadable CSV or Excel (XLSX) format. Built using **BeautifulSoup4** and **Pandas**, the data is fetched dynamically with every request to ensure the most up-to-date list.

---

## 📌 Features

- 🔍 Scrapes a table of Spider-Man villains from a public wiki
- 📥 Converts scraped data into `.csv` or `.xlsx` format
- 🧠 Uses BeautifulSoup4 for parsing HTML
- 📊 Uses Pandas for data processing and file generation
- 📁 Automatically stores output in the system `Downloads` folder
- ⚡ Trigger data fetch + download with a single button click (API endpoint or UI)

---

## 🧰 Technologies Used

- `Python 3.x`
- [`BeautifulSoup4`](https://www.crummy.com/software/BeautifulSoup/)
- [`Pandas`](https://pandas.pydata.org/)
- `Requests`
- `Flask` (if you're running this as a REST API)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/web-scrape-api.git
cd web-scrape-api
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the API
``` bash
python app.py
```

### 4. Use the API - Send a request (e.g. press a button on frontend or hit endpoint):
``` bash
GET /scrape-villains
```
This will:
	•	Scrape the latest table of villains
	•	Save it as villains.csv or villains.xlsx
	•	Store the file in your Downloads directory

### 📂 Output
File format: .csv or .xlsx <br>
Default path: /home/username/Downloads or C:\Users\username\Downloads (depending on OS)
 
### 📸 Sample Screenshot (Optional)
Include a screenshot of the table or download button if using a frontend.

### 🧪 Example API Response
```json
{
  "status": "success",
  "message": "Data scraped and saved as villains.xlsx",
  "path": "/Users/{your_user}/Downloads/villains.xlsx"
}
```

### 👨‍💻 Author
Created by Tsunahyper
GitHub: https://github.com/tsunahyper
