"""Módulo principal del programa"""

import logging

from sqlalchemy import insert, select, update, delete, exc
from settings import DB_FILE, Base, engine, session
from models import Productos

logging.basicConfig(level=logging.INFO)


def ingresar_data():
    # INSERT INTO productos (id, nombre, categoria, precio) VALUES (1,'Arroz','Granos','1.25');
    arroz = Productos(nombre="Arroz", categoria="Granos", precio=1.25)
    session.add(arroz)
    # INSERT INTO productos (id, nombre, categoria, precio) VALUES (2, "Agua", "Líquidos", 0.3);
    agua = Productos(nombre="Agua", categoria="Líquidos", precio=0.3)
    # INSERT INTO productos (id, nombre, categoria, precio) VALUES (3, "Mantequilla", "Lácteos", 3.56);
    mantequilla = Productos(nombre="Mantequilla", categoria="Lácteos", precio=3.56)
    # INSERT INTO productos (id, nombre, categoria, precio) VALUES (4, "Queso", "Lácteos", 8.56);
    queso = Productos(nombre="Queso", categoria="Lácteos", precio=8.56)
    session.add_all([agua, mantequilla, queso])
    # Hacer persistentes los cambios en la base de datos
    session.commit()
    # SELECT COUNT(*) AS number_of_productos FROM productos;
    row_count = session.query(Productos).count()
    logging.info(f"✅ ¡Inserción exitosa de los '{row_count}' productos!\n")


def consultar_data():
    print("✅ ¡Consulta todos los productos!")
    # SELECT * FROM productos;
    todos_productos = session.query(Productos).all()
    for cada_producto in todos_productos:
        print(f"📜 {cada_producto}")
    logging.info(f"✅ ¡Consulta exitosa de '{len(todos_productos)}' productos!")
    print("\n✅ ¡Consulta el 'nombre' y 'precio' de todos los productos!")
    # SELECT nombre, precio FROM productos;
    consulta = select(Productos)
    for producto in session.scalars(consulta):
        print(f"📜 {producto.nombre} {str(producto.precio)}")
    logging.info("✅ ¡Consulta exitosa del 'nombre' y 'precio' de todos los productos!")


def consultar_id_data(producto_id):
    print("\n✅ ¡Consulta de producto en base a su clave primaria!")
    # SELECT * FROM productos WHERE id == 1
    producto = session.get(Productos, producto_id)
    print(f"📜 {producto}")
    logging.info(f"✅ ¡Consulta exitosa del producto '{producto.nombre}'!")


def consultar_categoria_precio():
    print("\n✅ ¡Consulta de productos 'lacteos' con precio mayor a '3.0'!")
    # SELECT * FROM productos WHERE categoria == "Lácteos" AND precio >= 3.0
    lacteos = (
        session.query(Productos)
        .filter(Productos.categoria == "Lácteos")
        .filter(Productos.precio >= 3.0)
    )
    for lacteo in lacteos:
        print(f"📜 {lacteo}")
    logging.info(
        "✅ ¡Consulta exitosa de los productos 'lacteos' con precio mayor a '3.0'!"
    )


def consultar_nombre_tupla():
    print("\n✅ ¡Otra consulta de productos 'lácteos'!")
    # SELECT id, nombre, categoria FROM productos WHERE categoria == "Lácteos"
    lacteos = session.query(Productos).filter(Productos.categoria == "Lácteos")
    for lacteo in lacteos:
        print(f"📜 {lacteo.id}, {lacteo.nombre}, {lacteo.categoria}")
    logging.info("✅ ¡Consulta exitosa de todos los productos 'lacteos'!")


def consultar_nombre_primero():
    print("\n✅ ¡Consulta del primer producto!")
    # SELECT * FROM productos WHERE categoria == "Lácteos" LIMIT 1
    producto = session.query(Productos).filter_by(categoria="Lácteos").first()
    if producto:
        print(f"📜 {producto}")
    else:
        print("❌ ¡No hay ningún Producto con ese criterio en la base de datos!")


