dev setup:

python3 -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
uvicorn app.main:app --reload