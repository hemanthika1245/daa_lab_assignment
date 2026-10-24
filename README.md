# 🎒 Campus Lost and Found Matcher

A Python-based web application developed as part of the **Design and Analysis of Algorithms (DAA) Lab — Project 5 at RGUKT Ongole**.

Campus Lost and Found Matcher helps users record lost and found items, search reports, and identify potential matches using a simple scoring-based algorithm. It is designed as a classroom prototype to demonstrate how algorithmic techniques can help solve a real-world campus problem.

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [How Matching Works](#-how-matching-works)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation and Setup](#-installation-and-setup)
- [Usage Guide](#-usage-guide)
- [Sample Test Scenario](#-sample-test-scenario)
- [Data Storage](#-data-storage)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Academic Purpose](#-academic-purpose)

## 🎯 Overview

Losing personal belongings on a college campus can be frustrating. This project provides a simple way to maintain records of lost and found items and identify reports that may refer to the same belonging.

Users can submit item details, search existing reports, and request match suggestions. A scoring-based approach evaluates similarities between reports and helps prioritize potential matches.

**Project goal:** Demonstrate the practical application of algorithmic problem-solving through a working lost-and-found web application.

## ✨ Features

- **Lost Item Reporting:** Record details of items that have been lost.
- **Found Item Reporting:** Add information about items that have been found.
- **Smart Match Suggestions:** Rank potential matches using a scoring-based approach.
- **Keyword Search:** Search reports using relevant words, such as an item's name.
- **Manual Status Updates:** Update the status of reports through the application.
- **Local Data Persistence:** Store reports in a JSON file for subsequent use.
- **Simple Web Interface:** Interact with the application through a browser running on your local machine.

## 🧠 How Matching Works

The application uses a scoring-based approach to evaluate the similarity between lost and found reports.

The matching score considers factors such as:

| Matching Factor | Description |
|---|---|
| Category | Checks whether the item categories match. |
| Shared Words | Identifies words shared by item descriptions. |
| Location | Considers whether the reported locations match. |
| Date Proximity | Considers how close the reported dates are. |

Reports with stronger similarities can receive higher scores and appear as potential matches.

The score is intended to assist users in identifying relevant reports; it does not confirm ownership.

## 🛠️ Technology Stack

- **Programming Language:** Python 3.10 or later
- **Data Storage:** JSON
- **Interface:** Local web application
- **Development Environment:** Visual Studio Code (recommended)
- **Version Control:** Git and GitHub

The current setup does not require additional Python packages according to the project instructions.

## 📂 Project Structure

```text
daa_lab_assignment/
│
├── 05_lost_found/
│   ├── app.py
│   └── data.json          # Created or used for report storage
│
├── __pycache__/           # Python-generated cache files
├── common.py              # Shared Python functionality
└── README.md              # Project documentation
```

*Note: The structure above summarizes the main files documented by the project. The exact contents of the `05_lost_found` directory may vary.*

## 💻 Prerequisites

Before running the application, make sure you have:

- Python 3.10 or later installed.
- Git installed if you want to clone the repository.
- A modern web browser.
- Visual Studio Code or another code editor (optional).

Check your Python installation:

```bash
python --version
```

On Windows, you can also use:

```bash
py --version
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/hemanthika1245/daa_lab_assignment.git
```

### 2. Navigate to the project directory

```bash
cd daa_lab_assignment
```

### 3. Run the application

**Windows:**

```bash
py 05_lost_found/app.py
```

Alternatively:

```bash
python 05_lost_found/app.py
```

**macOS / Linux:**

```bash
python3 05_lost_found/app.py
```

### 4. Open the application

After the server starts, open the local URL displayed in the terminal. The default address is usually:

```text
http://127.0.0.1:8000
```

Keep the terminal open while using the application.

### 5. Stop the application

Press `Ctrl + C` in the terminal to stop the server.

## 📖 Usage Guide

1. Start the application using the commands above.
2. Open the application in your browser.
3. Submit a lost-item report with its category, description, location, and date.
4. Submit a found-item report containing the details of the item that was found.
5. Use the match suggestion feature to evaluate a potential match.
6. Search for reports using relevant keywords.
7. Test the manual status-update functionality.

## 🧪 Sample Test Scenario

Use this example to verify the matching functionality.

**Lost item report**

- Type: Lost
- Category: Bottle
- Description: Blue steel bottle
- Location: Library
- Date: `2026-10-08`

**Found item report**

Enter a corresponding found-item report with the same category, description, location, and date.

Then:

1. Open the match suggestion feature.
2. Enter report ID `1` when prompted.
3. Check whether the second report receives a matching score of `9`, based on the scoring example in the project instructions.
4. Search for `bottle` to verify keyword searching.
5. Test manual report status changes.

The score is based on the example's stated scoring rules and should be verified against the actual implementation.

## 💾 Data Storage

The application uses a local JSON file to store reports:

```text
05_lost_found/data.json
```

JSON provides a simple, human-readable way to store structured report data without requiring a separate database server.

Because the data is stored locally, it is not automatically shared with other users or computers.

## ⚠️ Limitations

- This is a local classroom prototype, not a production-ready campus-wide service.
- Match suggestions are based on similarities between submitted details and may produce incorrect matches.
- A suggested match does not prove ownership of an item.
- The application does not provide a shared, centralized service across multiple devices.
- The quality of match suggestions depends on the accuracy and completeness of the submitted information.

**Privacy note:** Use fictional test data while evaluating the project. Do not enter personal contact information or sensitive details.

## 🔮 Future Enhancements

Potential improvements for future versions include:

- User authentication and role-based access.
- A centralized database for campus-wide access.
- Image uploads for lost and found items.
- Improved text similarity and match-ranking algorithms.
- Email or in-app notifications for potential matches.
- Filters by category, date, location, and report status.
- Automated testing and a documented performance evaluation.
- Deployment to a secure hosting platform for authorized campus users.

These are proposed enhancements and are not claims about the current implementation.

## 🎓 Academic Purpose

This project was developed as part of the **Design and Analysis of Algorithms (DAA) Laboratory** coursework at RGUKT Ongole.

It demonstrates how algorithmic problem-solving can be applied to a practical scenario involving data comparison, keyword searching, scoring, and match prioritization.

The repository can serve as a learning resource for understanding the relationship between algorithm design and application development.

---

**Developed for:** RGUKT Ongole — DAA Lab, Project 5

**Repository:** [daa_lab_assignment](https://github.com/hemanthika1245/daa_lab_assignment)


