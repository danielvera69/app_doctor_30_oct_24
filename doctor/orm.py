from aplication.core.models import *
from aplication.attention.models import *
from django.db.models import Q
from django.db.models import Sum,Avg,Max,Min,Count
from django.db.models import F
# insertar registro directamente en el modelo tiposangre
tipo1 = TipoSangre.objects.create(tipo="z+", descripcion="Tipo z positivo")
# crea el registro en memoria
tipo2 = TipoSangre(tipo="y-", descripcion="Tipo y negativo")
tipo2.descripcion="Tipo y- negativo"
tipo2.save()
# Y luego con save() lo guarda el registro en la base de datos
# Crea una lista de instancias de TipoSangre con varios tipos de sangre
tipos_sangre = [
    TipoSangre(tipo="B+", descripcion="Tipo B positivo"),
    TipoSangre(tipo="B-", descripcion="Tipo B negativo"),
]
# inserta registro de forma maxima directamente en la basedato
TipoSangre.objects.bulk_create(tipos_sangre)

# Consulta todos los registros de TipoSangre con todos sus campos
tipos_sangre = TipoSangre.objects.all()
# Imprimir los resultados
for tipo in tipos_sangre:
    print(f"Tipo: {tipo.tipo}, Descripción: {tipo.descripcion}")

# Selecciona los tipos de sangre    
tipo_O_neg = TipoSangre.objects.get(tipo="O-")
tipo_A = TipoSangre.objects.get(tipo="A")
tipo_ab_pos = TipoSangre.objects.get(tipo="AB+")

# Se Crea una lista de instancias de Paciente
pacientes = [
    Paciente(
        nombres="Juan",
        apellidos="Pérez",
        cedula="1234567890",
        fecha_nacimiento="1980-01-15",
        telefono="0998765432",
        email="juan.perez@example.com",
        sexo="M",
        estado_civil="C",
        direccion="Calle Falsa 123",
        latitud=-0.123456,
        longitud=-78.123456,
        tipo_sangre_id=3,
        alergias="Ninguna",
        enfermedades_cronicas="Hipertensión",
        medicacion_actual="Losartán",
        cirugias_previas="Apendicectomía",
        antecedentes_personales="Diabetes en tratamiento",
        antecedentes_familiares="Corazón en la familia"
    ),
    Paciente(
        nombres="María",
        apellidos="Gómez",
        cedula="0987654321",
        fecha_nacimiento="1990-05-20",
        telefono="0991234567",
        email="maria.gomez@example.com",
        sexo="F",
        estado_civil="S",
        direccion="Av. Libertad 456",
        latitud=-0.654321,
        longitud=-78.654321,
        tipo_sangre=tipo_A,
        alergias="Penicilina",
        enfermedades_cronicas="Asma",
        medicacion_actual="Salbutamol",
        cirugias_previas="Ninguna",
        antecedentes_personales="No fuma",
        antecedentes_familiares="Madre con cáncer"
    ),
    Paciente(
        nombres="Carlos",
        apellidos="Ramírez",
        cedula="1357924680",
        fecha_nacimiento="1975-09-30",
        telefono="0987654321",
        email="carlos.ramirez@example.com",
        sexo="M",
        estado_civil="C",
        direccion="Calle 10 de Agosto 789",
        latitud=-0.321654,
        longitud=-78.321654,
        tipo_sangre=tipo_ab_pos,
        alergias="Ninguna",
        enfermedades_cronicas="Ninguna",
        medicacion_actual="Ninguna",
        cirugias_previas="Ninguna",
        antecedentes_personales="No antecedentes relevantes",
        antecedentes_familiares="Padre con hipertensión"
    ),
]
# Insercion maxiva de los registros en la base de datos utilizando bulk_create
Paciente.objects.bulk_create(pacientes)
# Presenta todos los pacientes 
pacientes=Paciente.objects.all()
for paciente in pacientes:
    print(f"--- Paciente ---")
    print(f"Nombres: {paciente.nombres}")
    print(f"Apellidos: {paciente.apellidos}")
    print(f"Cédula: {paciente.cedula}")
    print(f"Fecha de Nacimiento: {paciente.fecha_nacimiento}")
    print(f"Teléfono: {paciente.telefono}")
    print(f"Email: {paciente.email}")
    print(f"Sexo: {paciente.sexo}")
    print(f"Estado Civil: {paciente.estado_civil}")
    print(f"Dirección: {paciente.direccion}")
    print(f"Latitud: {paciente.latitud}")
    print(f"Longitud: {paciente.longitud}")
    print(f"Tipo de Sangre: {paciente.tipo_sangre.descripcion if paciente.tipo_sangre else 'No especificado'}")
    print(f"Alergias: {paciente.alergias if paciente.alergias else 'Ninguna'}")
    print(f"Enfermedades Crónicas: {paciente.enfermedades_cronicas if paciente.enfermedades_cronicas else 'Ninguna'}")
    print(f"Medicación Actual: {paciente.medicacion_actual if paciente.medicacion_actual else 'Ninguna'}")
    print(f"Cirugías Previas: {paciente.cirugias_previas if paciente.cirugias_previas else 'Ninguna'}")
    print(f"Antecedentes Personales: {paciente.antecedentes_personales if paciente.antecedentes_personales else 'Ninguno'}")
    print(f"Antecedentes Familiares: {paciente.antecedentes_familiares if paciente.antecedentes_familiares else 'Ninguno'}")
    print("-----------------------------")

