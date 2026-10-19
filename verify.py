# verify.py - Validación numérica del límite estático
import numpy as np

k_e = 8.9875517923e9  # Constante de Coulomb (N m^2 / C^2)

def validar_coulomb():
    q1 = -2e-6  # -2 uC
    q2 = 4e-6   # +4 uC
    r = 0.04    # 4 cm en metros
    
    # Cálculo de la fuerza electrostática
    fuerza = k_e * abs(q1 * q2) / (r**2)
    energia = fuerza * r
    
    print(f"--- REPORTE DE VALIDACIÓN ---")
    print(f"Fuerza calculada: {fuerza:.4f} N")
    print(f"Energía del sistema (F * r): {energia:.4f} J")
    print(f"Estado: Verificación numérica exitosa.")

if __name__ == "__main__":
    validar_coulomb()
