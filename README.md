# CFPB-R-Shiny
R Shiny applications using data from the Consumer Financial Protection Bureau 

You can download the data here: https://www.consumerfinance.gov/data-research/consumer-complaints/

Links to shinyapps.io webpages: https://mwatson717.shinyapps.io/CFPB/ ,
                                https://mwatson717.shinyapps.io/CFPB_LDA/

# Contents:

* app.R: R Shiny application containing both UI and Server

* panel1-9-28.csv: Data used for the first panel, creating ggplot line and bar charts (Data Downloaded on September 28th)

* panel2.csv: Data used for the second panel, creating a Plotly Map and bar chart (Data Downloaded on September 28th)

* map2.csv: Data used for the second map on second panel, contains output of LDA as column 'LDA_Topic' (Data Downloaded on September 28th)

* data_preprocessing.py: Python file used for data preprocessing

## LDA Folder:

* app.R: R shiny application dispalying output of LDA model through the LDAviz package

* LDA2.html: output of LDAviz
