from pydantic import BaseModel, Field


class PasswordRequest(BaseModel):
    password: str = Field(
        min_length=1,
        description="Password to analyze (not stored or logged)"
    )


class PasswordResponse(BaseModel):
    score: int
    rating: str
    entropy_bits: float
    crack_time_estimate: dict
    issues: list[str]
