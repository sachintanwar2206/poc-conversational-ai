import os
from datetime import date
from supabase import create_client, Client
from fastapi import FastAPI

app = FastAPI()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

#app.get("/user")(lambda: {"Hello": "World"})

# Fetch user
@app.get("/user")
def get_user(last4ssn: int, dob: date, zip_code: int):
    user = (
        supabase.from_("users")
        .select("name, user_recent_payments(amount, received_date, method, coverage_month), user_pending_payments(amount, due_date, coverage_month), user_coverages(monthly_premium, user_coverage_plans(plan_name, coverage))")
        .eq("last4ssn", last4ssn)
        .eq("dob", dob)
        .eq("zip_code", zip_code)
        .execute()
    )
    return user.data
