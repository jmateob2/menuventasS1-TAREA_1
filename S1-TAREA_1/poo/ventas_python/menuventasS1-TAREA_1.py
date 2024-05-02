from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

ventas = []

def registrar_venta():
    console.print("Registrar una nueva venta", style="bold green")
    cliente = Prompt.ask("Ingrese el nombre del cliente")
    producto = Prompt.ask("Ingrese el nombre del producto")
    cantidad = Prompt.ask("Ingrese la cantidad", default="1")
    precio = Prompt.ask("Ingrese el precio unitario")
    
    venta = {
        'id': len(ventas) + 1,
        'cliente': cliente,
        'producto': producto,
        'cantidad': int(cantidad),
        'total': int(cantidad) * float(precio)
    }
    ventas.append(venta)
    console.print(f"Venta registrada exitosamente! ID de venta: {venta['id']}", style="bold blue")

def consultar_venta():
    id_venta = Prompt.ask("Ingrese el ID de la venta que desea consultar", default="1")
    venta_encontrada = next((venta for venta in ventas if venta['id'] == int(id_venta)), None)
    if venta_encontrada:
        mostrar_ventas([venta_encontrada])
    else:
        console.print("Venta no encontrada", style="bold red")

def consultar_todas_las_ventas():
    if ventas:
        mostrar_ventas(ventas)
    else:
        console.print("No hay ventas registradas", style="bold red")

def eliminar_venta():
    id_venta = Prompt.ask("Ingrese el ID de la venta a eliminar", default="1")
    venta_original = len(ventas)
    ventas[:] = [venta for venta in ventas if venta['id'] != int(id_venta)]
    if len(ventas) < venta_original:
        console.print(f"Venta con ID {id_venta} eliminada exitosamente", style="bold green")
    else:
        console.print("Venta no encontrada", style="bold red")

def mostrar_ventas(lista_ventas):
    table = Table(title="Detalle de Ventas")

    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Cliente", style="magenta")
    table.add_column("Producto", style="green")
    table.add_column("Cantidad", style="red")
    table.add_column("Total", style="blue")

    for venta in lista_ventas:
        table.add_row(
            str(venta['id']),
            venta['cliente'],
            venta['producto'],
            str(venta['cantidad']),
            f"{venta['total']:.2f}"
        )

    console.print(table)

# Ejemplo de uso dentro de un main o similar
def main():
    while True:
        console.print("1. Registrar Venta", style="bold cyan")
        console.print("2. Consultar Venta", style="bold magenta")
        console.print("3. Consultar Todas las Ventas", style="bold yellow")
        console.print("4. Eliminar Venta", style="bold blue")
        console.print("5. Salir", style="bold red")

        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4", "5"], default="1")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            consultar_venta()
        elif opcion == "3":
            consultar_todas_las_ventas()
        elif opcion == "4":
            eliminar_venta()
        elif opcion == "5":
            console.print("Gracias por usar el sistema de gestión de ventas", style="bold green")
            break

if __name__ == "__main__":
    main()