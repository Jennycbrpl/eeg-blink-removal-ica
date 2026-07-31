from pathlib import Path


class ReportGenerator:

    def __init__(self, output_path="results/neuroqc_report.txt"):
        self.output_path = Path(output_path)


    def generate(
        self,
        raw,
        quality_score,
        eog_scores,
        eog_components,
        n_components
    ):

        max_correlation = max(abs(eog_scores))

        duration = raw.times[-1]
        channels = raw.info["nchan"]
        sfreq = raw.info["sfreq"]


        if max_correlation >= 0.8:
            severity = "HIGH"
            recommendation = "ICA cleaning recommended"

        elif max_correlation >= 0.5:
            severity = "MODERATE"
            recommendation = "Review artifacts"

        else:
            severity = "LOW"
            recommendation = "Signal quality acceptable"


        report = f"""
==============================
          NeuroQC Report
==============================


DATASET INFORMATION
------------------------------

Channels:
{channels}

Sampling frequency:
{sfreq} Hz

Recording duration:
{duration:.2f} seconds



ICA ANALYSIS
------------------------------

Total components:
{n_components}

Removed components:
{eog_components}



ARTIFACT DETECTION
------------------------------

Artifact type:
Eye movement (EOG)

Detected component:
{eog_components}

Maximum correlation:
{max_correlation:.3f}



QUALITY ASSESSMENT
------------------------------

Quality score:
{quality_score} %

Severity:
{severity}


Recommendation:
{recommendation}

"""

        self.output_path.parent.mkdir(
            exist_ok=True
        )


        with open(
            self.output_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)


        print(
            f"Report saved at {self.output_path}"
        )