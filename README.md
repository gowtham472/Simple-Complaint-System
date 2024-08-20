# Complaint Management System

This is a simple command-line application for managing customer complaints using SQLite as the database. The application allows users to register new complaints and update the status of existing complaints.

## Features

- **Register a New Complaint**: Users can enter their name and complaint, which will be stored in the database with a unique ID.
- **Update Complaint Status**: Users can update the status of their complaints to "RESOLVED" by providing their name and complaint ID.
- **Database**: Complaints are stored in an SQLite database (`Complaints.db`).

## Prerequisites

- Python 3.x
- SQLite (included with Python)

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gowtham472/Simple-Complaint-System.git

2. **Navigate to the project directory**:
    cd complaints

4. **Run the script**:
    python complaints.py

## Usage

When you run the script, you will be presented with three options:

1. New Complaint: Enter your name and complaint to register it in the system. You will receive a unique complaint ID.
2. Change Status: Enter your name and complaint ID to mark the complaint as "RESOLVED".
3. Exit: Close the application.

## Database Structure

The application uses a single table named complain with the following fields:

-**ID**: An auto-incrementing integer that uniquely identifies each complaint.
-**customername**: The name of the customer filing the complaint.
-**complaint**: The text of the complaint.
-**status**: The status of the complaint, either "UNRESOLVED" (default) or "RESOLVED".




