from fastapi import FastAPI


dict = {

    "title": "WellnessHub API",
    "description": "Backend for AI-Powered Medical & Emotional Support Assistant",
}

app = FastAPI()

@app.get('/')
def index():
    return {'Message': 'Welcome to WellnessHub API'}

def showme():
    print('Hellow world')

@app.get('/chat')
def show(para :str):
    return {'Data':para}








