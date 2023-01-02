#import libraries
import requests
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
import pandas as pd
from collections import defaultdict
warnings.filterwarnings("ignore")


def create_dataset (indicator:str):

   '''INPUT:
   indicator: string corresponding to the indicator that will be embedded to the API link 

    
   OUTPUT:
   df: dataframe created from json file in the format: country , year , value '''


   get_req_param = {'format': 'json', 'per_page': '5000', 'date':'2000:2020'}
   json_data = requests.get('http://api.worldbank.org/v2/countries/fin;dnk;che;ca;us/indicators/'+ str(indicator), params=get_req_param)
     
     
   indicator_dict = defaultdict(list)

   for e in json_data.json()[1]:
     # check if country is already in dictionary. If so, append the new x and y values to the lists
      if indicator_dict[e['country']['value']]:
         indicator_dict[e['country']['value']][0].append(int(e['date']))
         indicator_dict[e['country']['value']][1].append(float(e['value']))       
      else: # if country not in dictionary, then initialize the lists that will hold the x and y values
         indicator_dict[e['country']['value']] = [[],[]] 


   states_list = []
   year_list = []
   values_list = []

   for i in indicator_dict.keys(): #Loop through dictionary keys
      for (j,k) in  zip(indicator_dict[i][0] , indicator_dict[i][1]) : #Loop through each of the lists for a given key
            states_list.append(i)
            year_list.append(j)
            values_list.append(k)
      
   df = pd.DataFrame(list(zip(states_list ,year_list , values_list )) , columns = ['Country' , 'Year' , 'Value'])

     
   return df
    
    
#Create a dataset for mortality caused by road traffic - indicator 'SH.STA.TRAF.P5'
df_mortality_road_traffic = create_dataset('SH.STA.TRAF.P5').rename(columns = {'Value':'Road Traffic Mortality'})
#Create a dataset for unemployed population - indicator SL.UEM.TOTL.ZS
df_unemployed = create_dataset('SL.UEM.TOTL.ZS').rename(columns = {'Value':'Unemployment %'})
#Create a dataset for inflation - indicator FP.CPI.TOTL.ZG
df_inflation = create_dataset('FP.CPI.TOTL.ZG').rename(columns = {'Value':'Inflation %'})

#Create datasets for women and men than work in agriculture - women indicator SL.AGR.EMPL.FE.ZS men indicator SL.AGR.EMPL.MA.ZS
df_agriculture_women = create_dataset('SL.AGR.EMPL.FE.ZS').rename(columns = {'Value':'Employment in Agriculture in the past 20 years'})
df_agriculture_men  = create_dataset('SL.AGR.EMPL.MA.ZS').rename(columns = {'Value':'Employment in Agriculture in the past 20 years'})




#Group by Country dataset pertaining to men
df_male_emp_agr_grouped  = df_agriculture_men.groupby(['Country']).sum()['Employment in Agriculture in the past 20 years'].to_frame().reset_index()
df_male_emp_agr_grouped['Gender'] = 'Men'

#Group by Country dataset pertaining to women 
df_female_emp_agr_grouped  = df_agriculture_women.groupby(['Country']).sum()['Employment in Agriculture in the past 20 years'].to_frame().reset_index()
df_female_emp_agr_grouped['Gender'] = 'Women'

#Create a single dataset by appending
df_agriculture = df_female_emp_agr_grouped.append(df_male_emp_agr_grouped)
#Round the value to 3 decimals
df_agriculture['Employment in Agriculture in the past 20 years'] = round(df_agriculture['Employment in Agriculture in the past 20 years'],3)  
#Convert the value to percentage
df_agriculture['Percentage'] = round(df_agriculture.groupby(["Country"])['Employment in Agriculture in the past 20 years'].transform(lambda x:x/x.sum()) * 100 , 1 ) 
#Create a new column for percentage value so that it contains the '%' sign as well
df_agriculture['Percentage_'] = df_agriculture['Percentage'].astype(float).map('{:.1f}%'.format)
#Order by Gender for visualization purposes
df_agriculture.sort_values(by="Gender" , ascending = True , inplace = True)



#Create a list for graph 1
graph_one = []
#Create a line chart
graph_one = px.line(df_unemployed, x="Year", y="Unemployment %", color='Country' ,  title = "Unemployment (% total of labor force)")
#Update the title of chart while positioning it
graph_one.update_layout(title_text='Unemployment (% total of labor force)', title_x=0.3)


#Create a list for graph 2
graph_two= []
graph_two = px.bar(df_agriculture, x="Country", y="Percentage",color='Gender', barmode='group', text= "Percentage"  , height=400)
#Update the title of chart while positioning it
graph_two.update_layout(title_text='Women vs Men employment in agriculture (2000 - 2022)', title_x=0.45)


#Create a list for graph 3
graph_three= []
#Create a line chart
graph_three = px.line(df_inflation, x="Year", y="Inflation %", color='Country' ,  title = "Inflation, consumer prices (annual %)")
#Update the title of chart while positioning it
graph_three.update_layout(title_text='Inflation, consumer prices (annual %)', title_x=0.45)


#Create a list for graph 4
graph_four = []
#Create a line chart
graph_four = px.line(df_mortality_road_traffic, x="Year", y="Road Traffic Mortality", color='Country' )
#Update the title of chart while positioning it
graph_four.update_layout(title_text= "Mortality caused by road traffic injury (per 100,000) years 2000 - 2020 people" , title_x=0.45)


#Create a function which will be used in other files for retrieving graphs and their layouts
def return_figures():
    figures = []
    figures.append(dict(data = graph_one ))
    figures.append(dict(data = graph_two ))
    figures.append(dict(data = graph_three ))
    figures.append(dict(data = graph_four ))
    return figures



