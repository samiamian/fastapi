from fastapi import FastAPI
from . import models
from . database import engine
from .config import Settings
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='5Point_0',cursor_factory=RealDictCursor)
#         cursor  = conn.cursor()
#         print("Database connection was succesfull, Yaaaaaay!")
#         break
#     except Exception as error:
#         print("Connecting to DB failed")
#         print("Error: ", error)
#         time.sleep(2)


# my_posts = [
#     {"title" :"title of post 1","content": "content of post 1", "id": 1},
#     {"title" :"title of post 2","content": "content of post 2", "id": 2}
#     ]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p["id"] == id:
#             return i 
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "WORKS Right!!"}



