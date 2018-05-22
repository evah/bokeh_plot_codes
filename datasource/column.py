# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource from df: source
source = ColumnDataSource(df)

# Add circle glyphs to the figure p
p=figure(x_axis_label='Year',y_axis_label='Time')
p.circle(x='Year',y='Time',color='color',size=8,source=source)

# Specify the name of the output file and show the result
output_file('sprint.html')
show(p)
