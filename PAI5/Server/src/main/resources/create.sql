CREATE TABLE peticion (
    id_peticion INT AUTOINCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    datos_peticion VARCHAR(10) NOT NULL,
    verificacion INT NOT NULL,
    empleado_id INT NOT NULL,
    FOREIGN KEY (empleado_id) REFERENCES Empleado(id_empleado)
);