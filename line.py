import pandas as pd
import plotly.express as px

df = pd.read_csv("coviddata.csv")
graph = px.line(df,x="date",y="cases",color="country",title="Covid Data Line Graph")
graph.show()