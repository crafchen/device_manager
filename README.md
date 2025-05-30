add
## Device Manager Django Project

### Introduction
This is a Django project for device management. The project supports adding, editing, deleting, and listing devices.

### Requirements
- Python >= 3.8
- Django >= 3.2
- pip

### Installation

1. **Clone the repository**
    ```bash
    git clone <repo-url>
    cd device_manager
    ```

2. **Create a virtual environment and install dependencies**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Apply database migrations**
    ```bash
    python manage.py migrate
    ```

4. **Create an admin account**
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the server**
    ```bash
    python manage.py runserver
    ```

### Usage

- Access the admin site: http://127.0.0.1:8000/admin/
- Add, edit, or delete devices via the admin interface or API (if available).

### API Documentation (Swagger)

- This project uses Swagger for interactive API documentation.
- After running the server, visit: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) to view and test the API endpoints.
- If you do not see the Swagger UI, ensure that `drf-yasg` or a similar package is installed and configured in your project.

### Project Structure

```
device_manager/
├── manage.py
├── device_manager/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── devices/
│   ├── models.py
│   ├── views.py
│   └── ...
└── requirements.txt
```

### Notes

- Make sure all packages in `requirements.txt` are installed.
- You can extend the project with additional APIs or user interfaces as needed.

### Contact

- For questions, please contact via email or create an issue on the repository.
