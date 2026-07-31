from src.loader import EEGLoader
from src.ica_processor import ICAProcessor
from src.visualizer import EEGVisualizer
from src.quality_analyzer import EEGQualityAnalyzer
from src.report_generator import ReportGenerator


# =========================
# 1. Cargar EEG
# =========================

loader = EEGLoader()

raw = loader.load()


# =========================
# 2. Entrenar ICA
# =========================

processor = ICAProcessor()

print("Entrenando ICA...")

processor.fit(raw)

print("Entrenamiento terminado.")


# Visualizar componentes ICA
processor.get_ica().plot_components()


# =========================
# 3. Detectar y eliminar EOG
# =========================

raw_clean, eog_scores = processor.remove_eog(raw)


print("Scores EOG:")
print(eog_scores)


# =========================
# 4. Calcular calidad EEG
# =========================

analyzer = EEGQualityAnalyzer()

quality_score = analyzer.calculate_quality(
    eog_scores
)

print("Quality score calculado:", quality_score)
print("Máximo artefacto detectado:", max(abs(eog_scores)))

print(
    "EEG Quality Score:",
    quality_score,
    "%"
)

report = ReportGenerator()

report.generate(
    raw,
    quality_score,
    eog_scores,
    processor.ica.exclude,
    processor.ica.n_components
)

# =========================
# 5. Visualización
# =========================

visualizer = EEGVisualizer()


# Barra de calidad
visualizer.plot_quality_score(
    quality_score
)


# Comparación señal original vs limpia

raw.plot(
    title="EEG Original",
    duration=10,
    n_channels=20
)


raw_clean.plot(
    title="EEG Limpio",
    duration=10,
    n_channels=20
)