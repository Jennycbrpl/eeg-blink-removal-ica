from mne.preprocessing import ICA


class ICAProcessor:

    def __init__(self, n_components=20, random_state=42):

        self.ica = ICA(
            n_components=n_components,
            random_state=random_state
        )


    def fit(self, raw):

        self.ica.fit(raw)


    def get_ica(self):

        return self.ica


    def remove_eog(self, raw):

        # Detectar componentes relacionados con parpadeo
        eog_indices, scores = self.ica.find_bads_eog(raw)

        print(
            "Componentes EOG encontrados:",
            eog_indices
        )


        # Guardar componentes que serán eliminados
        self.ica.exclude = eog_indices


        # Crear copia para no modificar el EEG original
        raw_clean = raw.copy()


        # Aplicar limpieza ICA
        self.ica.apply(raw_clean)


        # Devolvemos:
        # 1. EEG limpio
        # 2. scores para calcular calidad después
        return raw_clean, scores