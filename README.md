# intro to streamlit ways of being

## goal

just have an overview on how streamlit works 

## streamlit

streamlit is just a library for building simple websites, and a free hosting service


### basis

* streamlit runs from a python file, named whatever
* allows for multiple pages, and page layouts
* important features:
    * every single expression line is printed
        * that is, it is rendered by streamlit in the webpage
        * alternatively, one can use `st.write(...)` or a specific function to render a specific type of object
    * streamlit is reactive
        * it will re-run the script every time a change is made
        * this entails some things to consider: 
            * we should not load data or models inside the script, as it will be re-run every time
            * we should not have side-effects, as they will be re-run every time
            * we should not have uncached expensive functions, as they will be re-run every time
    * each streamlit's session keeps a state
        * every widget/component has a value (state), which when changed may have implications on the rest of the script
    * streamlit has a cache
        * we can hold a function from being re-run, if we know it will not change
        * this is useful for expensive functions, such as loading data or ML models
    * streamlit has a sidebar
        * we can put widgets in the sidebar, which will not be re-run
        * this is useful for widgets that do not change, such as a title or a logo

### widgets (aka components)

* text
* images
* tables (dataframes)
* charts
* buttons, checkboxes, radio buttons
* sliders
* text inputs, file uploads
* etc

### layout

* we can use columns and rows to layout the widgets
* we can use containers to group widgets
* we can use expanders to hide widgets

