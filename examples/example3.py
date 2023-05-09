#### Example 3: Get rcParams as dict and set style over seaborn library

import seaborn as sns
from matplotlib import _rc_params_in_file

if __name__ == "__main__":
    plt.style.use('default') #reset to default first
    
    style_list = [
        "https://raw.githubusercontent.com/Schoepfloeffel/mplstyles/main/schoepfloeffel_style_1.mplstyle",
        "https://raw.githubusercontent.com/Schoepfloeffel/mplstyles/main/schoepfloeffel_style_2.mplstyle"
    ]

    # Load dataset from seaborn
    mpg = sns.load_dataset("mpg")

    # Get the stylesheet as dict from URL and use seaborns set_theme context
    for style_label in style_list:
        rcParams_from_url = dict(_rc_params_in_file(style_label))
        sns.set_theme(
            rc=rcParams_from_url
        )  # set the theme for axis, style, palette of seaborn plots. Will set mpl.rcParams.update(rc) under the hood for global change.
        sns.relplot(
            x="horsepower",
            y="mpg",
            hue="origin",
            size="weight",
            sizes=(40, 400),
            alpha=0.5,
            height=6,
            data=mpg,
        )
