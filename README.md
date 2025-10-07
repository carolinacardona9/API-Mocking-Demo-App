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

## PLAYWRIGHT TESTS

### COMING SOON
