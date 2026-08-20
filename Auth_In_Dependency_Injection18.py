# Auth in Dependency Injection
from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def varify_token(token: str=Header(None)):
    if token != "mysecrettoken":  #If we enter mysecrettoken, it should return the correct output.
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return {
        "user": "Authorized User"
    }
    
    
@app.get("/secure-data")
def secure_data(user = Depends(varify_token)):
    return {
        "message": "Secure data accessed",
        "user":user
    }
            