from fastapi import FastAPI
from pydantic import BaseModel


class GamestationPSType(BaseModel):
    id: int
    Console: str
    Games: str
    Controller: str


class GamestationPCType(BaseModel):
    id: int
    PC: str
    Keyboard: str
    Mouse: str


GAMESTATIONPS: list[GamestationPSType] = [

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


GAMESTATIONPC: list[GamestationPCType] = [

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
    },

    {
        "id": 6,
        "PC": "DELL Optiplex 360",
        "Keyboard": "Logitech G50",
        "Mouse": "FanTech G70"
    }

]

ps = FastAPI()


@ps.get("/gamestationps")
def gamestationps():
    return GAMESTATIONPS


@ps.get("/gamestationpc")
def gamestationpc():
    return GAMESTATIONPC


@ps.get("/gamestationpc/{id}")
def gamestationpc(id: int):
    for r in range(len(GAMESTATIONPC)):
        item = GamestationPCType(**GAMESTATIONPC[r])
        if id == item.id:
            return item

    return "item doesn't exist"


@ps.get("/gamestationps/{id}")
def gamestation(id: int):
    for s in range(len(GAMESTATIONPS)):
        item = GamestationPSType(**GAMESTATIONPS[s])
        if (id == item.id):
            return item
    return "item doesn't exist"


@ps.post("/gamestationps")
def gamestation(gamestationps: GamestationPSType):
    for s in range(len(GAMESTATIONPS)):
        if gamestationps.id == GAMESTATIONPS[s]["id"]:
            return "item already exist"

        GAMESTATIONPS.append(gamestationps.model_dump())
        return gamestationps


@ps.post("/gamestationpc")
def gamestationpc(gamestationpc: GamestationPCType):
    for r in range(len(GAMESTATIONPC)):
        if gamestationpc.id == GAMESTATIONPC[r]["id"]:
            return "item already exist"

    GAMESTATIONPC.append(gamestationpc.model_dump())
    return gamestationpc


@ps.delete("/gamestationps/{id}")
def gamestaionps(id: int):
    for q in range(len(GAMESTATIONPS)):
        item = GamestationPSType(**GAMESTATIONPS[q])
        if (id == item.id):
            GAMESTATIONPS.pop(q)
            return "id has been removed"

    return "id doesn't found"


@ps.delete("/gamestationpc/{id}")
def gamestaionpc(id: int):
    for q in range(len(GAMESTATIONPC)):
        item = GamestationPCType(**GAMESTATIONPC[q])
        if (id == item.id):
            GAMESTATIONPC.pop(q)
            return "id has been removed"

    return "id doesn't found"


@ps.put("/gamestationpc/{id}")
def gamestaionpc(id: int, gamestationpc: GamestationPCType):
    for o in range(len(GAMESTATIONPC)):
        item = GamestationPCType(**GAMESTATIONPC[o])
        if (id == item.id):
            GAMESTATIONPC[o]["PC"] = gamestationpc.PC
            GAMESTATIONPC[o]["Keyboard"] = gamestationpc.Keyboard
            GAMESTATIONPC[o]["Mouse"] = gamestationpc.Mouse
            return gamestationpc

    return "id doesn't found"
