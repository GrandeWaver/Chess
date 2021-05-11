from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, RedirectResponse
import ChessEngine

app = FastAPI()
templates = Jinja2Templates(directory="templates")

gs = ChessEngine.GameState()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/app/board")
def game_state():
    return gs.board


def split(word):
    return [char for char in word]


@app.get('/app/board/move/')
def send_move(request: Request):
    moves = request.query_params.get('moves', False)
    old_x = split(moves[3])
    old_y = split(moves[2])
    old = old_x + old_y
    new_x = split(moves[8])
    new_y = split(moves[7])
    new = new_x + new_y

    for i in range(0, len(old)):
        old[i] = int(old[i])

    for i in range(0, len(new)):
        new[i] = int(new[i])

    move = ChessEngine.Move(old, new, gs.board)
    gs.makeMove(move)

    return {'response': move, 'raport': gs}
