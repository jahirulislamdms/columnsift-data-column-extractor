# 📊 ColumnSift – Data Column Extractor

ColumnSift is a simple yet powerful Python tool that allows you to extract any column from a CSV or Excel file and export it as a clean text file.

Perfect for quickly isolating emails, phone numbers, names, or any dataset column.

---

## 🚀 Features

- ✅ Supports CSV, XLS, and XLSX files
- ✅ Simple file picker (Tkinter GUI)
- ✅ Displays all available columns
- ✅ Column preview (first 5 rows)
- ✅ Export selected column to TXT
- ✅ Skips empty values automatically
- ✅ Clean and user-friendly terminal interface

---

## 📦 Requirements

- Python 3.8+
- pandas
- openpyxl (for Excel files)

Install dependencies:

```bash
pip install pandas openpyxl
```

---

## ▶️ How to Run

```bash
python columnsift_data_extractor.py
```

---

## 📝 How It Works

1. Select a CSV or Excel file.
2. View the list of available columns.
3. Choose the column number you want to extract.
4. Preview the first 5 rows.
5. Confirm export.
6. The column is saved as a `.txt` file.

---

## 📂 Output

The exported file will be saved as:

```
<ColumnName>.txt
```

- No headers included
- No index included
- Empty values automatically removed

---

## 💡 Example Use Cases

- Extract email lists
- Extract phone numbers
- Extract usernames
- Extract product IDs
- Data cleaning & segmentation
- Preparing marketing lists

---

## 🛡️ Privacy

Runs completely offline.  
No data is sent externally.

---

## 📜 License

MIT License
