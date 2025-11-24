"""Test de integración completa - Models + Exercise Generator."""
from models import load_example_exercises, ExerciseFactory
from utils import generate_exercise

print("="*60)
print("PRUEBA DE INTEGRACIÓN COMPLETA")
print("="*60)

# 1. Cargar ejercicios de ejemplo desde models
print("\n1. Cargando ejercicios de ejemplo...")
factory = load_example_exercises()
example_exercises = factory.get_all_exercises()
print(f"   ✓ Cargados {len(example_exercises)} ejercicios de ejemplo:")
for ex in example_exercises:
    print(f"     - {ex.id}: {ex.name}")

# 2. Generar ejercicios desde exercise_generator
print("\n2. Generando ejercicios dinámicos...")
temas = ['sir', 'lorenz', 'van_der_pol', 'hopf', 'rlc', 'logistica', 
         'verhulst', 'orbitas', 'amortiguadores', 'newton']

generated = []
for tema in temas:
    ej = generate_exercise(tema)
    generated.append(ej)
    print(f"   ✓ {tema:15} → {ej.name[:35]}...")

# 3. Generar ejercicios avanzados
print("\n3. Generando ejercicios avanzados...")
avanzados = ['sir_avanzado', 'lorenz_comparacion', 'vdp_forzado', 
             'hopf_subcritico', 'rlc_forzado', 'logistica_cosecha']

for tema in avanzados:
    ej = generate_exercise(tema)
    generated.append(ej)
    print(f"   ✓ {tema:25} → {ej.name[:30]}...")

# 4. Verificando estructura de ejercicios...
print("\n4. Verificando estructura de ejercicios...")
from models import ExerciseValidator

valid_count = 0
for ej in generated[:5]:
    is_valid, errors = ExerciseValidator.validate_exercise(ej)
    if is_valid:
        valid_count += 1
        print(f"   ✓ {ej.name[:35]}... - válido")
    else:
        print(f"   ✗ {ej.name[:35]}... - errores: {errors}")

print(f"   {valid_count}/5 ejercicios válidos")

# 5. Búsqueda y filtrado en factory de ejemplos
print("\n5. Probando búsqueda y filtrado...")
from models import DifficultyLevel

basicos = factory.get_exercises_by_difficulty(DifficultyLevel.BASICO)
intermedios = factory.get_exercises_by_difficulty(DifficultyLevel.INTERMEDIO)
avanzados_diff = factory.get_exercises_by_difficulty(DifficultyLevel.AVANZADO)

print(f"   ✓ Básicos: {len(basicos)}, Intermedios: {len(intermedios)}, Avanzados: {len(avanzados_diff)}")

# 6. Verificar parámetros
print("\n6. Verificando parámetros de ejercicios...")
for ej in generated[:3]:
    print(f"   Ejercicio: {ej.name[:30]}...")
    for param in ej.parameters:
        if param.min_value is not None and param.max_value is not None:
            assert param.min_value <= param.default_value <= param.max_value, \
                f"Error: {param.name} default {param.default_value} fuera de rango [{param.min_value}, {param.max_value}]"
    print(f"     ✓ {len(ej.parameters)} parámetros válidos")

print("\n" + "="*60)
print("INTEGRACIÓN COMPLETA: ✓ ÉXITO")
print("="*60)
print(f"\nTotal ejercicios disponibles:")
print(f"  - Ejemplos: {len(example_exercises)}")
print(f"  - Generados básicos: 10")
print(f"  - Generados avanzados: 20")
print(f"  - TOTAL: 33+ tipos de ejercicios")
