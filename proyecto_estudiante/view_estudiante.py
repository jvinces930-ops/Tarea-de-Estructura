from abc import ABC, abstractmethod

from models_estudiante import Estudiante, Materia, Matricula
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido


# =====================================================================
# CLASE BASE (ABSTRACTA)
# =====================================================================
class CrudBase(ABC):

    @abstractmethod
    def leer(self):
        pass

    @abstractmethod
    def obtener(self, id_registro):
        pass

    @abstractmethod
    def buscar(self, texto):
        pass

    @abstractmethod
    def siguiente(self):
        pass

    @abstractmethod
    def crear(self, datos):
        pass

    @abstractmethod
    def actualizar(self, id_registro, datos):
        pass

    @abstractmethod
    def eliminar(self, id_registro):
        pass


# =====================================================================
# CONTROLADOR DE ESTUDIANTES
# =====================================================================
class EstudianteController(CrudBase):

    def __init__(self, archivo="data/estudiantes.json"):
        self.gestor = GestorJSON(archivo)

        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Estudiante.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for estudiante in self.lista:
            datos.append(estudiante.a_diccionario())
        self.gestor.guardar(datos)

    def carnets_registrados(self, excepto_id=None):
        """CONJUNTO de carnets ya usados para búsqueda instantánea."""
        return {e.carnet.upper() for e in self.lista if e.id != excepto_id}

    def validar(self, datos, id_actual=None):
        if id_actual is None:
            for campo in ("nombre", "apellido", "email", "carnet"):
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"

        if "email" in datos:
            email = str(datos["email"]).strip().lower()
            if not es_email_valido(email):
                return f"Email inválido: '{email}'"
            usados_email = {e.email for e in self.lista if e.id != id_actual}
            if email in usados_email:
                return "Ese email ya está registrado"

        if "carnet" in datos:
            carnet = str(datos["carnet"]).strip().upper()
            if carnet in self.carnets_registrados(id_actual):
                return f"El carnet '{carnet}' ya está asignado a otro estudiante"

        return None

    def leer(self):
        return self.lista

    def obtener(self, id_estudiante):
        for estudiante in self.lista:
            if estudiante.id == id_estudiante:
                return estudiante
        return None

    def buscar(self, texto):
        texto = texto.strip().lower()
        encontrados = []
        if texto == "":
            return encontrados

        for estudiante in self.lista:
            if (texto in estudiante.nombre.lower()
                    or texto in estudiante.apellido.lower()
                    or texto in estudiante.email
                    or texto in estudiante.carnet.lower()
                    or texto in estudiante.carrera.lower()):
                encontrados.append(estudiante)
        return encontrados

    def siguiente(self):
        mayor = 0
        for estudiante in self.lista:
            if estudiante.id > mayor:
                mayor = estudiante.id
        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)
        if error:
            return False, error

        estudiante = Estudiante(
            self.siguiente(),
            str(datos["nombre"]).strip().title(),
            str(datos["apellido"]).strip().title(),
            str(datos["email"]).strip().lower(),
            str(datos["carnet"]).strip().upper(),
            str(datos.get("carrera", "")).strip().title()
        )
        self.lista.append(estudiante)
        self.guardar()
        return True, f"Estudiante creado: {estudiante.etiqueta()}"

    def actualizar(self, id_estudiante, datos):
        estudiante = self.obtener(id_estudiante)
        if estudiante is None:
            return False, f"No existe un estudiante con id {id_estudiante}"
        if not datos:
            return False, "No se indicó ningún cambio"

        permitidos = {"nombre", "apellido", "email", "carnet", "carrera"}
        desconocidos = set(datos) - permitidos
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

        error = self.validar(datos, id_estudiante)
        if error:
            return False, error

        for campo, valor in datos.items():
            valor = str(valor).strip()
            if campo in ("nombre", "apellido", "carrera"):
                valor = valor.title()
            elif campo == "email":
                valor = valor.lower()
            elif campo == "carnet":
                valor = valor.upper()
            setattr(estudiante, campo, valor)

        self.guardar()
        return True, f"Estudiante {id_estudiante} actualizado"

    def eliminar(self, id_estudiante):
        estudiante = self.obtener(id_estudiante)
        if estudiante is None:
            return False, f"No existe un estudiante con id {id_estudiante}"

        self.lista.remove(estudiante)
        self.guardar()
        return True, f"Estudiante {id_estudiante} eliminado"

    def carreras(self):
        """CONJUNTO de carreras distintas ordenadas."""
        return sorted({e.carrera for e in self.lista if e.carrera != ""})


