# 📈 Stock Market Insights

## Overview
**Stock Market Insights** is a responsive and interactive web application built using **Flask**. It helps users explore and manage data about major companies by displaying financial metrics like stock price, market cap, sector, P/E ratio, and more.

The app offers a clean, user-friendly interface with support for searching, viewing, adding, and editing company data — all designed with good visual hierarchy and accessibility in mind.

---

## Features

### Home Page
- Displays the **3 companies with the lowest stock prices**.
- Uses Bootstrap cards for clean layout.
- Each card includes the company image, name, and stock price.
- Clicking a card leads to the company’s detailed view page.

---

### Search Functionality
- Users can search companies by:
  - **Company name**
  - **Ticker symbol**
  - **Sector**
- Supports **case-insensitive substring matching**.
- Displays:
  - Total number of results
  - Styled Bootstrap cards for each match
- Includes **autocomplete suggestions** while typing.

---

### Company Details Page
- Displays full company information:
  - Image, name, sector, stock price, market cap, P/E ratio, etc.
- Shows a list of **similar companies** with clickable links.
- Includes a **subtle 'Edit' button** to update company data.

---

### Add New Company
- Accessible via the navbar.
- Presents a **form with labeled input fields** for all required company data.
- Uses **AJAX** for form submission:
  - Displays success message without refreshing the page.
  - Includes a link to view the newly created item.
  - Clears the form and resets focus for a new entry.
- **Validates** that required fields are filled and numeric values are correct.

---

### Edit Company
- Accessible from the company’s detail page.
- Pre-fills all fields with the current data.
- Two buttons:
  - **Submit** → Saves changes and redirects to detail view.
  - **Discard** → Prompts for confirmation before exiting without saving.

---

## Design and Accessibility
- Implements:
  - Conceptual grouping
  - Clear labels (information scent)
  - Appropriate use of whitespace, color, contrast
  - A color palette with:
    - Base: Navy Blue `#2c3e50`
    - Accent: Blue `#3498db`
    - Light Grey `#ecf0f1`
    - Dark Grey `#34495e`
- **All images have `alt` text** for accessibility.
- **Responsive layout** built using **Bootstrap 5**.

---

## Getting Started

### Prerequisites
- Python 3.x
- Flask

### Run the App
```bash
python server.py

