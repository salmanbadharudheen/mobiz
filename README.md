# Project Name

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/salmanbadharudheen/mobiz
   
2. Navigate to the project directory:
   ```bash 
   cd project-directory
3. Activate the virtual environment
  ```bash
 .\venv\Scripts\activate      # Windows
  source venv/bin/activate     # MacOS/Linux
  ```
4. install dependencies:
  ```bash 
    pip install -r requirements.txt
  ```
5. setup the database
    ```
   python manage.py makemigrations
   python manage.py migrate

   ```
6. start the development server
```
python manage.py runserver
```

