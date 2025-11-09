# Setup guide - Demo Playwright Mocking

## Prerequisites
- Node.js v18+ 
- Python 3.8+
- Angular CLI: `npm install -g @angular/cli`

---

## BACKEND (FastAPI)

### Step 1: Create the project and virtualenv
```bash
cd playwright-demo-backend

# Create virtualenv
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 2: Install dependencies
```bash
# Recommended option (install all dependencies)
pip install "fastapi[all]"

# Or install them separetely:
pip install fastapi uvicorn pydantic
```

### Step 3: Execute backend server
```bash
python main.py
```

**Verify the server is running:** 
- API: http://localhost:8000
- Users Endpoint: http://localhost:8000/api/users
- Products Endpoint: http://localhost:8000/api/products
- Docs: http://localhost:8000/docs
---

## FRONTEND (Angular)

### Step 1: Create the project
```bash
ng new playwright-demo-app
# Select:
# - Routing: Yes
# - Stylesheet: CSS
# - SSR: No
```

### Paso 2: Install AG-Grid
```bash
cd playwright-demo-app
npm install ag-grid-angular ag-grid-community --legacy-peer-deps
```

> **Note**: If you have problems with the versions, use these specific ones:
```bash
npm install ag-grid-angular@32.2.1 ag-grid-community@32.2.1 --legacy-peer-deps
```

## TESTING (pytest + BDD)

This project uses **pytest** with **pytest-bdd** for tests in Gherkin (BDD) format.

### Step 1: Install test dependencies

```bash
# Option 1: Use the script
./install_test_dependencies.sh

# Option 2: Manual
pip install -r requirements.txt
playwright install chromium
```

### Step 2: Test Structure

```
tests/
├── features/              # .feature files (Gherkin)
│   ├── users.feature
│   ├── products.feature
│   └── images.feature
├── step_defs/            # Step definitions (implementations)
│   ├── common_steps.py
│   ├── users_steps.py
│   ├── products_steps.py
│   └── images_steps.py
├── test_bdd_*.py         # Files that import scenarios
├── test_*.py             # Traditional tests
└── conftest.py           # pytest configuration
```

### Step 3: Run Tests

**All tests:**
```bash
pytest tests/ -v -s
```

**BDD tests only (Gherkin):**
```bash
pytest tests/test_bdd_*.py -v -s
```

**Traditional tests:**
```bash
pytest tests/test_users.py tests/test_products.py tests/test_images.py -v -s
```

**Specific test:**
```bash
pytest tests/test_bdd_users.py::test_display_users_with_no_records -v -s
```

**By marker:**
```bash
pytest -m users -v -s
pytest -m images -v -s
```

### Environments

**Local (default):**
```bash
pytest tests/ -v -s
```

**Production:**
```bash
pytest tests/ --env=prod -v -s
```
