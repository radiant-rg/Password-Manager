
# 🔐 Password Manager (Tkinter)

A simple and clean **Password Manager GUI** built with **Python, Tkinter, and JSON**.  
It allows you to:

- Save website passwords  
- Search stored passwords  
- Auto-resize header image (like CSS background-size: cover)  
- Store credentials locally in `data.json`  

---

## 📸 Features

### ✔ Save Password  
Stores website, username/email, and password into a JSON file.

### ✔ Search Password  
Fetches saved credentials and displays them using `messagebox`.

### ✔ Responsive Header Image  
The header banner automatically resizes while keeping aspect ratio—similar to CSS `background-size: cover`.

### ✔ Clean UI  
Resizes well, uses grid layout with expandable columns.

---

## 🗂 Project Structure

│── img.png 

│── data.json 

│── main.py 

│── README.md


---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install pillow

2. Place your header image as:
   ```bash
   img.png
3. Run the program:
   ```bash
   python main.py

## 🧠 How It Works
- Saving passwords

- Reads existing data.json

- Updates dictionary

- Writes back formatted JSON

## Searching passwords

- Loads data.json

- Matches website name

- Shows username + password in popup

## Header Image Resizing

Uses a custom function:

- Scales image to fill width

- Crops center to maintain composition

- Refreshes on window resize

## 📦Dependencies

- Python 3.x

- Tkinter (comes with Python)

- Pillow (PIL)

Install Pillow:
```bash
pip install pillow




