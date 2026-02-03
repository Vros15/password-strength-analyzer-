from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

from analyzer.scorer import score_password
from api.schemas import PasswordRequest, PasswordResponse

# Rate limiter (10 requests per minute per IP)
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Password Strength Analyzer API",
    description="Analyzes password strength using entropy and rule-based scoring.",
    version="1.0.0",
)

app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    lambda request, exc: JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Try again later."},
    ),
)

# CORS (locked down)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://roscreations.com",
        "https://www.roscreations.com",
        "http://localhost:5173",
    ],
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/api/password/analyze", response_model=PasswordResponse)
@limiter.limit("10/minute")
def analyze_password(request: Request, data: PasswordRequest):
    return score_password(data.password)
