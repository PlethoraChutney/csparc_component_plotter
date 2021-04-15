import numpy as np
import pandas as pd
import plotly.express as px
from glob import glob
import sys
import os

def main():

    passthrough_files = glob(os.path.normpath(sys.argv[1]))
    reduce_by = int(sys.argv[2])
    df_dict = {
    'Component 0': [],
    'Component 1': [],
    'Component 2': [],
    'Group': []
    }

    i = 0
    while i < len(passthrough_files):
        data = np.load(passthrough_files[i])
        df_dict['Component 0'].extend(data['components_mode_0/value'])
        df_dict['Component 1'].extend(data['components_mode_1/value'])
        df_dict['Component 2'].extend(data['components_mode_2/value'])
        df_dict['Group'].extend([str(i)] * len(data))

        i += 1

    df = pd.DataFrame(data = df_dict)[::reduce_by]

    fig = px.scatter_3d(
        df,
        x = 'Component 0',
        y = 'Component 1',
        z = 'Component 2',
        color = 'Group'
    )
    fig.update_traces(
        marker = dict(
            size = 5,
            line = dict(width = 1, color = 'DarkSlateGrey')
        )
    )

    fig.write_html('component_plot.html')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: plotly_maker.py [data .cs glob] [reduce_by] [width] [height]')
    else:
        main()
