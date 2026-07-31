import mne
from pathlib import Path


class EEGLoader:

    def __init__(self):
        self.sample_path = Path(mne.datasets.sample.data_path())

    def load(self):
        raw_file = (
            self.sample_path
            / "MEG"
            / "sample"
            / "sample_audvis_raw.fif"
        )

        raw = mne.io.read_raw_fif(raw_file, preload=True)

        return raw