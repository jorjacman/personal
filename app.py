from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of the FastAPI class
app = FastAPI()

# Define a POST endpoint
@app.post("/hello")
def hello_world():
    # Return a greeting with the provided name
    return {"message": "hello"}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)