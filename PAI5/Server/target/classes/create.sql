CREATE TABLE Peticion (
    id_peticion INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha DATETIME DEFAULT (datetime('now','localtime')),
    datos_peticion TEXT NOT NULL,
    verificacion INTEGER NOT NULL,
    empleado_id INTEGER NOT NULL,
    FOREIGN KEY (empleado_id) REFERENCES Empleado(id_empleado)
);

CREATE TABLE Empleado (
      id_empleado INT PRIMARY KEY,
      clave_publica TEXT NOT NULL
);