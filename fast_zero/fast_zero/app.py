from fastapi import FastAPI

from http import HttpStatus

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HttpStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

print(read_root())
