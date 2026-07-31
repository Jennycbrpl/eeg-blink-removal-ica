# NeuroQC

**Automated EEG artifact detection and quality assessment using Independent Component Analysis (ICA).**

**Herramienta automatizada para detección de artefactos EEG y evaluación de calidad de señal mediante Análisis de Componentes Independientes (ICA).**

---

## Overview | Descripción general

**English**

NeuroQC is a Python-based tool designed to analyze EEG recordings and evaluate signal quality by detecting ocular artifacts (EOG) using ICA.

The objective is to provide an automated assessment of EEG contamination before further neuroscience analysis.

**Español**

NeuroQC es una herramienta desarrollada en Python para analizar registros EEG y evaluar la calidad de la señal mediante la detección de artefactos oculares (EOG) utilizando ICA.

El objetivo es proporcionar una evaluación automatizada de la contaminación de la señal EEG antes de realizar análisis neurocientíficos posteriores.

---

## Problem | Problema

**English**

EEG recordings are affected by artifacts that can reduce signal reliability, including:

* Eye movements and blinking (EOG)
* Muscle activity (EMG)
* Environmental noise

These artifacts can interfere with EEG interpretation and analysis.

**Español**

Los registros EEG están afectados por artefactos que pueden reducir la confiabilidad de la señal, incluyendo:

* Movimientos oculares y parpadeos (EOG)
* Actividad muscular (EMG)
* Ruido ambiental

Estos artefactos pueden afectar la interpretación y análisis de señales EEG.

---

## Solution | Solución

**English**

NeuroQC applies Independent Component Analysis (ICA) to separate EEG signals into independent components and identify components associated with ocular activity.

The system generates an automated quality assessment report describing detected artifacts and their severity.

**Español**

NeuroQC aplica Análisis de Componentes Independientes (ICA) para separar las señales EEG en componentes independientes e identificar aquellos asociados con actividad ocular.

El sistema genera un reporte automatizado de calidad describiendo los artefactos detectados y su nivel de severidad.

---

## Pipeline | Flujo del sistema

```text
EEG Recording
      |
      v
EEG Loading (MNE-Python)
      |
      v
ICA Decomposition
      |
      v
EOG Artifact Detection
      |
      v
Quality Assessment
      |
      v
Automated Report Generation
```

---

## Features | Características

* EEG data loading using MNE-Python
  Carga de datos EEG utilizando MNE-Python

* ICA decomposition for artifact separation
  Descomposición ICA para separación de artefactos

* Automatic EOG artifact detection
  Detección automática de artefactos oculares

* EEG quality scoring
  Cálculo de calidad de señal EEG

* Automated analysis report generation
  Generación automática de reportes de análisis

* Modular Python architecture
  Arquitectura modular en Python

---

## Example Result | Ejemplo de resultado

```text
Artifact type:
Eye movement (EOG)

Tipo de artefacto:
Movimiento ocular (EOG)


ICA Component:
1


Maximum EOG Correlation:
0.929


Severity:
HIGH

Severidad:
ALTA


Recommendation:
ICA cleaning recommended

Recomendación:
Se recomienda limpieza mediante ICA
```

---

## Project Structure | Estructura del proyecto

```text
NeuroQC/

├── main.py

├── src/
│   ├── loader.py
│   ├── ica_processor.py
│   ├── quality_analyzer.py
│   ├── report_generator.py
│   └── visualizer.py

└── results/
    └── neuroqc_report.txt
```

---

## Technologies | Tecnologías

* Python
* MNE-Python
* NumPy
* Matplotlib

---

## Installation | Instalación

Install dependencies:

```bash
pip install -r requirements.txt
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python main.py
```

Ejecuta el análisis:

```bash
python main.py
```

---

## Future Improvements | Mejoras futuras

* Detection of additional artifacts such as EMG and ECG
  Detección de artefactos adicionales como EMG y ECG

* More EEG quality metrics
  Más métricas de calidad EEG

* Automated visualization reports
  Reportes visuales automatizados

* Support for additional EEG datasets
  Soporte para más datasets EEG

---

## Author | Autor

Jenny Cabrera
