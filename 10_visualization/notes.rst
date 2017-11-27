**Reading**

- https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py 
- https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python 
 
**Key Concepts**

- What is data visualization?
- Data visualization in Python
- Basic matplotlib syntax
- Creating line, scatter, bar, & pie charts 
- Saving plots

**Data Visualization**

Presenting data visually often helps people to see and understand patterns in their data. Visualization can range from simple plots or charts to very complex plots of large datasets with mutiple dimensions.

Python offers several very powerful tools for data visualization and is widely used in the sciences and business for data analysis. Increasingly, knowing how to present data visually is a key technical skill.


**Visualization in Python**

matplotlib is a key python module that supports a wide range of data plots & charts. It's packaged with the standard python and includes several key sub-libraries. pyplot is one sub-library commonly used for plotting data. 

pyplot accepts Python lists or tuples with integer or float values, and can calculate default axis ranges and tick marks.  

A basic pyplot example:
::

    # Import the necessary packages and modules
    import matplotlib.pyplot as plt
    
    x = range(5) # values for x-axis
    y = [3,12,7,9,18] # values for y-axis
    
    # create sub-plot showing the data as a line
    plt.plot(x, y, label='my data')
    
    # Add a legend
    plt.legend()
    
    # Show the plot
    plt.show()

The data above could also be displayed as a scatter plot like so:
::

    plt.scatter(x,y, label='my data')

or as a bar chart or horizontal bar chart:
::

    plt.bar(x,y, label='my data') # show vertical bars
    plt.barh(x,y, label='my data') # show horizontal bars

A plot can include several sub-plots of the same or different types:
::

    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
    plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26])
    plt.show() 

* https://matplotlib.org/examples/api/barchart_demo.html
 
**Plot Text**

pyplot offers wide control over features of a plot, including title, axis labels, and tickmark labels. 
::

    sp = plt.subplot() # need a sub-plot object to customize text 
    # add custom text for labels, plot title and axes ticks
    sp.set_ylabel('Scores')
    sp.set_title('Scores by group')
    # include label for tick at intersection of x & y axis
    sp.set_xticklabels(('','G1', 'G2', 'G3', 'G4')) 

**Pie Charts**

pyplot can display data as a pie chart to show proportions:
::

    import matplotlib.pyplot as plt
    
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show (Links to an external site.)Links to an external site.()

**Saving Plots**

You can easily save plots to a  graphic file:
::

    plt.savefig("mydata.png")

or to a PDF file:
::

    from matplotlib.backends.backend_pdf import PdfPages 
    pp = PdfPages('mydata.pdf') # Initialize the pdf file 
    pp.savefig()