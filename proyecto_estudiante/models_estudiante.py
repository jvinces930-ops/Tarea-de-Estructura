from datetime import date


# =====================================================================
# CLASE BASE (Ya provista en la guía)
# =====================================================================
class ModeloBase:
    """Padre de todos los modelos. Guarda el id y define el comportamiento común."""

    def __init__(self, id_registro):
        self.id = int(id_registro)

    @classmethod
    def desde_diccionario(cls, datos):
        """Diccionario -> objeto. Escrito UNA vez y usado por los tres modelos."""
        datos = dict(datos)
        id_registro = datos.pop("id")
        return cls(id_registro, **datos)

    def a_diccionario(self):
        return {"id": self.id}

    def etiqueta(self):
        return f"registro {self.id}"

    def __str__(self):
        return f"[{self.id}] {self.etiqueta()}"


# =====================================================================
# PERSONA (Ya provista en la guía)
# =====================================================================
class Persona(ModeloBase):
    """Todo lo que tiene una persona del sistema."""

    def __init__(self, id_registro, nombre, apellido, email):
        super().__init__(id_registro)
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["nombre"] = self.nombre
        datos["apellido"] = self.apellido
        datos["email"] = self.email
        return datos

    def etiqueta(self):
        return self.nombre_completo()


# =====================================================================
# 1. ESTUDIANTE (Equivalente a Cliente)
# =====================================================================
class Estudiante(Persona):
    """Estudiante ES UNA Persona, con carnet y carrera."""

    def __init__(self, id_registro, nombre, apellido, email, carnet="", carrera=""):
        super().__init__(id_registro, nombre, apellido, email)
        self.carnet = carnet
        self.carrera = carrera

    def a_diccionario(self):
        datos = super().a_diccionario()  # Recupera id, nombre, apellido y email
        datos["carnet"] = self.carnet
        datos["carrera"] = self.carrera
        return datos

    def etiqueta(self):
        # Polimorfismo: extiende la etiqueta del padre sumando carnet y carrera
        return f"{super().etiqueta()} · {self.carnet} · {self.carrera or 'sin carrera'}"


# =====================================================================
# 2. MATERIA (Equivalente a Producto - Contiene atributos y métodos estáticos)
# =====================================================================
class Materia(ModeloBase):
    """Materia ES UN ModeloBase. Aquí viven las reglas estáticas."""

    # Atributos estáticos (compartidos para todo el programa)
    CUPOS_MAXIMOS = 30
    NOTA_APROBACION = 14

    def __init__(self, id_registro, nombre, codigo, creditos=0, cupos=0):
        super().__init__(id_registro)
        self.nombre = nombre
        self.codigo = str(codigo).upper()
        self.creditos = int(creditos)
        self.cupos = int(cupos)

    # Método estático: valida si una nota está entre 0 y 20
    @staticmethod
    def es_nota_valida(valor):
        try:
            nota = float(valor)
            return 0 <= nota <= 20
        except (TypeError, ValueError):
            return False

    # Métodos de instancia para manipular los cupos
    def hay_cupo(self):
        return self.cupos > 0

    def ocupar_cupo(self):
        if self.hay_cupo():
            self.cupos -= 1

    def liberar_cupo(self):
        if self.cupos < Materia.CUPOS_MAXIMOS:
            self.cupos += 1

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["nombre"] = self.nombre
        datos["codigo"] = self.codigo
        datos["creditos"] = self.creditos
        datos["cupos"] = self.cupos
        return datos

    def etiqueta(self):
        alerta = " ⚠ sin cupos" if not self.hay_cupo() else ""
        return f"{self.nombre} ({self.codigo}) · {self.creditos} créditos · cupos: {self.cupos}{alerta}"


# =====================================================================
# 3. MATRICULA (Equivalente a Venta - Une estudiante y materia)
# =====================================================================
class Matricula(ModeloBase):
    """Matrícula simple: un estudiante, una materia, periodo y nota."""

    def __init__(self, id_registro, estudiante_id, materia_id, periodo="", nota=0.0, fecha=""):
        super().__init__(id_registro)
        self.estudiante_id = int(estudiante_id)
        self.materia_id = int(materia_id)
        self.periodo = periodo or "2026-1"
        self.nota = float(nota) if nota != "" else 0.0
        self.fecha = fecha or date.today().isoformat()

    def esta_aprobada(self):
        return self.nota >= Materia.NOTA_APROBACION

    def estado(self):
        # Se calcula en tiempo real, no se guarda como atributo fijo
        return "Aprobado" if self.esta_aprobada() else "Reprobado"

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["estudiante_id"] = self.estudiante_id
        datos["materia_id"] = self.materia_id
        datos["periodo"] = self.periodo
        datos["nota"] = self.nota
        datos["fecha"] = self.fecha
        return datos

    def etiqueta(self):
        return (f"{self.fecha} · periodo {self.periodo} · estudiante {self.estudiante_id} "
                f"en materia {self.materia_id} · nota: {self.nota} ({self.estado()})")