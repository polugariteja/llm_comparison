# LLM Comparison Tool – Setup Guide

## Project Description

This project is an **LLM Comparison Tool** used to compare responses from different Large Language Models based on quality, accuracy, and usefulness.

---

## Environment Setup

### 1. Navigate to Project Folder

```bash
cd "LLM comparision"
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Streamlit App

```bash
python -m streamlit run app.py
```

After running, open the **local URL shown in the terminal** in your browser.

---

## Important Notes

* Do **not upload `venv/` or `.env`** to GitHub.
* Keep API keys safe inside the `.env` file.
* Use **requirements.txt** to recreate the environment.

---

## Project Aim

To evaluate and compare different **LLMs** based on:

* Response accuracy
* Speed
* Quality of answers
* Usefulness for real-world tasks

---

## Author

Project created for **learning and academic purposes**.
