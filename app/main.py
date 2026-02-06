from fastapi import FastAPI
# Absolute imports use kar rahe hain taaki Render ko path mil sake
import models             
from database import engine 
from routers import post, user, auth, vote 
from config import settings 
from fastapi.middleware.cors import CORSMiddleware

# Database tables create karne ke liye (agar aapne alembic use nahi kiya hai)
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS configuration
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Pehle yahan 'allow_meathods' tha, use sahi kar diya hai
    allow_headers=["*"],
)

# Routers include kar rahe hain
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World. Success! My FastAPI app is running on Render."}
