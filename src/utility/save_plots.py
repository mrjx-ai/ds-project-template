def export_figs(fig, filename, export_dir):
    import os

    filepath = os.path.join(export_dir, filename)
    fig.savefig(filepath)