# Consulta pacientes con tipo de sangre O+
pacientes_o_plus = Paciente.objects.filter(tipo_sangre__tipo="O+")
# funciones para manejo de texto del orm de django
# exact (coincidencia exacta), 
# iexact (coincidencia exacta sin distinguir mayúsculas/minúsculas), 
# contains (contiene el contenido), 
# icontains (contiene el contenido sin distinguir mayúsculas/minúsculas), 
# startswith (comienza con el contenido), 
# istartswith (comienza con el contenido sin distinguir mayúsculas/minúsculas), 
# endswith (termina con el contenido), 
# iendswith (termina con el contenido sin distinguir mayúsculas/minúsculas), 
# regex (coincide con expresión regular), 
# iregex (coincide con expresión regular sin distinguir mayúsculas/minúsculas)

# Consulta pacientes que contengan 'O' en el tipo de sangre. Ejemplo icontains
pacientes_con_o = Paciente.objects.filter(tipo_sangre__tipo__icontains="A")
# Buscar empleados cuyos nombres empiecen con una "y" o "w" sin importar mayúsculas/minúsculas
empleados_con_yw = Paciente.objects.filter(nombres__iregex=r'^[yw]')
# funciones de fecha del orm
# year: fecha__year=2024  o # (fecha__year__in=[2022, 2023, 2024]
# month: fecha__month=10 (para octubre)
# day: fecha__day=15
# week_day: fecha__week_day=1 (para domingo)
# quarter: fecha__quarter=2 (para el segundo trimestre)
# isnull: fecha__isnull=True (para comprobar si es NULL)
# gt: fecha__gt='2024-01-01' (mayor que una fecha específica)
# lt: fecha__lt='2024-01-01' (menor que una fecha específica)
# gte: fecha__gte='2024-01-01' (mayor o igual que una fecha específica)
# lte: fecha__lte='2024-01-01' (menor o igual que una fecha específica)
# range: fecha__range=['2024-01-01', '2024-12-31'] (dentro de un rango específico)
# Ejemplo
# presenta un queryset de pacientes como diccionarios (apellidos y fecha_nacimiento) que nacieron en 2024
pacientes_2024 = Paciente.objects.filter(fecha_nacimiento__year=2024).values('apellidos','fecha_nacimiento')
# Consulta pacientes que nacieron antes de 1980
# > __gt, < __lt, >= __gte, <= __lte, != __ne
pacientes_menor_2024 = Paciente.objects.filter(fecha_nacimiento__year__lt=2024).values('apellidos','fecha_nacimiento')
# convierte el queryset a una lista de diccionarios
pacientes_menor_2024=list(pacientes_menor_2024)
# Obtener los nombres y la descripción del tipo de sangre de pacientes con tipo de sangre "AB+"
pacientes_ab = Paciente.objects.filter(tipo_sangre__tipo="AB+").values('nombres', 'apellidos', 'tipo_sangre__descripcion')
# Obtener los tipos de sangre "AB+" y los nombres de los pacientes asociados
tipos_sangre_ab = TipoSangre.objects.filter(tipo="AB+").values('descripcion', 'tipos_sangre__nombres', 'tipos_sangre__apellidos')
# relacion d epaciente normal con tiposangre
Paciente.objects.filter(tipo_sangre__tipo__icontains="Ab+").values("nombres","tipo_sangre")
# consulta inversa
# Obtener el tipo de sangre "AB+"
tipo_sangre_ab = TipoSangre.objects.get(tipo="AB+")
# Obtener todos los pacientes que tienen este tipo de sangre ab+
pacientes_con_ab = tipo_sangre_ab.tipos_sangre.all()
# Consulta con AND
pacientes = Paciente.objects.filter(fecha_nacimiento__year=1980, tipo_sangre__tipo="O+")
# Consulta con or
pacientes = Paciente.objects.filter(Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"))
# Filtrar pacientes que nacieron en 1980 o tienen tipo de sangre O+ y no tienen alergias
pacientes = Paciente.objects.filter(
    Q(fecha_nacimiento__year=1980) | Q(tipo_sangre__tipo="O+"),
    alergias__isnull=True  # Esta condición se aplica con AND implícito
)
#Obtener pacientes que no tengan tipo de sangre "AB+".
pacientes = Paciente.objects.exclude(tipo_sangre__tipo="AB+").values('apellidos','tipo_sangre__descripcion')
#Obtener pacientes que nacieron después de 1980 y excluir aquellos con tipo de sangre "O-".
pacientes = Paciente.objects.filter(fecha_nacimiento__year__gt=1980).exclude(tipo_sangre__tipo="O+").values('apellidos','tipo_sangre__descripcion')

# obtener el cargo cuyo id sea igul a 1(enfermera) 
cargo_1 = Cargo.objects.get(id=1)  
# Crear dos empleados
empleado1 = Empleado(
    nombres="Juan",
    apellidos="Pérez",
    cedula="1234567890",
    fecha_nacimiento="1990-01-01",
    cargo=cargo_1,
    sueldo=1500.00,
    direccion="Calle 1, Ciudad",
    latitud=-0.123456,
    longitud=-78.123456,
)

empleado2 = Empleado(
    nombres="María",
    apellidos="Gómez",
    cedula="0987654321",
    fecha_nacimiento="1985-05-15",
    cargo_id=2,
    sueldo=1600.00,
    direccion="Calle 2, Ciudad",
    latitud=-0.654321,
    longitud=-78.654321,
)

# Guardar en la base de datos
empleado1.save()
empleado2.save()
# muestra e nombre y el sueldo de todos los empleados
emps=Empleado.objects.values('nombres','sueldo')
#consulta de agregados para empleados con cargo "Enfermera"
# para contar, sumar, promediar,obtener el maximo y el minimo de los sueldos de todos los empeados. Si hay condicion dada la condicion 
#                                    cargo_id=1  
resultados = Empleado.objects.filter(cargo__descripcion__icontains="Enfermera").aggregate(
    total_sueldo=Sum('sueldo'),
    promedio_sueldo=Avg('sueldo'),
    max_sueldo=Max('sueldo'),
    min_sueldo=Min('sueldo'),
    cantidad_enfermeras=Count('id')
)
# agrupar campos de una tabla
# Realizar la consulta de agregados agrupados por cargo
resultados = Empleado.objects.values('tipo').annotate(
    total_sueldo=Sum('sueldo'),
    promedio_sueldo=Avg('sueldo'),
    max_sueldo=Max('sueldo'),
    min_sueldo=Min('sueldo'),
    cantidad_empleados=Count('id')
)
# {'total_sueldo': Decimal('2200'),
#  'promedio_sueldo': Decimal('1100'),
#  'max_sueldo': Decimal('1650.00000000000'),
#  'max_sueldo': Decimal('1650.00000000000'),
#  'min_sueldo': Decimal('550'),
#  'cantidad_enfermeras': 2}


#Realizar la consulta de agregados agrupados por cargo y sueldo
resultados = Empleado.objects.values('cargo__nombre', 'sueldo').annotate(
    cantidad_empleados=Count('id')
).order_by('cargo__nombre', 'sueldo')  # Ordenar por cargo y sueldo
# Realizar la consulta de empleados y agregar el nombre del cargo como un alias sin agrupar
resultados = Empleado.objects.annotate(
    cargo_descripcion=F('cargo__nombre')  
)
# Actualizar los sueldos en un 10% para los empleados cuyo cargo sea "Enfermera"
Empleado.objects.filter(cargo__nombre="Enfermera").update(sueldo=F('sueldo') * 1.10,direccion='Guayaquil')
cargo = Cargo.objects.get(id=3)
# actualiza lo deseado
cargo.descripcion="Financiero"
cargo.save() # luego se graba
# Eliminar los tipos de sangre cuya descripcion contenido contenga "positivo"
tipos_eliminados = TipoSangre.objects.filter(descripcion__iendswith="positivo").delete()
cargo = Cargo.objects.get(id=3)
cargo.delete()
