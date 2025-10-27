"""
main.py
-------
FastAPI application for a simple calculator web app.
Serves a browser-based UI (index.html) and JSON API endpoints.
Uses centralized singleton logger for consistent logging.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.operations import add, subtract, multiply, divide
from app.logger import logger
import math
import os

# -------------------------------------------------------
# Utility: Ensure results are JSON-safe
# -------------------------------------------------------
def sanitize_result(value: float):
    """Ensure results are JSON-safe (finite numbers only)."""
    if not math.isfinite(value):
        return "Infinity or NaN (result too large)"
    return value


# -------------------------------------------------------
# FastAPI App Initialization
# -------------------------------------------------------
app = FastAPI(title="FastAPI Calculator", version="1.0")

templates = Jinja2Templates(directory="templates")

# Serve static folder (ensure it exists)
app.mount("/static", StaticFiles(directory="static"), name="static")

# -------------------------------------------------------
# Favicon route
# -------------------------------------------------------
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    favicon_path = os.path.join("static", "favicon.ico")
    return FileResponse(favicon_path)


# -------------------------------------------------------
# Routes
# -------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """Serve the calculator UI page."""
    logger.info("Serving calculator UI page.")
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/add")
async def perform_addition(payload: dict):
    try:
        a, b = payload.get("a"), payload.get("b")
        result = sanitize_result(add(a, b))
        logger.info(f"Addition: {a} + {b} = {result}")
        return {"result": result}
    except Exception as e:
        logger.error(f"Error in addition: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/subtract")
async def perform_subtraction(payload: dict):
    """Perform subtraction operation."""
    try:
        a, b = payload.get("a"), payload.get("b")
        result = sanitize_result(subtract(a, b))
        logger.info(f"Subtraction: {a} - {b} = {result}")
        return {"result": result}
    except Exception as e:
        logger.error(f"Error in subtraction: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/multiply")
async def perform_multiplication(payload: dict):
    """Perform multiplication operation."""
    try:
        a, b = payload.get("a"), payload.get("b")
        result = sanitize_result(multiply(a, b))
        logger.info(f"Multiplication: {a} * {b} = {result}")
        return {"result": result}
    except Exception as e:
        logger.error(f"Error in multiplication: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/divide")
async def perform_division(payload: dict):
    """Perform division operation."""
    try:
        a, b = payload.get("a"), payload.get("b")
        result = sanitize_result(divide(a, b))
        logger.info(f"Division: {a} / {b} = {result}")
        return {"result": result}
    except ValueError as ve:
        logger.warning(f"Division by zero attempted: {ve}")
        return JSONResponse(status_code=400, content={"error": str(ve)})
    except Exception as e:
        logger.error(f"Error in division: {e}")
        raise HTTPException(status_code=400, detail=str(e))


# -------------------------------------------------------
# Exception Handlers
# -------------------------------------------------------
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions with structured JSON output."""
    logger.error(f"HTTPException: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


@app.exception_handler(Exception)
async def custom_general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions."""
    logger.error(f"Unexpected error: {exc}")
    return JSONResponse(status_code=500, content={"error": "Internal Server Error"})


# -------------------------------------------------------
# App Lifecycle Logging
# -------------------------------------------------------
@app.on_event("startup")
async def on_startup():
    logger.info("🚀 Application startup complete.")


@app.on_event("shutdown")
async def on_shutdown():
    logger.info("🛑 Application shutdown initiated.")
