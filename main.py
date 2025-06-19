from fastapi import FastAPI
from pydantic import BaseModel


class GamestaionPSType(BaseModel):
    id: int
    Console: str
    Games: str
    Controller: str


class GamestaionPCType(BaseModel):
    id: int
    PC: str
    Keyboard: str
    Mouse: str


GAMESTAIONPS: list[GamestaionPSType] = [

    {
        "id": 1,
        "Console": "Playstation",
        "Games": "Resident Evil,Tekken 3,Metal Gear Solid V,Final Fantasy IX",
        "Controller": "DualShock Analog Controller"
    },

    {"id": 2,
        "Console": "Playstaion 2",
        "Games": "Grand Theft Auto: San Andreas,Grand Theft Auto: Vice City,God of War II,Silent Hill 2",
     "Controller": "DualShock 2 Analog Controller"
     },

    {
        "id": 3,
        "Console": "Playstaion 3",
        "Games": "The Last of Us,Red Dead Redemption,Fallout 3,Skate 3",
        "Controller": "DualShock 3 Wireless Controller"
    },

    {
        "id": 4,
        "Console": "Playstaion 4",
        "Games": "Grand Theft Auto V,God of War: Ragnarok,FIFA 22,Days Gone",
        "Controller": "DualShock 4 Wireless Controller"
    },

    {
        "id": 5,
        "Console": "Playstation 5",
        "Games": "Grand Theft Auto VI,Marvel's Spider-man 2,Forza Horizon 5,The Last of Us Part II Remastered",
        "Controller": "Dualsense Controller"
    }
]


GAMESTAIONPC: list[GamestaionPCType] = [

    {
        "id": 1,
        "PC": "Lenovo LOQ Tower gen 9 (Intel)",
        "Keyboard": "Logitech G213",
        "Mouse": "Razer Viper V3 Pro"
    },

    {
        "id": 2,
        "PC": "HP Pro Tower 400 G9",
        "Keyboard": "Asus ROG Strix Scope II RX",
        "Mouse": "Corsair SCIMITAR RGB ELITE"
    },

    {
        "id": 3,
        "PC": "PREDATOR ORION X",
        "Keyboard": "Keychron Q5 Pro",
        "Mouse": "Corsair M75 Air"
    },

    {
        "id": 4,
        "PC": "ALIENWARE AREA-51",
        "Keyboard": "Turtle Beach Vulcan II TKL Pro",
        "Mouse": "Redragon M686 Vampire Elite"
    },

    {
        "id": 5,
        "PC": "MSI Codex R2C",
        "Keyboard": "OnePlus Keyboard 81 Pro",
        "Mouse": "Razer Naga V2 Pro"
    }

]

ps = FastAPI()


@ps.get("/gamestationps")
def gamestationps():
    return GAMESTAIONPS


@ps.get("/gamestationpc")
def gamestationpc():
    return GAMESTAIONPC


@ps.get("/gamestationpc/{id}")
def gamestationpc(id: int):
    for r in range(len(GAMESTAIONPC)):
        item = GamestaionPCType(**GAMESTAIONPC[r])
        if id == item.id:
            return item

    return "item doesn't exist"


@ps.get("/gamestationps/{id}")
def gamestation(id: int):
    for s in range(len(GAMESTAIONPS)):
        item = GamestaionPSType(**GAMESTAIONPS[s])
        if (id == item.id):
            return item
    return "item doesn't exist"


@ps.post("/gamestationps")
def gamestation(gamestationps: GamestaionPSType):
    for s in range(len(GAMESTAIONPS)):
        if gamestationps.id == GAMESTAIONPS[s]["id"]:
            return "item already exist"

        GAMESTAIONPS.append(gamestationps.model_dump())
        return gamestationps


@ps.post("/gamestationpc")
def gamestationpc(gamestationpc: GamestaionPCType):
    for r in range(len(GAMESTAIONPC)):
        if gamestationpc.id == GAMESTAIONPC[r].id:
            return "item already exist"

    GAMESTAIONPC.append(gamestationpc.model_dump())
    return gamestationpc
