
# 🧮 FastAPI Calculator – Module 8 Assignment

[![CI/CD](https://github.com/Rajat-njit/Module-8/actions/workflows/ci.yml/badge.svg)](https://github.com/Rajat-njit/Module-8/actions/workflows/ci.yml)


A fully functional **FastAPI-based Calculator Web Application** built as part of **Module 8 Assignment**.
It integrates complete **CI/CD automation**, **Docker containerization**, **automated testing**, and **security scanning** — following real-world software engineering practices.

---

## ⚙️ Features

✅ Perform all arithmetic operations: **Addition, Subtraction, Multiplication, Division**
✅ Responsive **Web UI** using **Jinja2 Templates**
✅ **Singleton Logger** implementation for centralized logging
✅ **RESTful Endpoints** for each operation
✅ **Unit, Integration, and E2E tests** with **100% coverage**
✅ Automated **GitHub Actions CI/CD** pipeline
✅ **Dockerized deployment** with vulnerability scanning (Trivy)
✅ Follows clean code architecture and design patterns

---

## 📁 Project Structure

```
Module-8
├── app/
│   ├── __init__.py
│   ├── logger.py               # Singleton Logger class (creates logs/app.log)
│   └── operations/__init__.py  # Core arithmetic logic
│
├── templates/
│   └── index.html              # Web interface (Jinja2)
│
├── static/
│   └── favicon.ico             # Application icon
│
├── tests/
│   ├── unit/                   # Unit tests for core modules
│   ├── integration/            # API-level integration tests
│   ├── e2e/                    # Playwright-based UI tests
│   └── conftest.py
│
├── main.py                     # FastAPI app entry point
├── requirements.txt            # All dependencies
├── Dockerfile                  # Docker container configuration
├── .github/workflows/ci.yml    # GitHub Actions workflow
└── README.md
```

---

## 🧩 Installation & Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Rajat-njit/Module-8.git
cd Module-8
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
# or
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4️⃣ Run the FastAPI app

```bash
uvicorn main:app --reload
```

Now visit 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📦 `requirements.txt` Contents

```
annotated-doc==0.0.3
annotated-types==0.7.0
anyio==4.11.0
certifi==2025.10.5
click==8.3.0
fastapi==0.120.1
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.11
pydantic==2.12.3
pydantic_core==2.41.4
sniffio==1.3.1
starlette==0.48.0
typing-inspection==0.4.2
typing_extensions==4.15.0
uvicorn==0.38.0
playwright>=1.48.0
pytest>=8.3.3
pytest-cov>=6.0.0
pytest-playwright>=0.5.0
requests>=2.32.3
jinja2>=3.1.4
```

---

## 🧪 Testing

### 🧩 Unit & Integration Tests

```bash
pytest --cov=app --cov-report=term-missing
```

### 🌐 End-to-End (E2E) Tests

```bash
pytest tests/e2e -v
```

📈 Expected output:

```
50 passed, 1 xfailed in 6.7s
Coverage: 100 %
```

---

## 🐳 Docker Deployment

### Build Docker image

```bash
docker build -t rajatpednekar/module-8 .
```

### Run container

```bash
docker run -d -p 8000:8000 --name fastapi-calculator rajatpednekar/module-8
```

Open app at: [http://localhost:8000](http://localhost:8000)

Check running containers:

```bash
docker ps
```

---

## 🧠 Design Pattern Map

| Pattern               | Location                       | Purpose                                         |
| --------------------- | ------------------------------ | ----------------------------------------------- |
| **Singleton**         | `app/logger.py`                | Ensures a single shared logger instance         |
| **Factory**           | `app/operations/__init__.py`   | Creates operation logic dynamically             |
| **Observer (Logger)** | `logger` reacts to user events | Captures every API action                       |
| **Facade**            | `main.py`                      | Provides unified interface to API and UI layers |

---

## 🔧 Enhancements Made

| Area                            | Enhancement                                                     |
| ------------------------------- | --------------------------------------------------------------- |
| 🧩 **Logging System**           | Added Singleton-based `AppLogger` with auto log folder creation |
| 🌐 **Frontend**                 | Redesigned calculator layout with improved dark theme           |
| 🧪 **Testing Suite**            | Added Unit + Integration + Playwright-based UI tests            |
| 🧱 **Dockerization**            | Added `Dockerfile` for deployment portability                   |
| 🔁 **CI/CD Pipeline**           | Integrated GitHub Actions workflow with Trivy scanning          |
| 🛡️ **Security Fixes**          | Upgraded `h11` to `0.16.0` to patch CVE-2025-43859              |
| ⚡ **Error Handling**            | Improved division by zero and invalid input messages            |
| 🧩 **Favicon + Static Support** | Added `/static` route and graceful 404 fallback                 |

---

## ⚙️ Continuous Integration (GitHub Actions)

The workflow automates every stage from testing to deployment.

**Workflow file:** `.github/workflows/ci.yml`

### CI/CD Pipeline Steps:

1. 🧰 Setup Python + dependencies
2. ✅ Run Unit, Integration, and E2E tests
3. 🧾 Generate coverage report
4. 🔒 Run **Trivy vulnerability scan**
5. 🐳 Build and push Docker image → `rajatpednekar/module-8:latest`

All builds verified via the badge at the top of this README ✔️

---

## 🧾 Logging

All runtime events are logged in:

```
logs/app.log
```

Sample log entries:

```
2025-10-25 14:33:11 [INFO] Application started.
2025-10-25 14:33:18 [INFO] POST /add | a=5, b=3 | result=8
2025-10-25 14:33:20 [ERROR] Division by zero attempted.
```

---

## 🧩 Security Scanning

Integrated **Trivy Security Action** checks for vulnerabilities in:

* OS-level packages
* Python dependencies

✅ No vulnerabilities found after upgrading to `h11==0.16.0`.

---

## 🏁 Final Results

| Category                             | Result                           |
| ------------------------------------ | -------------------------------- |
| ✅ **App Functionality**              | All operations working correctly |
| ✅ **Logging System**                 | Fully functional & persistent    |
| ✅ **Unit + Integration + E2E Tests** | 100% coverage                    |
| ✅ **GitHub Actions Workflow**        | All stages passed successfully   |
| ✅ **Security Scan**                  | 0 Critical/High vulnerabilities  |
| ✅ **Docker Image**                   | Pushed to Docker Hub             |
| 🌐 **Web App Live Demo**             | Accessible at `localhost:8000`   |

---

## 👤 Author

**Rajat Pednekar**
📍 Master’s in Computer Science – New Jersey Institute of Technology
---

---

Would you like me to make a **shorter “Canvas submission version”** of this (1-page, includes screenshots placeholders + summary) so you can upload that to your LMS along with your code link?
