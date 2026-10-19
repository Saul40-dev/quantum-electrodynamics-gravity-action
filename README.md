# Acción Unificada de Einstein-Maxwell-Dirac (EMD)

## Resumen / Abstract
Este repositorio documenta la formulación matemática de una **Acción Unificada** ($\mathcal{S}$) que integra la curvatura del espacio-tiempo (Relatividad General), la dinámica del campo electromagnético (Ecuaciones de Maxwell) y la función de onda de materia cuántica con espín 1/2 (Ecuación de Dirac).

El objetivo de este proyecto es analizar la consistencia dimensional y el límite clásico electrostático (Ley de Coulomb) a partir de la variación de la Acción en marcos de referencia estáticos y relativistas.

---

## 1. Formulación Matemática Formal

La Acción del sistema completo en notación de campos en espacio-tiempo curvo está dada por:

$$ \mathcal{S} = \int d^4x \sqrt{-g} \left[ \frac{c^4}{16\pi G} R - \frac{1}{4} F_{\alpha\beta} F^{\alpha\beta} + \bar{\psi}(i \hbar \gamma^\mu D_\mu - m c)\psi \right] $$

### Definición de Variables y Tensores

| Símbolo | Nombre Físico | Definición / Unidades |
| :--- | :--- | :--- |
| $\mathcal{S}$ | **Acción Total** | Magnitud escalar en Joules-segundo ($\text{J}\cdot\text{s}$). |
| $d^4x$ | **Elemento de Volumen Espaciotemporal** | $dx^0 dx^1 dx^2 dx^3 = c dt \, dx \, dy \, dz$. |
| $\sqrt{-g}$ | **Determinante de la Métrica** | Invariante geométrico que sustituye al factor de Lorentz $\gamma$ en espacio curvo. |
| $c$ | **Velocidad de la Luz** | $2.99792458 \times 10^8 \text{ m/s}$. |
| $G$ | **Constante Gravitacional** | $6.67430 \times 10^{-11} \text{ m}^3\text{kg}^{-1}\text{s}^{-2}$. |
| $R$ | **Escalar de Ricci** | Contracción del tensor de curvatura de Riemann ($g^{\mu\nu} R_{\mu\nu}$). |
| $F_{\alpha\beta}$ | **Tensor Electromagnético** | $F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha$. |
| $\psi, \bar{\psi}$ | **Espinores de Dirac** | Función de onda cuántica y su adjunto de Dirac ($\bar{\psi} = \psi^\dagger \gamma^0$). |
| $\hbar$ | **Constante de Planck Reducida** | $1.054571817 \times 10^{-34} \text{ J}\cdot\text{s}$. |
| $\gamma^\mu$ | **Matrices de Dirac** | Matrices $4 \times 4$ que satisfacen el álgebra de Clifford $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$. |
| $D_\mu$ | **Derivada Covariante de Gauge** | $D_\mu = \partial_\mu + \frac{ie}{\hbar} A_\mu$ (mecanismo de interacción electromagnética). |
| $m$ | **Masa de la Partícula** | Masa en reposo del fermión en kilogramos ($\text{kg}$). |

---

## 2. Derivación de Límites Clásicos ($\delta \mathcal{S} = 0$)

Al aplicar el **Principio de Mínima Acción**, se obtienen los tres pilares de la física fundamental:

1. **Variación respecto a $g_{\mu\nu}$ ($\delta \mathcal{S} / \delta g_{\mu\nu} = 0$):**
   Produce las **Ecuaciones de Campo de Einstein**:
   $$ R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \frac{8\pi G}{c^4} T_{\mu\nu} $$

2. **Variación respecto al potencial $A_\mu$ ($\delta \mathcal{S} / \delta A_\mu = 0$):**
   Produce las **Ecuaciones de Maxwell Covariantes**:
   $$ \nabla_\alpha F^{\alpha\beta} = \mu_0 J^\beta $$
   En el límite estático ($\vec{v} = 0$) y en espacio plano ($g_{\mu\nu} = \eta_{\mu\nu}$), esto colapsa exactamente en la **Ley de Coulomb**:
   $$ F_e = \frac{1}{4\pi \varepsilon_0} \frac{|q_1 q_2|}{r^2} $$

3. **Variación respecto al espinor $\bar{\psi}$ ($\delta \mathcal{S} / \delta \bar{\psi} = 0$):**
   Produce la **Ecuación de Dirac Relativista**:
   $$ (i \hbar \gamma^\mu D_\mu - m c)\psi = 0 $$

---

## 3. Pruebas y Evidencia Numérica de Validación

Las pruebas del modelo se validan mediante la recuperación de datos electrostáticos en reposo (métrica plana de Minkowski $\eta_{\mu\nu}$, $\gamma = 1$).

### Parámetros del Experimento Controlado
* **Carga $q_1$:** $-2 \times 10^{-6} \text{ C}$ ($-2 \, \mu\text{C}$)
* **Carga $q_2$:** $+4 \times 10^{-6} \text{ C}$ ($+4 \, \mu\text{C}$)
* **Distancia de separación ($r$):** $0.04 \text{ m}$ ($4 \text{ cm}$)
* **Constante electrostática ($K = \frac{1}{4\pi\varepsilon_0}$):** $8.98755 \times 10^9 \text{ N}\cdot\text{m}^2/\text{C}^2$

### Cálculo de Fuerza Electrostática
$$ F_e = 8.98755 \times 10^9 \times \frac{|(-2 \times 10^{-6})(4 \times 10^{-6})|}{(0.04)^2} = 44.9377 \text{ N} $$

### Cálculo de Trabajo/Energía del Sistema
$$ E = F_e \cdot r = 44.9377 \text{ N} \times 0.04 \text{ m} = 1.7975 \text{ Joules} $$

---

## 4. Licencia y Derechos de Autor

Este trabajo está protegido bajo la Licencia **Creative Commons Attribution 4.0 International (CC BY 4.0)**. 
Eres libre de compartir y adaptar el material siempre que otorgues el crédito correspondiente al autor original.
