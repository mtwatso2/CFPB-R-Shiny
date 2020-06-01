#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(

  tabPanel("LDA", "CFPB Database: Only used 5,000 rows for LDA",
           helpText(a("Click here to see other visualizations created from the CFPB Database", href = "https://mwatson717.shinyapps.io/CFPB/")),
           
           titlePanel("LDA Visualization"),
           # create the json object, start a local file server, open in default browser
           mainPanel(
             includeHTML("LDA2.html") 
           ) #ends main panel
  ), #ends tab panel

  #wellPanel(
   # helpText( a("Click Here to see other part of the project", href = "https://mwatson717.shinyapps.io/CFPB/"))
  #)
    
)

# Define server logic required to draw a histogram
server <- function(input, output) {
}

# Run the application 
shinyApp(ui = ui, server = server)
