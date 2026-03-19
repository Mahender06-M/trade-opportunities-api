from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "mysecretkey"

@app.get("/analyze/{sector}")
async def analyze_sector(sector: str, x_api_key: str = Header(None)):
    
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    report = f"""
# Sector: {sector}

## Market Overview
The {sector} sector is growing in India.

## Opportunities
- High demand
- Investment potential

## Risks
- Competition
- Market changes

## Conclusion
Positive outlook
"""

    return {"report": report}
