from fastapi import FastAPI
from routers import stripe_listener, raina_desktop, raina_background

app = FastAPI()
app.include_router(stripe_listener.router)
app.include_router(raina_desktop.router)
app.include_router(raina_background.router)

@app.get("/")
def home():
    return {"status":"Backend running"}