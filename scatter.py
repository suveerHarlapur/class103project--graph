import pandas as pd
import plotly.express as px
df = pd.read_csv("coviddata.csv")
graph = px.scatter(df,x="date",y="cases",color="country",size="cases",size_max=30)
graph.show()