from fastapi import FastAPI
from .database import engine
from app import models
from .routers import user, post, auth, vote
from fastapi


#models.Base.metadata.create_all(bind=engine)  

app = FastAPI()

   
    
# try:
#     conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="darkknight", cursor_factory=RealDictCursor)
#     cur = conn.cursor()
#     print("Database Connection was sucessful")
#     #break
# except Exception as error:
#     print("Connection to DB failed")
#     print("Error: ", error)
#     time.sleep(2)    


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Wagwaan"}





 