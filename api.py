# #!/usr/bin/env python3
# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import List, Optional

# # Import your refactored core functions
# from birth_chart.main_birth_chart_interpretation import compute_birth_chart
# from compatibility.main_compatibility import run_compatibility
# from prediction.main_transit_interpretation import run_transits

# app = FastAPI(
#     title="Astrology API v2",
#     description="Astrology endpoints: birth-chart, compatibility, transit",
# )

# # CORS: allow your frontend origin
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["https://teal-brioche-d37e12.netlify.app"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Pydantic models for request bodies
# class BirthInfo(BaseModel):
#     name: Optional[str] = None
#     birth_date: List[int]    # [YYYY, MM, DD]
#     birth_time: List[int]    # [HH, MM, SS]
#     birth_place: str
#     gender: Optional[str] = "other"
#     lat: Optional[float] = None
#     lng: Optional[float] = None
#     tz_str: Optional[str] = None

# class CompatRequest(BaseModel):
#     person1: BirthInfo
#     person2: BirthInfo

# class TransitRequest(BaseModel):
#     user: BirthInfo
#     period: Optional[List[str]] = ["today","tomorrow","week-end","month-end","year-end"]

# @app.post("/birth-chart")
# def api_birth_chart(req: BirthInfo):
#     try:
#         data = compute_birth_chart(
#             tuple(req.birth_date),
#             tuple(req.birth_time),
#             req.birth_place,
#             gender=req.gender or "other"
#         )
#         return {"status": "success", "data": data}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/compatibility")
# def api_compat(req: CompatRequest):
#     try:
#         # Map Pydantic model to run_compatibility expected dict
#         p1 = {
#             "name":        req.person1.name or "Person1",
#             "birth_date":  tuple(req.person1.birth_date),
#             "birth_time":  tuple(req.person1.birth_time),
#             "birth_place": req.person1.birth_place,
#             "lat":         req.person1.lat,
#             "lng":         req.person1.lng,
#             "tz_str":      req.person1.tz_str
#         }
#         p2 = {
#             "name":        req.person2.name or "Person2",
#             "birth_date":  tuple(req.person2.birth_date),
#             "birth_time":  tuple(req.person2.birth_time),
#             "birth_place": req.person2.birth_place,
#             "lat":         req.person2.lat,
#             "lng":         req.person2.lng,
#             "tz_str":      req.person2.tz_str
#         }
#         result = run_compatibility(p1, p2)
#         return {"status": "success", "data": result}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/transit")
# def api_transit(req: TransitRequest):
#     try:
#         # Map Pydantic model to run_transits expected dict
#         user = {
#             "name":         req.user.name or "User",
#             "birth_year":   req.user.birth_date[0],
#             "birth_month":  req.user.birth_date[1],
#             "birth_day":    req.user.birth_date[2],
#             "birth_hour":   req.user.birth_time[0],
#             "birth_minute": req.user.birth_time[1],
#             "birth_city":   req.user.birth_place,
#             "latitude":     req.user.lat,
#             "longitude":    req.user.lng,
#             "timezone_str": req.user.tz_str
#         }
#         result = run_transits(user, periods=req.period)
#         return {"status": "success", "data": result}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # For local testing only
# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")


#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
# Import your refactored core functions
from birth_chart.main_birth_chart_interpretation import compute_birth_chart
from compatibility.main_compatibility import run_compatibility
from prediction.main_transit_interpretation import run_transits
# Import timezone helper
from timezone_helper import timezone_helper

app = FastAPI(
    title="Astrology API v2",
    description="Astrology endpoints: birth-chart, compatibility, transit",
)
# CORS: allow your frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://teal-brioche-d37e12.netlify.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# Pydantic models for request bodies
class BirthInfo(BaseModel):
    name: Optional[str] = None
    birth_date: List[int]    # [YYYY, MM, DD]
    birth_time: List[int]    # [HH, MM, SS]
    birth_place: str
    gender: Optional[str] = "other"
    lat: Optional[float] = None
    lng: Optional[float] = None
    tz_str: Optional[str] = None
class CompatRequest(BaseModel):
    person1: BirthInfo
    person2: BirthInfo
class TransitRequest(BaseModel):
    user: BirthInfo
    period: Optional[List[str]] = ["today","tomorrow","week-end","month-end","year-end"]
def enrich_birth_info_with_timezone(birth_info: BirthInfo) -> BirthInfo:
    """Auto-calculate tz_str from lat/lng if missing."""
    if birth_info.lat is not None and birth_info.lng is not None and not birth_info.tz_str:
        birth_info.tz_str = timezone_helper.get_timezone_with_fallback(
            birth_info.lat,
            birth_info.lng,
            fallback="UTC"
        )
    return birth_info
@app.post("/birth-chart")
def api_birth_chart(req: BirthInfo):
    try:
        # Enrich with timezone if needed
        req = enrich_birth_info_with_timezone(req)
        
        # Pass coordinates and timezone into core function
        data = compute_birth_chart(
            tuple(req.birth_date),
            tuple(req.birth_time),
            req.birth_place,
            tz_str=req.tz_str,
            lat=req.lat,
            lng=req.lng,
            gender=req.gender or "other"
        )
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/compatibility")
def api_compat(req: CompatRequest):
    try:
        # Enrich both persons with timezone if needed
        req.person1 = enrich_birth_info_with_timezone(req.person1)
        req.person2 = enrich_birth_info_with_timezone(req.person2)
        
        # Map Pydantic model to run_compatibility expected dict
        p1 = {
            "name":        req.person1.name or "Person1",
            "birth_date":  tuple(req.person1.birth_date),
            "birth_time":  tuple(req.person1.birth_time),
            "birth_place": req.person1.birth_place,
            "lat":         req.person1.lat,
            "lng":         req.person1.lng,
            "tz_str":      req.person1.tz_str
        }
        p2 = {
            "name":        req.person2.name or "Person2",
            "birth_date":  tuple(req.person2.birth_date),
            "birth_time":  tuple(req.person2.birth_time),
            "birth_place": req.person2.birth_place,
            "lat":         req.person2.lat,
            "lng":         req.person2.lng,
            "tz_str":      req.person2.tz_str
        }
        result = run_compatibility(p1, p2)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/transit")
def api_transit(req: TransitRequest):
    try:
        # Enrich user with timezone if needed
        req.user = enrich_birth_info_with_timezone(req.user)
        
        # Map Pydantic model to run_transits expected dict
        user = {
            "name":         req.user.name or "User",
            "birth_year":   req.user.birth_date[0],
            "birth_month":  req.user.birth_date[1],
            "birth_day":    req.user.birth_date[2],
            "birth_hour":   req.user.birth_time[0],
            "birth_minute": req.user.birth_time[1],
            "birth_city":   req.user.birth_place,
            "latitude":     req.user.lat,
            "longitude":    req.user.lng,
            "timezone_str": req.user.tz_str
        }
        result = run_transits(user, periods=req.period)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# For local testing only
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")