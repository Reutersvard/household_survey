import pandas as pd
import numpy as np
import plotly.express as px


def bar_plotter(df, var1, y, var2):
    
    view = (
        df.query(f"{var1} != 'All' & {var2} != 'All'")
        .groupby([var1, var2]).mean().reset_index()
    )
    
    fig = px.bar(view, x=var1, y=y, color=var2, barmode='group', width=600, height=400)
    
    return fig.show('notebook')


def greenspace_plotter(df, var1, var2):
    
    var_switch = {'short': 'A 5 minute walk or less',
                  'long': 'An 11 minute walk or more',
                  'medium': 'Within a 6-10 minute walk'
    }
    
    option = var_switch[var2]
    
    view = (
        df.query(f"{var1} != 'All' & nearest_green_space == @option")
        .groupby(['year', var1])
        .mean('percent_adults')
        .reset_index()
        .sort_values('year')
    )

    fig = (px.line(view, x="year", y="percent_adults", color=var1,
        title=f'Percentage of adults living {option} from green spaces', markers=True)
    )

    return fig.show('notebook')


def merger(df1, df2, df3):

    # Merge on every common column, keep all records
    survey = (pd.merge(pd.merge(df1, df2, how='outer',), df3, how='outer',
              
    # Drop confidence interval values and redundant columns.
    # Replace NAs in the ratings and age columns with the 'All' value that signifies being held constant.                  
    ).query("measurement == 'Percent'")
    .drop(columns=['measurement', 'units']).fillna('All').copy()
    .rename(columns={"distance_to_nearest_green_or_blue_space": "nearest_green_space", 
    "value": "percent_adults", "datecode": "year"})
    )

    # Wrangling nearest_green_space to incorporate missing information from walking_distance_to_nearest_greenspace
    survey['nearest_green_space'] = (np.where(
        survey.nearest_green_space.isin(['All', "Don't Know"]), 
        survey.walking_distance_to_nearest_greenspace, survey.nearest_green_space))

    # Information is taken, column can be dropped
    survey = survey.drop('walking_distance_to_nearest_greenspace', axis=1).copy()

    # Re-binning the column, making the conservative assumption: 'Less than 10 minutes' means 'Within a 6-10 minute walk' rather than 'A 5 minute walk or less'
    survey['nearest_green_space'] = (np.where(
        survey.nearest_green_space == 'More than 10 minutes', 
        'An 11 minute walk or more', np.where(
        survey.nearest_green_space == 'Less than 10 minutes', 
        'Within a 6-10 minute walk', survey.nearest_green_space)))
    
    return survey


def df_std(df, var, par):

    dfout = pd.DataFrame()

    predictors = list(df.columns)

    option = par

    for col in predictors:
        view = (df.query(f"{var} == @option & {col} != 'All'")
            .groupby([col])
            .mean()
        )

        dfout[col] = view.std()

    return dfout