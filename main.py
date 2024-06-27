from fastapi import FastAPI
from Brainboxes_Test import controlar_salidas



app = FastAPI(title="Cervus III Multiconmutador API", 
              version="0.1")
              

@app.post("/apagar_amplificador")
def amplifiadores():
    return controlar_salidas(accion = 'abrir todas') 

@app.post("/encender_amplificador")
def amplifiadores():
    return controlar_salidas(accion = 'cerrar salida 0') 

# @app.post("/encender_amplificador")
# def amplifiadores(accion: str = 'cerrar salida 0'):
#     return controlar_salidas(accion) 

@app.get("/listar_acciones")
def listar_acciones():
    acciones = [
        'abrir todas',
        'cerrar todas',
        'cerrar salida 0',
        'cerrar salida 1',
        'cerrar salida 2',
        'cerrar salida 3',
        'cerrar salida 0 y 1',
        'cerrar salida 0 y 2',
        'cerrar salida 0 y 3',
        'cerrar salida 1 y 2',
        'cerrar salida 1 y 3',
        'cerrar salida 2 y 3',
        'cerrar salida 0, 1 y 2',
        'cerrar salida 0, 1 y 3',
        'cerrar salida 0, 2 y 3',
        'cerrar salida 1, 2 y 3'
    ]
    return {"acciones_disponibles": acciones}






