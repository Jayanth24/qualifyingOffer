"""
Jayanth Gunda's solution to Question 2 of the Phillies
Baseball R&D Questionnaire.
"""

""" 
Import statements needed for the Python program. 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

""" 
Constant values needed for the Python program. 
"""
HTML_PAGE = "https://questionnaire-148920.appspot.com/swe/data.html"
NUM_TOP_PLAYERS = 125

def read_salary_data(html):
  """
  Function that reads in the salary data from the provided HTML, and 
  converts it into a Pandas DataFrame.

  Parameters
  ----------
  html : string
    HTML page where the salary data is located.

  Returns
  -------
  pd.DataFrame
    The parsed Salary Pandas DataFrame from the HTML page.
  """
  salary_data_table_list = pd.read_html(html)
  salary_data = salary_data_table_list[0]
  return salary_data

def convert_salary_to_float(salary):
  """
  Function that is applied row-wise on each dollar value in the salary
  column to convert its dollar representation from an object to a floating
  point number. 

  All corrupted and malformed salary entries are converted into np.NaN values,
  to ensure that they don't interfere in the calculation of the final qualifying
  offer amount (as they will not be among the top NUM_TOP_PLAYERS - currently 125 -
  salaries).

  Parameters
  ----------
  salary : string
    The salary entry to be converted into a float.

  Returns
  -------
  float
    Either np.NaN if the salary entry is corrupted or malformed, or the 
    converted floating point salary entry otherwise.
  """
  if pd.isna(salary):
    return np.NaN
  salary_amount = salary.translate(salary.maketrans("$,", "  ")).replace(" ", "")
  if salary_amount.isdigit():
    return float(salary_amount)
  else:
    return np.NaN

def sort_salary_data(salary_data):
  """
  Function that sorts the provided Salary DataFrame by descending order of the Salary
  column, in order to allow efficient calculation of the qualifying offer.

  Parameters
  ----------
  salary_data : pd.DataFrame
    The Salary Pandas DataFrame to be sorted.

  Returns
  -------
  pd.DataFrame
    The Salary Pandas DataFrame sorted by descending order of the Salary column.
  """
  salary_data_sorted = salary_data.sort_values(by=['Salary'], ascending=False).reset_index()
  del salary_data_sorted['index']
  return salary_data_sorted

def calculate_qualifying_offer(salary_data, number_of_salaries):
  """
  Function that determines the monetary value of the upcoming qualifying offer as the 
  average of the NUM_TOP_PLAYERS (currently 125) highest salaries from the past season.

  Parameters
  ----------
  salary_data : pd.DataFrame
    The sorted Salary Pandas DataFrame.

  number_of_salaries: int
    The number of highest salaries to use when calculating the qualifying offer (passed 
    in as a parameter for code flexibility).

  Returns
  -------
  int
      The calculated qualifying offer.
  """
  top_salaries = salary_data['Salary'][0:number_of_salaries]
  qualifying_offer = top_salaries.mean()
  return qualifying_offer

def plot_histogram_vs_qualifying_offer(axis, salary_data, qualifying_offer, title):
  """
  Function that plots a histogram of the all of the salaries in the provided Salary
  DataFrame, and overlays the monetary value of the qualifying offer on top of this 
  histogram as a comparative visualization.

  Parameters
  ----------
  axis : int
    The subplot location where this generated seaborn subplot will be inserted within the 
    overall plot.

  salary_data: pd.DataFrame
    The Salary Pandas DataFrame that is used to create the relevant statistics for this
    seaborn subplot.

  qualifying_offer: double
    The monetary value of the qualifying offer to be added onto this seaborn subplot.

  title: string
    The displayed title of this seaborn subplot.
  """
  sns.histplot(ax=axis, data = salary_data, x = "Salary", color='b')
  axis.set_title(title)
  axis.axvline(x=qualifying_offer, color='red', ymax = 0.95, 
               label='qualifying offer \n($' + '{:.2e}'.format(qualifying_offer) + ")")
  axis.legend(bbox_to_anchor=(1.0, 1), loc='upper left', fontsize = 7)

def plot_line_graph_vs_qualifying_offer(axis, salary_data, qualifying_offer, title):
  """
  Function that plots a line graph of the all of the salaries in the provided Salary
  DataFrame, and overlays the monetary value of the qualifying offer on top of this 
  line graph as a comparative visualization.

  Parameters
  ----------
  axis : int
    The subplot location where this generated seaborn subplot will be inserted within the 
    overall plot.

  salary_data: pd.DataFrame
    The Salary Pandas DataFrame that is used to create the relevant statistics for this
    seaborn subplot.

  qualifying_offer: double
    The monetary value of the qualifying offer to be added onto this seaborn subplot.

  title: string
    The displayed title of this seaborn subplot.
  """
  sns.lineplot(ax = axis, data=salary_data, x = 'index', y = 'Salary')
  axis.set_xlabel("Player Index (by Descending Order of Salary)")
  axis.set_title(title)
  axis.axhline(y=qualifying_offer, color='red', xmin = 0.05, xmax = 0.95, 
               label='qualifying \noffer \n($' + '{:.2e}'.format(qualifying_offer) + ")")
  axis.legend(bbox_to_anchor=(1.0, 1), loc='upper left', fontsize = 7)

def plot_line_graph_vs_mean_std_qualifying_offer(axis, salary_data, qualifying_offer, title, top):
  """
  Function that plots a line graph of the all of the salaries in the provided Salary
  DataFrame, along with their mean and standard deviation, and overlays the monetary value 
  of the qualifying offer on top of this line graph as a comparative visualization.

  Parameters
  ----------
  axis : int
    The subplot location where this generated seaborn subplot will be inserted within the 
    overall plot.

  salary_data: pd.DataFrame
    The Salary Pandas DataFrame that is used to create the relevant statistics for this
    seaborn subplot.

  qualifying_offer: double
    The monetary value of the qualifying offer to be added onto this seaborn subplot.

  title: string
    The displayed title of this seaborn subplot.
  
  top: boolean
    Either True if salary_data contains only the top NUM_TOP_PLAYERS (currently 125) 
    player salaries, and False otherwise (needed for minor differences in visualization).
  """
  salary_stats = pd.DataFrame({
      'salaries': salary_data['Salary'],
      'mean': [salary_data['Salary'].mean() for i in range(len(salary_data['Salary']))],
      'std': [salary_data['Salary'].std() for i in range(len(salary_data['Salary']))]})
  sns.lineplot(ax = axis, data=salary_stats)
  if top:
    axis.axhline(y=qualifying_offer, color='red', xmin = 0.05, xmax = 0.95, 
                 label='qualifying offer = \nmean \n ($' + '{:.2e}'.format(qualifying_offer) + ")")
    handles, labels = axis.get_legend_handles_labels()
    axis.legend(handles=handles[2:], labels=labels[2:])
  else:
    axis.axhline(y=qualifying_offer, color='red', xmin = 0.05, xmax = 0.95, 
                 label='qualifying \noffer\n ($' + '{:.2e}'.format(qualifying_offer) + ")")
    handles, labels = axis.get_legend_handles_labels()
    axis.legend(handles=handles[1:], labels=labels[1:])
  axis.legend(bbox_to_anchor=(1.0, 1), loc='upper left', fontsize = 7)
  axis.set_title(title)
  axis.set_xlabel("Sorted Player Index")
  axis.set_ylabel("Salary")

def plot_percentiles_vs_qualifying_offer(axis, salary_data, qualifying_offer, title):
  """
  Function that plots a boxplot all of the salaries in the provided Salary
  DataFrame (highlighting the 25, 50, and 75th percentiles), and overlays
  the monetary value of the qualifying offer on top of this boxplot as a comparative 
  visualization.

  Parameters
  ----------
  axis : int
    The subplot location where this generated seaborn subplot will be inserted within the 
    overall plot.

  salary_data: pd.DataFrame
    The Salary Pandas DataFrame that is used to create the relevant statistics for this
    seaborn subplot.

  qualifying_offer: double
    The monetary value of the qualifying offer to be added onto this seaborn subplot.

  title: string
    The displayed title of this seaborn subplot.
  """
  sns.boxplot(ax = axis, x=salary_data["Salary"])
  percentiles = [0, 25, 50, 75, 100]
  colors = ['green', 'black', 'orange', 'magenta', 'yellow']
  quantiles = np.quantile(salary_data["Salary"], np.array([0, 0.25, 0.50, 0.75, 1.00]))
  for index, line in enumerate(quantiles):
    axis.axvline(x=line, ymax = 0.95, color = colors[index], 
                 label= str(percentiles[index]) + 'th percentile \n ($' + '{:.2e}'.format(line) + ")")
  axis.axvline(x=qualifying_offer, color='red', ymax = 0.95, 
               label='qualifying offer \n($' + '{:.2e}'.format(qualifying_offer) + ")")
  axis.legend(bbox_to_anchor=(1.0, 1), loc='upper left', fontsize = 7)
  axis.set_title(title)

def plot_top_ten_salaries_vs_qualifying_offer(axis, salary_data, qualifying_offer, title):
  """
  Function that plots the salaries of the ten highest players from the 2016 MLB season as 
  a histogram, and overlays the monetary value of the qualifying offer on top of this histogram 
  as a comparative visualization.

  Parameters
  ----------
  axis : int
    The subplot location where this generated seaborn subplot will be inserted within the 
    overall plot.

  salary_data: pd.DataFrame
    The Salary Pandas DataFrame that is used to create the relevant statistics for this
    seaborn subplot.

  qualifying_offer: double
    The monetary value of the qualifying offer to be added onto this seaborn subplot.

  title: string
    The displayed title of this seaborn subplot.
  """
  salary_data["Player"]= salary_data["Player"].str.split(",", n=1, expand=True).reset_index()[0]
  sns.barplot(ax = axis, data = salary_data[0:10], x = 'Player', y = 'Salary')
  axis.tick_params(axis='x', rotation=85, labelsize=7)
  axis.set_title(title)
  axis.axhline(y=qualifying_offer, color='red', xmin = 0.05, xmax = 0.95, 
               label='qualifying \noffer \n ($' + '{:.2e}'.format(qualifying_offer) + ")")
  axis.legend(bbox_to_anchor=(1.0, 1), loc='upper left', fontsize = 7)

def main():
  """
  Main function that calculates the value of the upcoming qualifying offer, and displays 
  this information to the user, along with all the other relevant visualizations.

  Visualizations include comparisons of the Salary Dataframe's Histogram, Line Graph, Mean and 
  Standard Deviation against the upcoming qualifying offer, for both the All Salaries and
  the Top 125 Salaries cases. The salaries of the Top 10 highest paid players are also 
  compared against the upcoming qualifying offer.

  The monetary value of the qualifying offer is displayed as a bolded statement above the
  relevant accompanying visualizations.
  """
  salary_data = read_salary_data(HTML_PAGE)
  salary_data['Salary'] = salary_data['Salary'].apply(convert_salary_to_float)
  salary_data_sorted = sort_salary_data(salary_data)
  qualifying_offer = round(calculate_qualifying_offer(salary_data_sorted, NUM_TOP_PLAYERS), 2)

  non_null_salary_data = salary_data_sorted[~salary_data_sorted["Salary"].isna()].reset_index()
  top_salary_data = salary_data_sorted[~salary_data_sorted["Salary"].isna()][0:NUM_TOP_PLAYERS].reset_index()

  fig, axes = plt.subplots(3, 3, figsize=(20, 10))
  plt.subplots_adjust(hspace = 1)
  plt.subplots_adjust(wspace = 1)

  fig.canvas.manager.set_window_title('Question 2 Solution: Qualifying Offer Display')

  fig.suptitle("The value of the Qualifying Offer is a one year contract worth $" + f"{qualifying_offer:,}" + ".",
               fontsize=14, fontweight='bold')

  plot_histogram_vs_qualifying_offer(axes[0][0], non_null_salary_data, qualifying_offer,
                                       "All Salaries Histogram vs\n Qualifying Offer")
  plot_line_graph_vs_qualifying_offer(axes[0][1], non_null_salary_data, qualifying_offer, 
                                        "All Salaries Line Graph vs\n Qualifying Offer")
  plot_line_graph_vs_mean_std_qualifying_offer(axes[0][2], non_null_salary_data, qualifying_offer, 
                                        "All Salaries Line Graph vs\n Mean, Std, and Qualifying Offer",
                                        False)
  plot_percentiles_vs_qualifying_offer(axes[1][0], non_null_salary_data, qualifying_offer, 
                                        "All Salaries Percentile Information vs\n Qualifying Offer")

  plot_histogram_vs_qualifying_offer(axes[1][1], top_salary_data, qualifying_offer,
                                       "Top 125 Salaries Histogram vs\n Qualifying Offer")
  plot_line_graph_vs_qualifying_offer(axes[1][2], top_salary_data, qualifying_offer, 
                                        "Top 125 Salaries Line Graph vs\n Qualifying Offer")
  plot_line_graph_vs_mean_std_qualifying_offer(axes[2][0], top_salary_data, qualifying_offer, 
                                        "Top 125 Salaries Line Graph vs\n Mean, Std and Qualifying Offer",
                                        True)
  plot_percentiles_vs_qualifying_offer(axes[2][1], top_salary_data, qualifying_offer, 
                                        "Top 125 Salaries Percentile Information vs\n Qualifying Offer")
  
  plot_top_ten_salaries_vs_qualifying_offer(axes[2][2], non_null_salary_data, qualifying_offer,
                                          "Top 10 Highest Salaried Players vs\n Qualifying Offer")

  manager = plt.get_current_fig_manager()
  manager.full_screen_toggle()

  plt.show()

main()
