#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(ggplot2)
library(plotly)
library(dplyr)
library(reshape2)

cfpb <- read.csv("panel1.csv") #read.csv("data2.csv")
cfpb$Year <- factor(cfpb$Year)
cfpb[cfpb == 0] <- NA

mbData <- read.csv("panel2.csv")
mbData$Year <- factor(mbData$Year)

mbData_melt <- melt(mbData, id = c("State", "Year", "Company"))
mbData_melt <- mbData_melt[!(mbData_melt$variable == "Total"),]

# Define UI for application that displays plots
ui <- fluidPage(
  
  tabsetPanel(
    
    tabPanel("Complaint Counts", "CFPB Database: Data was downloaded on May 7, 2020", 
             
             titlePanel( "Complaint Counts"),
             
             # Sidebar with a drop down select for Complaint type, Year and Month
             sidebarLayout(
               sidebarPanel(
                 varSelectInput("complaint",
                                "Complaint Type:",
                                cfpb[, 4:13],
                                selected = "Total",
                                multiple = FALSE),
                 
                 checkboxGroupInput("year",
                                    "Select Year(s):",
                                    choices = levels(cfpb$Year),
                                    selected = levels(cfpb$Year)),
                 
                 checkboxGroupInput("month",
                                    "Select Month(s)",
                                    choices = c("January" = 1, "February" = 2, "March" = 3, "April" = 4, "May" = 5, "June" = 6,
                                                "July" = 7, "August" = 8, "September" = 9, "October" = 10, 
                                                "November" = 11, "December" = 12),
                                    selected = c("January" = 1, "February" = 2, "March" = 3, "April" = 4, "May" = 5, "June" = 6,
                                                 "July" = 7, "August" = 8, "September" = 9, "October" = 10, 
                                                 "November" = 11, "December" = 12)),
                 
                 selectInput("company",
                             "Select Company: (Only top 10 most frequent complaints)",
                             choices = levels(cfpb$Company),
                             selected = "All",
                             multiple = FALSE)
               ), #ends side bar panel 
               
               # Show plots 
               mainPanel(
                 textOutput("first"),
                 plotOutput("linePlot"),
                 plotOutput("barPlot")
               )#end main Panel
             )#end side bar
    ), #ends first panel
    
    tabPanel("Map", "Note: Some combinations of Year and Company will return null values as there were no complaints for that given Company during that given Year",
             titlePanel("Map"),
             
             sidebarLayout(
               sidebarPanel(
                 varSelectizeInput("complaints",
                                   "Complaint Type: (Only affects Map)",
                                   mbData[, 4:13],
                                   selected = "Total",
                                   multiple = FALSE),
               
                 selectizeInput("years",
                               "Select Year:",
                               levels(mbData$Year),
                               selected = "All",
                               multiple = FALSE),
                 
                 selectizeInput("state",
                                "Select a State: (Only affects Bar Chart)",
                                levels(mbData$State),
                                selected = "CA",
                                multiple = FALSE),
                 
                 selectizeInput("comp",
                                "Select a Company: (Only top 10 most frequent complaints)",
                                levels(mbData$Company),
                                selected = "All",
                                multiple = FALSE)
                 
               ),
               
               mainPanel(
                 textOutput("year"),
                 plotlyOutput("mapPlot"),
                 textOutput("state"),
                 plotlyOutput("statePlot")
               ) #ends mainpanel
             ) #ends side bar layout
    )#ends second panel
    
  )#ends tab panel
) #ends UI

# Define server logic required to draw a histogram
server <- function(input, output, session) {
  
  output$linePlot <- renderPlot({
    ggplot(data = subset(cfpb, cfpb$Year %in% input$year & cfpb$Month %in% input$month & cfpb$Company == input$company), 
           aes_string(x = "Month", y = input$complaint, group = "Year", color = "Year")) +   
      geom_line() +
      geom_point() +
      theme_light() +
      scale_x_discrete(limits = month.abb) +
      labs(title = 'Count of Complaint Type vs Month',
           y = 'Total Count of Complaints',
           color = 'Year')
    
  }) #ends line plot 
  
  output$barPlot <- renderPlot({
    
    ggplot(data = subset(cfpb, cfpb$Year %in% input$year & cfpb$Month %in% input$month & cfpb$Company == input$company), 
           aes_string(x = "Month", y = input$complaint, group = "Year", fill = "Year")) +  
      geom_col(position = "dodge") +
      scale_x_discrete(limits = month.abb) +
      theme_light() +
      labs(title = 'Count of Complaint Type vs Month',
           y = 'Total Count of Complaints',
           fill = 'Year')
    
  }) #ends bar plot
  
  output$mapPlot <- renderPlotly({
    
    mbData_ss = subset(mbData, mbData$Year == input$years & mbData$Company == input$comp)
    g <- list(
      scope = 'usa',
      projection = list(type = 'albers usa'),
      showlakes = TRUE,
      lakecolor = toRGB('white')
    )
    
    #fig <- plot_geo(mapData, locationmode = 'USA-states')
    fig <- plot_geo(mbData_ss, locationmode = 'USA-states')
    fig <- fig %>% add_trace(
      z = mbData_ss[[input$complaints]], locations = ~State,
      color = mbData_ss[[input$complaints]], colors = 'Spectral'
    )
    fig <- fig %>% colorbar(title = "Number of complaints")
    fig <- fig %>% layout(
      title = 'Number of Complaints by State',
      geo = g
    )
    
    fig
    
  }) #ends mapPlot
  
  output$statePlot <- renderPlotly({
    
    melt_ss = subset(mbData_melt, mbData_melt$Year == input$years & mbData_melt$State == input$state & mbData$Company == input$comp)
    melt_ss$variable = factor(melt_ss$variable, levels = unique(melt_ss$variable)[order(melt_ss$value, decreasing = TRUE)])
    
    fig <- plot_ly(data = melt_ss, x = ~value, y = ~variable, text = ~value, textposition = 'outside',
                   type = 'bar', orientation = 'h', color = ~variable, colors = 'Set3')
    fig <- fig %>% layout(title = "Count of Complaints for State for Year", xaxis = list(title = "Count of Complaints", gridcolor = '#808080'), 
                          yaxis = list(title = ""), showlegend = FALSE, plot_bgcolor = '#000000')
    
    fig 
  })
  
  output$first <- renderText({
    paste("Showing data for Complaint Type:", input$complaint, "and Company:", input$company)
  })
  
  output$year <- renderText({
    paste("Showing data from year(s):", input$years, "and Complaint Type:", input$complaints)
  })
  
  output$state <- renderText({
    paste("Showing data for the State:", input$state, "and year(s):", input$years)
  })
} #ends server

# Run the application 
shinyApp(ui = ui, server = server)
