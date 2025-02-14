To run Locally:

Frontend:
Terminal1->
  cd Frontend
  npm install
  npm run dev

Backend:
In the Backend directory, create a .env file and fill the data for API_KEY and DATABASE_URL
Terminal2->
  cd Backend
  python -m venv env
  env/Scripts/activate
  pip install -r requirements.txt
  alembic upgrade head (applying migrations, to sync with the database)
  uvicorn main:app

  

