# main.py
from task_storage import load_contacts, save_contacts
from task_logic import add_contact, list_contacts, search_contact, delete_contact
import asyncio

async def main():
    contacts = await load_contacts()

    while True:
        print("\n--- AGENDA DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            contacto = {"nombre": nombre, "telefono": telefono, "correo": correo}
            contacts = add_contact(contacts, contacto)
            await save_contacts(contacts)
            print("Contacto agregado.")

        elif opcion == '2':
            list_contacts(contacts)

        elif opcion == '3':
            criterio = input("Buscar por nombre o teléfono: ")
            resultados = search_contact(contacts, criterio)
            if resultados:
                for c in resultados:
                    print(c)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == '4':
            nombre = input("Nombre del contacto a eliminar: ")
            contacts, eliminado = delete_contact(contacts, nombre)
            if eliminado:
                await save_contacts(contacts)
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")

        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    asyncio.run(main())
