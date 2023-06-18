from Persona import Persona
from Empleado import Empleado

# pruebaPersona = Persona ('David', 'Ramos', 'Masculino', 'Cedula', 1000511858, 90, 1.92, 24)
# pruebaPersona.mostrarPersona()

empleado = Empleado()
empleado.pedirDatos()
empleado.calcularHonorarios()
empleado.mostrarPersona()

persona = Persona()
persona.pedirDatos()
persona.mostrarPersona()
persona.calcularImc()
persona.mayorEdad()