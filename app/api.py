from fastapi import FastAPI, Form, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()
app.mount("/ui", StaticFiles(directory="ui"), name="ui")


@app.get("/")
async def root():
    return {"message": "Hello World"}


def is_valid_user(username, password):
    return username == "somu@ti.com" and password == "1234"


@app.post("/login")
def post_login(username: str = Form(...), password: str = Form(...)):
    if is_valid_user(username, password):
        return "User is valid"
    else:
        return RedirectResponse("/ui/login.html?error", status_code=status.HTTP_302_FOUND)
