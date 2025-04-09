# Golden Crop Distributors Ltd. (GCDL) - Web Application

## Overview

This project is a web application designed to modernize the operations of Golden Crop Distributors Ltd. (GCDL), a leading wholesale produce distributor. The system manages **procurement**, **sales**, **stock**, and **analytics** to replace the manual record-keeping process. This application was developed using **Django** for the backend and integrates with **PostgreSQL** as the database.

## Features

- **Procurement Management**: Record produce details, dealers, tonnage, cost, etc.
- **Sales Management**: Record sales details and generate receipts.
- **Credit Sales Management**: Manage credit sales with buyer information, due amounts, and produce details.
- **Stock Management**: Automatically update stock after sales and allow edits.
- **Analytics & Reporting**: Generate interactive reports (PDF, Excel, CSV) for credit sales, stock, sales trends, and more.
- **Role-based Access**: Admins, Managers, and Sales Agents have role-specific permissions for different functionalities.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Folder Structure](#folder-structure)
- [Endpoints](#endpoints)
- [Authentication](#authentication)
- [Reporting](#reporting)
- [Contributing](#contributing)
- [License](#license)

---

## Technologies Used

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Frontend**: (Planned for React integration, if needed)
- **Authentication**: JWT Authentication with **Django REST Framework (DRF)**
- **Reporting**: `pandas`, `xhtml2pdf` for Excel and PDF report generation
- **Environment**: Python 3.9+, PostgreSQL

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/gcdl-backend.git
cd gcdl-backend
```

### 2. Set up a virtual environment

```bash
python -m venv gcdl_env
source gcdl_env/bin/activate  # For Windows: gcdl_env\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

Create a **PostgreSQL** database and configure the database settings in `gcdl_backend/settings.py`.

```bash
# Example for PostgreSQL configuration in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gcdl_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional for accessing admin panel)

```bash
python manage.py createsuperuser
```

---

## Running the Project

### 1. Start the server

```bash
python manage.py runserver
```

Your backend should now be running at `http://127.0.0.1:8000/`.

---

## Folder Structure

```
gcdl_backend/
│
├── gcdl_backend/        # Project settings and configurations
│   ├── __init__.py
│   ├── settings.py      # Database, app settings, JWT config
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py
│
├── users/               # User management (authentication, roles)
│   ├── models.py        # Custom User model
│   ├── views.py         # Register, login, user details
│   ├── serializers.py   # User serializers
│   └── urls.py          # User URLs (login, register)
│
├── inventory/           # Procurement and stock management
│   ├── models.py        # Produce, procurement, and stock models
│   ├── views.py         # Procurement management
│   ├── serializers.py   # Procurement and stock serializers
│   └── urls.py          # Procurement and stock URLs
│
├── sales/               # Sales and credit sales management
│   ├── models.py        # Sales and CreditSales models
│   ├── views.py         # Sales management
│   ├── serializers.py   # Sales serializers
│   └── urls.py          # Sales URLs
│
├── reports/             # Reporting and Analytics
│   ├── views.py         # Excel and PDF report generation
│   ├── urls.py          # Report endpoints
│
└── requirements.txt     # Project dependencies
```

---

## Endpoints

### User Endpoints
- **POST** `/api/users/register/` – Register a new user (Manager, Sales Agent, CEO)
- **POST** `/api/users/login/` – Login (Returns JWT token)
- **GET** `/api/users/me/` – Get logged-in user details

### Procurement Endpoints
- **GET** `/api/procurements/` – Get all procurements
- **POST** `/api/procurements/` – Create a new procurement

### Sales Endpoints
- **GET** `/api/sales/` – Get all sales
- **POST** `/api/sales/` – Create a new sale

### Credit Sales Endpoints
- **GET** `/api/credit-sales/` – Get all credit sales
- **POST** `/api/credit-sales/` – Create a new credit sale

### Report Endpoints
- **GET** `/api/reports/sales/excel/` – Generate an Excel report for sales
- **GET** `/api/reports/procurement/excel/` – Generate an Excel report for procurements
- **GET** `/api/reports/credit-sales/excel/` – Generate an Excel report for credit sales
- **GET** `/api/reports/summary/excel/` – Generate a summary dashboard export for a specific date range

---

## Authentication

- This project uses **JWT Authentication** to secure the endpoints.
- After registering or logging in, use the **JWT token** in the `Authorization` header like this:

```
Authorization: Bearer <your_token_here>
```

---

## Reporting

The backend supports **Excel and PDF reports** for the following:

- **Sales Report**: Export sales records (with optional filters like date range, agent)
- **Procurement Report**: Export procurement records (with optional filters like branch, date range)
- **Credit Sales Report**: Export credit sales records (with optional filters)
- **Summary Report**: Monthly summary with total sales, procurements, and more

### Export Options:
- Excel (`.xlsx`)
- PDF (`.pdf`)

Reports are filtered based on query parameters like `start_date`, `end_date`, and `agent`.

---

## Contributing

1. **Fork the repository** and clone it to your local machine.
2. Create a **feature branch** for any new work:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes** and push to your fork:
   ```bash
   git commit -am "Added new feature"
   git push origin feature-name
   ```
4. **Submit a Pull Request** to merge changes into the main branch.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
