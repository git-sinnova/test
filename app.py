from fastapi import FastAPI, Request
from supabase import create_client
from passlib.hash import bcrypt

SUPABASE_URL = "https://laoakyhmwczlaiozkobb.supabase.co"
SUPABASE_KEY = "YeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxhb2FreWhtd2N6bGFpb3prb2JiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk1MTE1MDUsImV4cCI6MjA3NTA4NzUwNX0.veWiYwCklBZurc0AGCIsxt21NDnpzpeiKZNHJimEELY"  
# server-side key
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

@app.post("/signup")
async def signup(request: Request):
    data = await request.json()
    company_name = data.get("company_name")
    cnpj = data.get("cnpj")
    password = data.get("password")

    # Hash password before saving
    hashed_password = bcrypt.hash(password)

    # Insert into Supabase
    supabase.table("companies").insert({
        "company_name": company_name,
        "cnpj": cnpj,
        "password": hashed_password
    }).execute()

    return {"status": "success"}
