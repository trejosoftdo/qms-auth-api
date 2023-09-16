# Install dependencies
Run the following command: `pip install --no-cache-dir --upgrade -r requirements/base.txt`

# Run it!  - Development - 
Run live server with the following command {Inside src folder}: `uvicorn main:app --reload`

The command uvicorn main:app refers to:
* main: the file main.py (the Python "module").
* app: the object created inside of main.py with the line app = FastAPI().
* --reload: make the server restart after code changes. Only use for development.

Open your browser at http://127.0.0.1:8000