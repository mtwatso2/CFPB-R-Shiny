# CFPB-R-Shiny
R Shiny applications using data from the Consumer Financial Protection Bureau 

You can download the data here: https://www.consumerfinance.gov/data-research/consumer-complaints/

Links to shinyapps.io webpages: https://mwatson717.shinyapps.io/CFPB/ ,
                                https://mwatson717.shinyapps.io/CFPB_LDA/

# Contents:

* CFPB_328.pbix: Power BI Report containing CFPB data through 3-28-2023

* app.R: R Shiny application containing both UI and Server

* cfpbPBI.py: Python script used to create data for CPFB_328.pbix

* data_preprocessing.py: Python file used for data preprocessing

* map2-12-21-22.csv: Data used for the second map on second panel, contains output of LDA as column 'LDA_Topic' (Data Downloaded on December 21, 2022)

* panel1-12-21-22.csv: Data used for the first panel, creating ggplot line and bar charts (Data Downloaded on December 21, 2022)

* panel1.csv: Data used for the first panel of the PBI report (Data downloaded on March 28, 2023)

* panel2-12-21-22.csv: Data used for the second panel, creating a Plotly Map and bar chart (Data Downloaded on December 21, 2022)

* panel2.csv: Data used for the second panel of the PBI report (Data downloaded on March 28, 2023)

* panel3.csv: Data used for the thrid panel of the PBI report (Data downloaded on March 28, 2023)


## LDA Folder:

* app.R: R shiny application dispalying output of LDA model through the LDAviz package

* LDA2.html: output of LDAviz
 
