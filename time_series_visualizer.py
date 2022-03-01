import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
dfi = pd.read_csv('fcc-forum-pageviews.csv')
dfi["date"] = pd.to_datetime(dfi["date"])
dfi = dfi.set_index('date')

# Clean data
df = dfi[(dfi['value'] >= dfi['value'].quantile(0.025)) &
        (dfi['value'] <= dfi['value'].quantile(0.975))]
        
def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (15,5))
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    sns.lineplot(data=df, legend=False, x = 'date', y = 'value', color = 'red')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df.copy()
    df_bar["Years"] = df_bar.index.year
    df_bar["Months"] = df_bar.index.month_name()
    df_bar = df_bar.rename(columns={"value": "Average Page Views"})

    # Draw bar plot
    fig, ax1 = plt.subplots(figsize=(12,10))
    sns.barplot(data = df_bar, y = 'Average Page Views', hue = 'Months', x="Years",  palette="tab10", ci=None, hue_order = new_order)
    plt.legend(loc='upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box = df_box.rename(columns={"value": "Page Views", 'year':'Year', 'month': 'Month'})
    new_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(15,5))
    sns.boxplot(data = df_box, x = 'Year', y = 'Page Views', ax=ax[0]).set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(data = df_box, x = 'Month', y = 'Page Views', ax=ax[1], order = new_order).set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
