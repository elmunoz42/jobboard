# Job Board

A Django-based application for tracking job applications, managing resumes and cover letters, and organizing your job search.

## Features

- Track job listings with detailed information including:
  - Company details
  - Salary ranges
  - Work type (remote, hybrid, on-site)
  - Application status
  - Distance from a given location
- Manage multiple versions of resumes and cover letters in Markdown format
- Link specific resumes and cover letters to job applications
- Track application status and notes
- Admin interface for easy data management
- Database viewer support via DB Browser for SQLite

## Installation

1. Ensure Python is installed:
```bash
python --version
```

2. Create a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install django
```

4. Create database structure:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create an admin user:
```bash
python manage.py createsuperuser
```

## Project Structure

```
jobboard/                  # Root project directory
    ├── jobboard/         # Project settings directory
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── jobs/            # Application directory
    │   ├── __init__.py
    │   ├── models.py
    │   ├── views.py
    │   └── admin.py
    ├── resumes/        # Resume and cover letter storage
    │   ├── resumes/
    │   └── coverletter_templates/
    ├── manage.py
    └── venv/           # Virtual environment
```

## Usage

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the admin interface at http://127.0.0.1:8000/admin

3. Add companies and job listings through the admin interface

4. Store resume and cover letter files in Markdown format in the respective directories:
   - Resumes: `resumes/resumes/`
   - Cover Letters: `resumes/coverletter_templates/`

## Database Management

The application uses SQLite as its database, stored in `db.sqlite3`. You can:

1. View the database using DB Browser for SQLite
2. Create backups:
```bash
# Simple file copy
cp db.sqlite3 db.sqlite3.backup

# Or using Django's data dump
python manage.py dumpdata --indent 2 > backup.json
```

3. Restore from backup:
```bash
python manage.py loaddata backup.json
```

## Resume and Cover Letter Management

- Store resume files in `resumes/resumes/` directory
- Store cover letter templates in `resumes/coverletter_templates/` directory
- Files should be in Markdown format for version control and easy editing
- Link files to job applications through the admin interface

## Contributing

This is a personal project, but feel free to fork and modify for your own use.

## License

This project is for personal use and is not licensed for distribution.