# =====================================================================
# CONTROLADOR DE MATERIAS
# =====================================================================
class MateriaController(CrudBase):

    def __init__(self, archivo="data/materias.json"):
        self.gestor = GestorJSON(archivo)

        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Materia.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for materia in self.lista:
            datos.append(materia.a_diccionario())
        self.gestor.guardar(datos)

    def validar(self, datos, id_actual=None):
        if id_actual is None:
            for campo in ("nombre", "codigo", "creditos"):
                if str(datos.get(campo, "")).strip() == "":
                    return f"El campo {campo} es obligatorio"

        if "codigo" in datos:
            codigo = str(datos["codigo"]).strip().upper()
            for otra in self.lista:
                if otra.codigo == codigo and otra.id != id_actual:
                    return f"Ya existe una materia con el código {codigo}"

        creditos = str(datos.get("creditos", "")).strip()
        if creditos != "":
            if not creditos.isdigit() or not (1 <= int(creditos) <= 10):
                return "Los créditos deben ser un número entero entre 1 y 10"

        cupos = str(datos.get("cupos", "")).strip()
        if cupos != "":
            if not cupos.isdigit() or not (0 <= int(cupos) <= Materia.CUPOS_MAXIMOS):
                return f"Los cupos deben estar entre 0 y {Materia.CUPOS_MAXIMOS}"

        return None

    def leer(self):
        return self.lista

    def obtener(self, id_materia):
        for materia in self.lista:
            if materia.id == id_materia:
                return materia
        return None

    def buscar(self, texto):
        texto = texto.strip().lower()
        encontrados = []
        if texto == "":
            return encontrados

        for materia in self.lista:
            if texto in materia.nombre.lower() or texto in materia.codigo.lower():
                encontrados.append(materia)
        return encontrados

    def siguiente(self):
        mayor = 0
        for materia in self.lista:
            if materia.id > mayor:
                mayor = materia.id
        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)
        if error:
            return False, error

        cupos = str(datos.get("cupos", "")).strip()
        materia = Materia(
            self.siguiente(),
            str(datos["nombre"]).strip().title(),
            str(datos["codigo"]).strip().upper(),
            int(datos["creditos"]),
            int(cupos) if cupos != "" else Materia.CUPOS_MAXIMOS
        )
        self.lista.append(materia)
        self.guardar()
        return True, f"Materia creada: {materia.etiqueta()}"

    def actualizar(self, id_materia, datos):
        materia = self.obtener(id_materia)
        if materia is None:
            return False, f"No existe una materia con id {id_materia}"
        if not datos:
            return False, "No se indicó ningún cambio"

        permitidos = {"nombre", "codigo", "creditos", "cupos"}
        desconocidos = set(datos) - permitidos
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

        error = self.validar(datos, id_materia)
        if error:
            return False, error

        if "nombre" in datos:
            materia.nombre = str(datos["nombre"]).strip().title()
        if "codigo" in datos:
            materia.codigo = str(datos["codigo"]).strip().upper()
        if "creditos" in datos:
            materia.creditos = int(datos["creditos"])
        if "cupos" in datos:
            materia.cupos = int(datos["cupos"])

        self.guardar()
        return True, f"Materia {id_materia} actualizada"

    def eliminar(self, id_materia):
        materia = self.obtener(id_materia)
        if materia is None:
            return False, f"No existe una materia con id {id_materia}"

        self.lista.remove(materia)
        self.guardar()
        return True, f"Materia {id_materia} eliminada"

    def materias_sin_cupo(self):
        return [m for m in self.lista if not m.hay_cupo()]


