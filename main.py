from fastapi import FastAPI
from pydantic import BaseModel


class GamestaionType(BaseModel):
    id: int
    Console: str
    Games: str
    Controller: str

    class GamestaionType(BaseModel):
        id: int
        PC: str
        Keyboard: str
        Mouse: str


GAMESTAION: list[GamestaionType] = [

    {
        "id": 1,
        "Console": "Playstation",
        "Games": "Resident Evil",
        "Tekken 3"
        "Metal Gear Solid"
        "Final Fantasy IX"
        "Controller": "DualShock Analog Controller"
    },

    {"id": 2,
        "Console": "Playstaion 2",
        "Games": "Grand Theft Auto: San Andreas",
        "Grand Theft Auto: Vice City"
        "God of War II"
        "Silent Hill 2"
     "Controller": "DualShock 2 Analog Controller"
     },

    {
        "id": 3,
        "Console": "Playstaion 3",
        "Games": "The Last of Us",
        "Red Dead Redemption"
        "Fallout 3"
        "Skate 3"
        "Controller": "DualShock 3 Wireless Controller"
    },

    {
        "id": 4,
        "Console": "Playstaion 4",
        "Games": "Grand Theft Auto V",
        "God of War: Ragnarok"
        "FIFA 22"
        "Days Gone"
        "Controller": "DualShock 4 Wireless Controller"
    },

    {
        "id": 5,
        "Console": "Playstation 5",
        "Gmaes": "Grand Theft Auto VI",
        "Marvel's Spider-man 2"
        "Forza Horizon 5"
        "The Last of Us Part II Remastered"
        "Controller": "Dualsense Controller"
    }
]
