
import re
from typing import Tuple

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Module 1 - Session 1 API", version="1.0.0")


# -----------------------------
# Schemas (Pydantic models)
# -----------------------------

class NormalizeTextRequest(BaseModel):
    text: str
    lowercase: bool = False


class NormalizeTextResponse(BaseModel):
    normalized_text: str
    char_count: int
    word_count: int


# -----------------------------
# Services (business logic)
# -----------------------------

def _collapse_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def normalize_text(text: str, lowercase: bool = False) -> Tuple[str, int, int]:
    """Deterministic text normalization.

    Design notes:
    - Keep this function pure-ish (no global state, no I/O).
    - This style is easy to test and safe to reuse in pipelines.
    """
    if lowercase:
        text = text.lower()

    normalized = _collapse_whitespace(text)
    char_count = len(normalized)
    word_count = 0 if not normalized else len(normalized.split(" "))
    return normalized, char_count, word_count


# -----------------------------
# Routes (API boundary)
# -----------------------------

@app.post("/normalize-text", response_model=NormalizeTextResponse)
def post_normalize_text(payload: NormalizeTextRequest) -> NormalizeTextResponse:
    normalized, char_count, word_count = normalize_text(
        text=payload.text,
        lowercase=payload.lowercase,
    )
    return NormalizeTextResponse(
        normalized_text=normalized,
        char_count=char_count,
        word_count=word_count,
    )
