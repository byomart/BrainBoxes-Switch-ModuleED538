import brainboxes

def controlar_salidas(accion, ipaddr='192.168.127.254', port=9500, timeout=1.0):
    acciones = {
        'abrir todas': b'@0100',
        'cerrar todas': b'@01FF',
        'cerrar salida 0': b'@0101',
        'cerrar salida 1': b'@0102',
        'cerrar salida 2': b'@0104',
        'cerrar salida 3': b'@0108',
        'cerrar salida 0 y 1': b'@0103',
        'cerrar salida 0 y 2': b'@0105',
        'cerrar salida 0 y 3': b'@0109',
        'cerrar salida 1 y 2': b'@0106',
        'cerrar salida 1 y 3': b'@010A',
        'cerrar salida 2 y 3': b'@010C',
        'cerrar salida 0, 1 y 2': b'@0107',
        'cerrar salida 0, 1 y 3': b'@010B',
        'cerrar salida 0, 2 y 3': b'@010D',
        'cerrar salida 1, 2 y 3': b'@010E'
    }

    txmessage = acciones.get(accion)

    if txmessage is None:
        print("Acción no válida. Use una acción válida.")
        return

    with brainboxes.AsciiIo(ipaddr=ipaddr, port=port, timeout=timeout) as io:
        print("Sending command %s" % txmessage)
        rxdata = io.command_response(txmessage)
        if rxdata is None:
            print("  No response received!")
        else:
            print("  Response was %s" % rxdata)




if __name__ == "__main__":
    acciones = {
        'abrir todas': b'@0100',
        'cerrar todas': b'@01FF',
        'cerrar salida 0': b'@0101',
        'cerrar salida 1': b'@0102',
        'cerrar salida 2': b'@0104',
        'cerrar salida 3': b'@0108',
        'cerrar salida 0 y 1': b'@0103',
        'cerrar salida 0 y 2': b'@0105',
        'cerrar salida 0 y 3': b'@0109',
        'cerrar salida 1 y 2': b'@0106',
        'cerrar salida 1 y 3': b'@010A',
        'cerrar salida 2 y 3': b'@010C',
        'cerrar salida 0, 1 y 2': b'@0107',
        'cerrar salida 0, 1 y 3': b'@010B',
        'cerrar salida 0, 2 y 3': b'@010D',
        'cerrar salida 1, 2 y 3': b'@010E'
    }

    print("Acciones disponibles:")
    for accion in acciones:
        print(f"- {accion}")
    
    accion = input("Ingrese la acción: ")
    controlar_salidas(accion)