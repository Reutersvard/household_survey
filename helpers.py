import pandas as pd
import numpy as np
import seaborn as sns
import janitor


def weighted_average(df, values, weights):
    return sum(df[weights] * df[values]) / df[weights].sum()


def bivar_plotter(df, var1, var2):
    
    view = (
        df.query(f"{var1} != 'All' & {var2} != 'All'")
        .groupby([var1, var2]).mean().reset_index()
    )
    
    return sns.barplot(data=view, x=var1, y='value', hue=var2)


def green_space_plotter(df, var1, var2):
    
    var_switch = {'long': 'More than 10 minutes',
                  'short': 'Less than 10 minutes'}
    
    option = var_switch[var2]
    
    view = (
        df.query(f"{var1} != 'All' & walking_distance_to_nearest_greenspace == @option")
        .groupby(['datecode', var1]).mean('value'))

    return sns.lineplot(x = 'datecode', y = 'value', hue = var1, data = view)


def merger(df1, df2, df3):

    # Merge on every common column
    survey = pd.merge(pd.merge(

        df1, df2, how='outer',
        left_on=['featurecode', 'datecode', 'measurement', 'units', 'value', 'gender', 'urban_rural_classification',
                'simd_quintiles', 'type_of_tenure', 'household_type', 'ethnicity', 'walking_distance_to_nearest_greenspace'],
        right_on=['featurecode', 'datecode', 'measurement', 'units', 'value', 'gender', 'urban_rural_classification',
                'simd_quintiles', 'type_of_tenure', 'household_type', 'ethnicity', 'walking_distance_to_nearest_greenspace'],
                ),

            df3, how='outer',
                left_on=['featurecode', 'datecode', 'measurement', 'units', 'value', 'gender', 'urban_rural_classification',
                        'simd_quintiles', 'type_of_tenure', 'household_type', 'ethnicity', 'walking_distance_to_nearest_greenspace'],
                right_on=['featurecode', 'datecode', 'measurement', 'units', 'value', 'gender', 'urban_rural_classification',
                         'simd_quintiles', 'type_of_tenure', 'household_type', 'ethnicity', 'walking_distance_to_nearest_greenspace']
                    
    # Drop confidence interval values, regional values and redundant columns.
    # Replace NAs in the ratings columns with the 'All' value that signifies being held constant.                  
    ).query("featurecode == 'S92000003' & measurement == 'Percent'").drop(columns=['featurecode', 'measurement', 'units']).fillna('All').copy()
    
    return survey