def consultar_nombre_unico():
    print("\n✅ ¡Consulta del único producto!")
    # SELECT * FROM productos WHERE categoria == "Lácteos"
    producto = session.query(Productos).filter_by(categoria="Líquidos").one()
    if not producto:
        logging.error(
            "❌ ERROR: ¡No hay ningún Producto de la categoria 'Líquidos' en la base de datos!"
        )
    else:
        print(f"📜 {producto}")
        logging.info(
            "✅ ¡Consulta exitosa del único producto con la categoria 'Líquidos'!"
        )


def consultar_nombres_data(nombres):
    print("\n✅ ¡Consulta los productos cuyos nombres coincidan con los suministrados!")
    # SELECT * FROM productos WHERE nombre IN ("Agua", "Arroz")
    consulta = select(Productos).where(Productos.nombre.in_(nombres))
    for producto in session.scalars(consulta):
        print(f"📜 {producto}")
    logging.info(
        "✅ ¡Consulta exitosa de producto(s) cuyo(s) nombres coincidan con 'Agua' y 'Arroz'!"
    )


def actualizar_data(producto_id):
    print("\n✅ ¡Actualiza el producto suministrado!")
    # SELECT * FROM productos WHERE id == 1 LIMIT 1
    # UPDATE productos SET precio = 11.50 WHERE id = 1;
    producto = session.query(Productos).filter(Productos.id == producto_id).first()
    print("📜 Precio anterior:", producto, producto.precio)
    producto.precio = 11.50
    print("📜 Precio nuevo:", producto, producto.precio)
    session.add(producto)
    # Hacer persistentes los cambios en la base de datos
    session.commit()
    logging.info(
        f"✅ ¡Actualización exitosa de precio del producto '{producto.nombre}'!\n"
    )


def actualizar_otra_data(producto_id, precio_nuevo):
    # UPDATE productos SET precio = 3.33 WHERE id = 2;
    producto = session.query(Productos).filter_by(id=producto_id).one()
    session.execute(
        update(Productos)
        .where(Productos.id == producto_id)
        .values(precio=precio_nuevo)
        .execution_options(synchronize_session=False)
    )
    # Hacer persistentes los cambios en la base de datos
    session.commit()
    logging.info(
        f"✅ ¡Actualización exitosa del producto '{producto.nombre}' con el precio '{precio_nuevo}'!\n"
    )


def eliminar_data(producto_id):
    # DELETE FROM productos WHERE id = 1';
    producto = session.query(Productos).filter_by(id=producto_id).one()
    session.query(Productos).filter(Productos.id == producto_id).delete()
    # Hacer persistentes los cambios en la base de datos
    session.commit()
    logging.info(f"✅ ¡Eliminación exitosa del producto '{producto.nombre}'!\n")


if __name__ == "__main__":
    try:
        # Borra la base de datos y tablas
        Base.metadata.drop_all(engine)
        # Crea la base de datos y tablas
        Base.metadata.create_all(engine)
        logging.info(f"✅ ¡Creación exitosa de la tabla 'productos'!\n")
        ingresar_data()
        consultar_data()
        consultar_id_data(1)
        consultar_categoria_precio()
        consultar_nombre_tupla()
        consultar_nombre_primero()
        consultar_nombre_unico()
        consultar_nombres_data(["Agua", "Arroz"])
        actualizar_data(1)
        actualizar_otra_data(2, 3.33)
        eliminar_data(1)
    except exc.SQLAlchemyError as e:
        logging.error(
            f"❌ ERROR: ¡Se produjo un falla al establecer la conexión a la base de datos '{DB_FILE}': '{e}'!"
        )
    finally:
        if session:
            # Cerrar la conexión a la base de datos
            session.close()
            engine.dispose()
            logging.info(
                f"✅ ¡La conexión SQLite a la base de datos '{DB_FILE}' fue cerrada!"
            )
