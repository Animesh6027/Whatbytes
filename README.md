### Healthcare Backend (Django + DRF + PostgreSQL + JWT)

A simple healthcare backend with user auth (JWT), Patients, Doctors, and Patient–Doctor mappings.

### Requirements
- Python 3.10+
- PostgreSQL 12+
- PowerShell (Windows) or bash (macOS/Linux)

### Setup
1) Clone and create venv
```powershell
cd D:\Whatbytes
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -U pip setuptools wheel
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary python-dotenv
```

2) Environment variables
Create `D:\Whatbytes\.env`:
```ini
DJANGO_SECRET_KEY=change-this-in-production
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
POSTGRES_DB=healthcare_backend
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

3) Database and migrations
- Ensure you created a PostgreSQL database named `healthcare_backend` (or change POSTGRES_DB).
```powershell
.\.venv\Scripts\python manage.py makemigrations
.\.venv\Scripts\python manage.py migrate
```

4) Run server
```powershell
.\.venv\Scripts\python manage.py runserver
```
- Root: `http://127.0.0.1:8000/` (JSON index of endpoints)

### Tech Stack
- Django 5
- Django REST Framework
- SimpleJWT (Bearer tokens)
- PostgreSQL
- python-dotenv for env vars

### Authentication
- Register: POST `/api/auth/register/`
  - Body:
  ```json
  { "name": "John Doe", "email": "john@example.com", "password": "Passw0rd!" }
  ```
  - Returns: `access`, `refresh` tokens
- Login: POST `/api/auth/login/`
  - Body:
  ```json
  { "email": "john@example.com", "password": "Passw0rd!" }
  ```
  - Returns: `access`, `refresh`

Use on protected routes:
- Header: `Authorization: Bearer <access_token>`

### Patients (owner-scoped; auth required)
- Create: POST `/api/patients/`
```json
{ "name": "Alice Smith", "age": 32, "gender": "female", "address": "123 Health St" }
```
- List (mine): GET `/api/patients/`
- Retrieve: GET `/api/patients/{id}/`
- Update: PUT `/api/patients/{id}/`
- Delete: DELETE `/api/patients/{id}/`

### Doctors
- List (public): GET `/api/doctors/`
- Retrieve (public): GET `/api/doctors/{id}/`
- Create (auth): POST `/api/doctors/`
```json
{ "name": "Dr. Amy Wong", "specialization": "Cardiology", "email": "amy@example.com", "phone": "555-1234" }
```
- Update (auth): PUT `/api/doctors/{id}/`
- Delete (auth): DELETE `/api/doctors/{id}/`

### Patient–Doctor Mappings (auth required)
- Create: POST `/api/mappings/`
```json
{ "patient": 1, "doctor": 1 }
```
- List all: GET `/api/mappings/`
- List by patient: GET `/api/mappings/{patient_id}/`
- Delete: DELETE `/api/mappings/{id}/`

### Quick Postman Flow
1) Register or Login → copy `access`
2) Create a Patient (with token)
3) Create a Doctor (with token)
4) Create a Mapping (with token)
5) List Mappings (with token)

### Common Issues
- 401 Unauthorized: Missing/invalid `Authorization: Bearer <access>`. Ensure you use the access, not refresh token.
- Token invalid: If you changed `DJANGO_SECRET_KEY` or system time is off, log in again.
- 400 on mapping: Ensure the provided `patient` and `doctor` IDs exist. Patients must belong to the logged-in user.
- DB connection: Verify `.env` values match your PostgreSQL user/password/host/port.

### Project Structure (key files)
- `healthcare_backend/settings.py` – env-based config, DRF + JWT
- `healthcare_backend/urls.py` – routes
- `api/models.py` – `Patient`, `Doctor`, `PatientDoctorMapping`
- `api/serializers.py` – serializers incl. auth
- `api/views.py` – auth endpoints, viewsets, index
- `api/admin.py` – admin registration

### Optional Enhancements
- Pagination, ordering, filtering
- Swagger/OpenAPI docs
- CORS headers
- Admin superuser
- Unit tests
