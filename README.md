# NeuroQC

### Automated EEG Quality Assessment using Independent Component Analysis (ICA)

NeuroQC is a Python-based tool for evaluating EEG signal quality through automatic detection of ocular artifacts (EOG) using Independent Component Analysis (ICA).

The project is designed to identify blink-related components, assess signal contamination, and generate an automated quality report before downstream EEG processing or neuroscience research.

---

## Overview

Electroencephalography (EEG) recordings are commonly contaminated by physiological and environmental artifacts that reduce signal quality and may affect subsequent analyses.

NeuroQC focuses on detecting ocular artifacts (EOG) by applying Independent Component Analysis (ICA), allowing researchers to identify contaminated components and evaluate the overall quality of EEG recordings.

---

## Key Features

* Load EEG recordings using MNE-Python
* Perform Independent Component Analysis (ICA)
* Automatically detect ocular (EOG) artifacts
* Evaluate EEG signal quality
* Generate automated quality assessment reports
* Modular and extensible Python architecture

---

## Processing Pipeline

```text
Raw EEG Recording
        │
        ▼
Load EEG Data (MNE-Python)
        │
        ▼
Preprocessing
        │
        ▼
Independent Component Analysis (ICA)
        │
        ▼
EOG Artifact Detection
        │
        ▼
Quality Assessment
        │
        ▼
Automated Report Generation
```

---

## Project Structure

```text
eeg-blink-removal-ica/
│
├── main.py
│
├── src/
│   ├── loader.py
│   ├── ica_processor.py
│   ├── quality_analyzer.py
│   ├── report_generator.py
│   └── visualizer.py
│
├── results/
│   └── neuroqc_report.txt
│
├── requirements.txt
│
└── README.md
```

---

## Technologies

* Python
* MNE-Python
* NumPy
* Matplotlib

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Jennycbrpl/eeg-blink-removal-ica.git
cd eeg-blink-removal-ica
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the analysis:

```bash
python main.py
```

After execution, NeuroQC will:

1. Load the EEG recording.
2. Perform ICA decomposition.
3. Detect components correlated with ocular activity.
4. Evaluate signal quality.
5. Generate an automated quality assessment report.

---

## Example Output

```text
===============================
        EEG Quality Report
===============================

Artifact Type:
Eye movement (EOG)

Detected ICA Component:
1

Maximum EOG Correlation:
0.929

Quality Score:
7.08%

Severity:
HIGH

Recommendation:
ICA cleaning recommended
```

---

## Example Results

| Metric              |                    Value |
| ------------------- | -----------------------: |
| Artifact Type       |       Eye Movement (EOG) |
| ICA Component       |                        1 |
| Maximum Correlation |                    0.929 |
| Quality Score       |                    7.08% |
| Severity            |                     HIGH |
| Recommendation      | ICA cleaning recommended |

---

## Future Improvements

* Detection of EMG artifacts
* Detection of ECG artifacts
* Additional EEG quality metrics
* Interactive visualization dashboard
* PDF report generation
* Support for multiple EEG datasets
* Machine learning-based artifact classification

---

## Contributing

Contributions are welcome.

If you would like to improve NeuroQC, feel free to fork the repository, create a feature branch, and submit a pull request.

---

## License

This project is released under the MIT License.


---

## Author | Autor

Jenny Cabrera
