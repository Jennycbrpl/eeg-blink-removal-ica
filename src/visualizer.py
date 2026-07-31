import matplotlib.pyplot as plt


class EEGVisualizer:

    def plot_quality_score(self, score):

        if score >= 70:
            color = "green"
            status = "GOOD"

        elif score >= 40:
            color = "orange"
            status = "WARNING"

        else:
            color = "red"
            status = "BAD"


        fig, ax = plt.subplots(figsize=(8, 2))


        # barra completa (fondo)
        ax.barh(
            ["EEG Quality"],
            [100],
            color="lightgray"
        )


        # barra del score
        ax.barh(
            ["EEG Quality"],
            [score],
            color=color
        )


        ax.set_xlim(0,100)

        ax.set_xlabel(
            f"Quality Score: {score}% - {status}"
        )


        plt.title(
            "EEG Signal Quality Assessment"
        )


        plt.show()