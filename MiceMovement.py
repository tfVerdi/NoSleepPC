import asyncio
from keyboard import is_pressed, press, release
from mouse import move
from random import randint

# Setup config
minimo_espera = 40
maximo_espera = 60
tab_switch = True

async def pressAndRelease(key: str):
    press(key)
    await asyncio.sleep(0.05)
    release(key)
    await asyncio.sleep(0.05)

async def activitySim(tab_switch: bool = tab_switch):
    if tab_switch:
        await pressAndRelease('alt+tab')
        await pressAndRelease('alt+tab')
    move(randint(600, 1200), randint(0, 800), duration=0.25)
    
async def checkForQuit():
    if is_pressed('esc'):
        print("Has detenido el programa.")
        print("Ya puedes cerrar esta ventana, pero se cerrará de todos modos en unos segundos.")
        await asyncio.sleep(2)
        return True
    return False

async def mainLoop():
    stop = False
    while not stop:
        await activitySim()

        wait_time = randint(minimo_espera, maximo_espera)
        for _ in range(wait_time*4):
            await asyncio.sleep(0.25)
            if await checkForQuit():
                stop = True
                break

print("El programa empezará de inmediato...\n\nPara detener el programa cierra esta ventana o mantén presionado Esc.\n\n\n")
print("https://github.com/tfVerdi/NoSleepPC\n\n")
asyncio.run(mainLoop())