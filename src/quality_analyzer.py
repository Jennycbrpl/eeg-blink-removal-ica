import numpy as np


class EEGQualityAnalyzer:

    def calculate_quality(self, eog_scores):

        # Tomamos la mayor correlación con parpadeo
        max_artifact = np.max(np.abs(eog_scores))


        # Convertimos artefacto a calidad
        quality = (1 - max_artifact) * 100


        return round(quality, 2)