# =====================================================================
# CONTROLADOR DE MATRÍCULAS
# =====================================================================
class MatriculaController(CrudBase):

    def __init__(self, estudiantes, materias, archivo="data/matriculas.json"):
        self.estudiantes = estudiantes
        self.materias = materias
        self.gestor = GestorJSON(archivo)

        self.lista = []
        for datos in self.gestor.leer():
            self.lista.append(Matricula.desde_diccionario(datos))

    def guardar(self):
        datos = []
        for matricula in self.lista:
            datos.append(matricula.a_diccionario())
        self.gestor.guardar(datos)

    def validar(self, datos):
        try:
            estudiante_id = int(datos.get("estudiante_id", 0))
            materia_id = int(datos.get("materia_id", 0))
        except (TypeError, ValueError):
            return "estudiante_id y materia_id deben ser números enteros"

        periodo = str(datos.get("periodo", "2026-1")).strip()
        if not periodo:
            return "El periodo es obligatorio"

        if self.estudiantes.obtener(estudiante_id) is None:
            return f"No existe un estudiante con id {estudiante_id}"

        materia = self.materias.obtener(materia_id)
        if materia is None:
            return f"No existe una materia con id {materia_id}"

        if not materia.hay_cupo():
            return f"La materia {materia.nombre} no tiene cupos disponibles"

        # Validación: No matricular dos veces al mismo estudiante en la misma materia y periodo
        for mat in self.lista:
            if (mat.estudiante_id == estudiante_id and 
                mat.materia_id == materia_id and 
                mat.periodo == periodo):
                return "El estudiante ya está matriculado en esta materia para este periodo"

        return None

    def leer(self):
        return self.lista

    def obtener(self, id_matricula):
        for matricula in self.lista:
            if matricula.id == id_matricula:
                return matricula
        return None

    def buscar(self, texto):
        texto = texto.strip()
        encontradas = []
        if texto == "":
            return encontradas

        for matricula in self.lista:
            if texto in matricula.periodo or texto in matricula.fecha:
                encontradas.append(matricula)
        return encontradas

    def siguiente(self):
        mayor = 0
        for matricula in self.lista:
            if matricula.id > mayor:
                mayor = matricula.id
        return mayor + 1

    def crear(self, datos):
        error = self.validar(datos)
        if error:
            return False, error

        materia = self.materias.obtener(int(datos["materia_id"]))
        matricula = Matricula(
            self.siguiente(),
            int(datos["estudiante_id"]),
            materia.id,
            str(datos.get("periodo", "2026-1")).strip(),
            datos.get("nota", 0.0)
        )

        materia.ocupar_cupo()
        self.materias.guardar()  # Actualiza cupos en materias.json
        self.lista.append(matricula)
        self.guardar()
        return True, f"Matrícula {matricula.id} registrada con éxito"

    def actualizar(self, id_matricula, datos):
        # Las matrículas en sí no se cambian de estudiante/materia, pero se usa registrar_nota para la nota
        return False, "Use la función de registrar nota para actualizar calificaciones"

    def registrar_nota(self, id_matricula, nota):
        matricula = self.obtener(id_matricula)
        if matricula is None:
            return False, f"No existe la matrícula {id_matricula}"

        if not Materia.es_nota_valida(nota):
            return False, f"Nota inválida: '{nota}' (debe estar entre 0 y 20)"

        matricula.nota = float(nota)
        self.guardar()
        return True, f"Nota registrada correctamente para la matrícula {id_matricula}: {matricula.nota} ({matricula.estado()})"

    def eliminar(self, id_matricula):
        """Retirar matrícula: se borra y el cupo vuelve a la materia."""
        matricula = self.obtener(id_matricula)
        if matricula is None:
            return False, f"No existe la matrícula {id_matricula}"

        materia = self.materias.obtener(matricula.materia_id)
        if materia is not None:
            materia.liberar_cupo()
            self.materias.guardar()

        self.lista.remove(matricula)
        self.guardar()
        return True, f"Matrícula {id_matricula} retirada y cupo devuelto"

    def certificado(self, id_matricula):
        matricula = self.obtener(id_matricula)
        if matricula is None:
            return None

        estudiante = self.estudiantes.obtener(matricula.estudiante_id)
        materia = self.materias.obtener(matricula.materia_id)

        texto = f"CERTIFICADO #{matricula.id}   periodo: {matricula.periodo}\n"
        texto += f"Estudiante: {estudiante.nombre_completo() if estudiante else 'eliminado'}   ({estudiante.carnet if estudiante else 'S/C'})\n"
        texto += f"Materia   : {materia.nombre if materia else 'eliminado'}   ({materia.codigo if materia else 'S/C'}) · {materia.creditos if materia else 0} créditos\n"
        texto += "-" * 42 + "\n"
        texto += f"Nota      : {matricula.nota}\n"
        texto += f"Estado    : {matricula.estado()}"
        return texto

    def matriculas_por_estudiante(self):
        """DICCIONARIO de LISTAS: {estudiante_id: [matrículas de ese estudiante]}."""
        agrupadas = {}
        for matricula in self.lista:
            agrupadas.setdefault(matricula.estudiante_id, []).append(matricula)
        return agrupadas

    def promedio_de_estudiante(self, estudiante_id):
        mats = [m for m in self.lista if m.estudiante_id == estudiante_id]
        if not mats:
            return 0.0
        suma = sum(m.nota for m in mats)
        return round(suma / len(mats), 2)