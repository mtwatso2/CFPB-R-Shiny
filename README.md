# CFPB-R-Shiny
R Shiny application using data from the Consumer Financial Protection Bureau 

Links to shinyapps.io webpages: https://mwatson717.shinyapps.io/CFPB/
                                https://mwatson717.shinyapps.io/CFPB_LDA/

Contents:

app.R: R Shiny application containing both UI and Server

panel1.csv: Data used for the first panel, creating ggplot line and bar charts

panel2.csv: Data used for the second panel, creating a Plotly Map and bar chart

map2.csv: Data used for the second map on second panel, contains output of LDA as column 'LDA_Topic'

LDA Folder:

app.R: R shiny application dispalying output of LDA model through the LDAviz package

LDA2.html: output of LDAviz
