# Step 1 import Libraries

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Step 2: Create an instance of the FastAPI class
app = FastAPI()

# Step 3:Create Pydantic Class with Attributes
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
# Step 4 : Create Endpoints of Root 
@app.get("/")
def root():
    """
    Root endpoint that returns a greeting message.
    
    Returns:
        dict: A dictionary containing the greeting message.
    """
    return {"message":"Hello World"}
# Step 5 Create end point of /posts route with get()
@app.get("/posts")
def get_posts():
    """
    Endpoint to retrieve posts.
    
    Returns:
        dict: A dictionary containing the post data.
    """
    return {"data":"This is your post"}
#  Step 6 Create End point with /createposts Rout and post()
@app.post("/createposts")
def create_post(new_post:Post):
    """
    Endpoint to create a new post.
    
    Args:
        new_post (Post): The new post to be created.
    
    Returns:
        dict: The created post data.
    """
    print(new_post.title)
    print(new_post.content)
    print(new_post.rating)
    print(new_post.model_dump())
    return {"data":new_post}