import os
from datetime import date
from supabase import create_client, Client
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# Define a request model for the POST API
class UserRequest(BaseModel):
    last4ssn: int
    dob: date
    zip_code: int
    
# Define a response model for the POST API
class UserResponse(BaseModel):
    toolCallId: str
    result: object

# POST API to fetch user
@app.post("/user")
async def post_user(req: Request):
    req_json = await req.json()
    tool_call = req_json["message"]["toolCalls"][0]
    payload = tool_call["function"]["arguments"]
    user_request = UserRequest(last4ssn=payload["last4ssn"], dob=payload["dob"], zip_code=payload["zip_code"])
    user = (
        supabase.from_("users")
        .select("name, user_recent_payments(amount, received_date, method, coverage_month), user_pending_payments(amount, due_date, coverage_month), user_coverages(monthly_premium, user_coverage_plans(plan_name, coverage))")
        .eq("last4ssn", user_request.last4ssn)
        .eq("dob", user_request.dob)
        .eq("zip_code", user_request.zip_code)
        .execute()
    )
    return UserResponse(toolCallId=str(tool_call["id"]), result=user.data[0])