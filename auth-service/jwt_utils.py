import jwt
import datetime

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
TOKEN_EXP_MIN = 30

def create_token(username: str, role: str = "viewer"):
    payload = {
        "sub": username,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXP_MIN),
        "iat": datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
