# Vendor Reliability Intelligence Platform

A full-stack web application for managing vendors, monitoring vendor reliability, tracking procurement and purchase orders, managing contracts, and viewing business insights through an analytics dashboard.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
  - [1. Clone or open the project](#1-clone-or-open-the-project)
  - [2. Configure the MySQL database](#2-configure-the-mysql-database)
  - [3. Set up the backend](#3-set-up-the-backend)
  - [4. Set up the frontend](#4-set-up-the-frontend)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Vendor Search, Sorting, and Pagination](#vendor-search-sorting-and-pagination)
- [Testing](#testing)
- [Security Notes](#security-notes)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)

## Project Overview

The Vendor Reliability Intelligence Platform helps procurement and operations teams organize vendor information and related purchasing activities in one place. It provides a web interface for maintaining vendor records, managing procurement and purchase orders, tracking contract dates and statuses, and reviewing key metrics.

The application uses a React frontend, a FastAPI REST API, and a MySQL database. The frontend communicates with the backend through HTTP requests.

## Features

- **Authentication:** User registration and login. The project has used password validation and JWT-based authentication.
- **Dashboard:** Summary metrics, charts, status breakdowns, top-vendor information, and recent-order information, depending on the available data.
- **Vendor management:** Create, view, update, and delete vendor records.
- **Vendor search and table controls:** Backend search, pagination, and sorting for vendor records.
- **Procurement management:** Manage procurement records and review procurement information.
- **Purchase orders:** Create, view, update, and delete purchase orders, including vendor, item, quantity, pricing, and status fields.
- **Order table controls:** Backend search, pagination, and sorting for order number, vendor name, and item name.
- **Contract management:** Maintain contract records, dates, renewal dates, and status.
- **Notifications:** Display notifications such as low vendor reliability scores and upcoming contract-related alerts, based on backend rules.
- **Reports:** Reports page with export functionality intended for PDF and Excel.
- **Profile management:** View or update supported profile fields.
- **Responsive UI components:** Material UI components for forms, tables, alerts, dialogs, and pagination.

> Feature availability depends on the routes, components, database schema, and export libraries currently present in your local project. Verify each feature in your environment before presenting it as production-ready.

## Technology Stack

### Frontend
- React
- Vite
- JavaScript
- Material UI (MUI)
- React Router
- Axios (or the API client configured in `src/services/api.js`)

### Backend
- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- JWT authentication libraries, if configured in the project

### Database
- MySQL

## Architecture

```text
User
 |
 v
React + Vite Frontend
(Material UI pages and components)
 |
 | HTTP / REST API
 v
FastAPI Backend
(Routes, schemas, validation)
 |
 | SQLAlchemy ORM
 v
MySQL Database
```

## Project Structure

The structure below is representative of the files discussed during development. Your local project may contain additional files or slightly different names.

```text
vendor-reliability-platform/
├── backend/
│   ├── app/
│   │   └── database.py
│   ├── models/
│   │   ├── vendor.py
│   │   ├── order.py
│   │   └── contract.py
│   ├── schemas/
│   │   ├── vendor_schema.py
│   │   ├── order_schema.py
│   │   └── profile_schema.py
│   ├── routes/
│   │   ├── vendor_routes.py
│   │   ├── order_routes.py
│   │   ├── dashboard_routes.py
│   │   ├── notification_routes.py
│   │   └── profile_routes.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env                  # Create locally; do not commit secrets
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── VendorTable.jsx
│   │   │   ├── VendorForm.jsx
│   │   │   ├── OrderTable.jsx
│   │   │   ├── OrderForm.jsx
│   │   │   ├── Topbar.jsx
│   │   │   └── NotificationMenu.jsx
│   │   ├── pages/
│   │   │   ├── Vendors.jsx
│   │   │   ├── Orders.jsx
│   │   │   ├── Reports.jsx
│   │   │   └── Dashboard.jsx
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   ├── vendorService.js
│   │   │   ├── orderService.js
│   │   │   └── notificationService.js
│   │   └── ...
│   ├── package.json
│   └── .env                  # Optional frontend environment configuration
│
└── README.md
```

## Prerequisites

Install the following before running the project:

- Python 3.10 or a compatible version supported by your dependencies
- Node.js and npm
- MySQL Server
- Git (optional)

Check installed versions:

```bash
python --version
node --version
npm --version
mysql --version
```

## Installation and Setup

### 1. Clone or open the project

If the repository is hosted on GitHub:

```bash
git clone <YOUR_REPOSITORY_URL>
cd vendor-reliability-platform
```

Alternatively, open your existing local project folder.

### 2. Configure the MySQL database

Open MySQL and create the database used by your application. For example:

```sql
CREATE DATABASE vendor_platform;
```

Use the database name configured in `backend/app/database.py` or your environment configuration. Ensure that your MySQL user has the necessary permissions.

Do not publish database passwords or other credentials in this README.

### 3. Set up the backend

Open a terminal in the `backend` directory.

#### Windows PowerShell

```powershell
cd backend
py -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks virtual-environment activation, use Command Prompt:

```bat
venv\Scripts\activate.bat
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If the project does not yet have a `requirements.txt`, create one from the active environment after confirming the required packages:

```bash
pip freeze > requirements.txt
```

Configure the database connection and any authentication settings in the location expected by your application. If using a `.env` file, add it to `.gitignore` and load it explicitly in the backend.

Example configuration values (adapt names to the settings used by your code):

```env
DATABASE_URL=mysql+pymysql://YOUR_DB_USER:YOUR_DB_PASSWORD@localhost:3306/vendor_platform
SECRET_KEY=replace_with_a_long_random_secret
```

Install the MySQL driver required by your configured connection URL. For example, a `mysql+pymysql://` URL requires PyMySQL:

```bash
pip install pymysql
```

Start the API from the directory and module path appropriate to your project. If `main.py` is in `backend/`:

```bash
uvicorn main:app --reload
```

If your application entry point is `backend/app/main.py`, run the corresponding module instead, for example:

```bash
uvicorn app.main:app --reload
```

Do not run both commands; use the one that matches your actual entry-point file.

The API is commonly available at:

- API base: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

These URLs assume the default local Uvicorn host and port.

### 4. Set up the frontend

Open a second terminal:

```bash
cd frontend
npm install
```

If the API client uses an environment variable for the backend URL, configure the variable expected by `src/services/api.js`. For example, if the client reads `VITE_API_BASE_URL`:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

If your `api.js` hard-codes the API base URL or uses a differently named variable, keep its configuration consistent rather than adding an unused variable.

Start the frontend:

```bash
npm run dev
```

Vite commonly serves the application at `http://localhost:5173`. Open the URL printed in your terminal.

## Running the Application

1. Start MySQL.
2. Start the FastAPI backend.
3. Start the Vite frontend in a separate terminal.
4. Open the frontend URL shown by Vite.
5. Register or log in using the application's authentication flow.
6. Use the navigation menu to access the available modules.

Keep the backend and frontend terminals running while using the application.

## API Endpoints

The following endpoints have been discussed or implemented during development. Confirm the exact paths and request schemas in Swagger (`/docs`) because route prefixes and authentication requirements can differ by configuration.

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/auth/register` | Register a user |
| `POST` | `/auth/login` | Log in |
| `GET` | `/vendors/` | List vendors; supports pagination, search, and sorting in the upgraded route |
| `POST` | `/vendors/` | Create a vendor |
| `GET` | `/vendors/{vendor_id}` | Retrieve a vendor |
| `PUT` | `/vendors/{vendor_id}` | Update a vendor |
| `DELETE` | `/vendors/{vendor_id}` | Delete a vendor |
| `GET` | `/orders/` | List purchase orders; supports pagination, search, and sorting in the upgraded route |
| `POST` | `/orders/` | Create a purchase order |
| `GET` | `/orders/{order_id}` | Retrieve a purchase order |
| `PUT` | `/orders/{order_id}` | Update a purchase order |
| `DELETE` | `/orders/{order_id}` | Delete a purchase order |
| `GET` | `/notifications/` | Retrieve notifications |
| `GET` / `PUT` | `/profile/` | Retrieve or update profile information, if configured |
| `GET` | `/dashboard/...` | Dashboard data; exact route depends on router configuration |
| `GET` | `/reports/...` | Report/export endpoints, if implemented |

### Example: Vendor pagination, search, and sorting

First page, 10 records:

```http
GET /vendors/?page=1&size=10
```

Search for vendors matching “abc”:

```http
GET /vendors/?page=1&size=10&search=abc
```

Sort vendor names in descending order:

```http
GET /vendors/?page=1&size=10&sort=vendor_name&order=desc
```

The upgraded list endpoint returns a response shaped like:

```json
{
  "total": 52,
  "page": 1,
  "size": 10,
  "data": [
    {
      "id": 1,
      "vendor_name": "Example Vendor",
      "company_name": "Example Company",
      "email": "vendor@example.com",
      "phone": "0000000000",
      "address": "Example City",
      "category": "Electronics"
    }
  ]
}
```

This is an illustrative response. The fields returned depend on the actual `VendorResponse` schema and database records.

### Example: Purchase-order search and sorting

```http
GET /orders/?page=1&size=10&search=example&sort=order_number&order=asc
```

The order search implemented for this project matches order number, vendor name, and item name. Confirm the route's current response shape before using it in other clients.

## Vendor Search, Sorting, and Pagination

The Vendors page uses backend-driven table controls:

- **Search:** Sends the search term to the API.
- **Pagination:** Requests a specific page and page size from the backend.
- **Sorting:** Requests a supported model column and ascending or descending order.
- **CRUD refresh:** Reloads the table after create, update, and delete operations.

The Orders page follows the same general pattern for order number, vendor, and item. The frontend expects the list endpoints to return a paginated object containing `total` and `data`, rather than a plain list.

## Testing

### API tests

1. Start the backend.
2. Open `http://127.0.0.1:8000/docs`.
3. Test registration and login with valid request bodies.
4. Create a test vendor and purchase order.
5. Verify list, detail, update, and delete operations.
6. Test vendor and order search, sorting, and pagination.
7. Test notification, profile, dashboard, and report endpoints that exist in the current build.

### Frontend tests

1. Start the frontend with `npm run dev`.
2. Verify login and registration.
3. Create, edit, and delete a vendor.
4. Search vendors and change table pages and sorting.
5. Create, edit, and delete a purchase order.
6. Test order search, pagination, and sorting.
7. Open the dashboard and check whether the cards and charts load.
8. Open the notification menu and Reports page.
9. Check the browser console and backend terminal for errors.

Use test records and a development database while validating destructive operations.

## Security Notes

- Never commit `.env` files, database credentials, JWT secrets, access tokens, or real user passwords.
- Use a long, randomly generated secret key for token signing.
- Store passwords using a suitable password-hashing algorithm; never store plaintext passwords.
- Validate and authorize protected endpoints on the backend, not only in the frontend.
- Restrict CORS to trusted frontend origins in production.
- Use HTTPS and secure environment variables in deployment.
- Apply database migrations or a controlled schema-management process when changing models.
- Back up the database before making schema or data changes.
- Review sort-field allowlists and input validation before exposing endpoints publicly.

## Troubleshooting

### Backend cannot connect to MySQL
- Check that MySQL is running.
- Confirm database name, username, password, host, and port.
- Confirm that the configured SQLAlchemy driver is installed.
- Check the connection URL used by `app/database.py`.

### Frontend cannot reach the API
- Confirm the backend is running on the configured host and port.
- Check the base URL in `frontend/src/services/api.js`.
- Verify CORS settings in FastAPI.
- Inspect the browser Network tab for the request URL, status code, and response body.

### List page crashes after adding pagination
- Confirm the endpoint returns an object with `data` and `total`.
- Confirm the frontend reads `response.data.data` and `response.data.total`.
- A plain array response is incompatible with that frontend response shape.

### A table column is blank
- Compare the frontend field name with the SQLAlchemy model and Pydantic response schema. For example, the vendor field is `vendor_name`, not necessarily `name`.

### Swagger returns a validation error
- Check the request body against the Pydantic schema shown in Swagger.
- Send fields at the expected top level and use the correct types.
- Inspect the backend terminal traceback for server-side errors.

## Future Enhancements

Potential improvements include:

- Automated backend and frontend tests
- Role-based authorization and audit logs
- Improved loading, error, and empty states
- Debounced search and consistent pagination across all modules
- Date-range and status filters for reports
- Read/unread notification states and timestamps
- Database migrations and seed data
- Docker-based local development
- CI/CD and deployment configuration
- Production logging, monitoring, backups, and rate limiting

## License

Add the license appropriate to your project before distributing it publicly.
