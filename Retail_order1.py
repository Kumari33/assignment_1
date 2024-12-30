import streamlit as st 
import pandas as pd
import psycopg2

import matplotlib.pyplot as plt
import numpy as np
 
from sqlalchemy import create_engine

#Get connection setup using SQLAlchemy

conn=psycopg2.connect(
host="localhost",
port="5432",
user="postgres",
password="kuma",
database="first",
)

#create Engine
host="localhost",
port="5432",
user="postgres",
password="kuma",
database="first"

engine = create_engine(f"postgresql://{user}:{password}@{host}/{database}")

print(engine) 


mediator=conn.cursor()
#mediator.execute('select * from df,df1,df2')
#data=mediator.fetchall()    
    

st.set_page_config(page_title="Retail Order Management", 
    page_icon="🛒" 
)
st.title("Welcome to the Retail Order Management System")

st.markdown("""
    Welcome to the Retail Order Management System, where you can manage and analyze your retail orders efficiently. 
    """)
#st.write("Retail Order Analysis")


st.sidebar.title("Home")



a=st.selectbox ("Question",["1.Find top 10 highest revenue generating products",
                            "2.Find the top 5 cities with the highest profit margins",
                            "3.Calculate the total discount given for each category",
                            "4.Find the average sale price per product category",
                            "5.Find the region with the highest average sale price",
                            "6.Find the total profit per category",
                            "7.Identify the top 3 segments with the highest quantity of orders",
                            "8.Determine the average discount percentage given per region",
                            "9.Find the product category with the highest total profit",
                            "10.Calculate the total revenue generated per year",
                            "11.Find the total revenue generated by each segment",
                            "12.Find the total profit generated for each region",
                            "13.Matching orders and product details",
                            "14.All Orders with or without Product Details",
                            "15.Find the total discount given for each category",
                            "16.Select total sales price and profit per product category",
                            "17.Count Orders by Segment",
                            "18.Calculate average discount per state",
                            "19.Select top 10 most profitable products",
                            "20.Select the total quantity sold per product"
                            ])
#st.write(a)
if st.button('Generate Reports'):
    st.write("Reports will be generated soon...")


    if a=="1.Find top 10 highest revenue generating products":
        
        mediator.execute("select product_name, sum(quantity*sales_price) as total_revenue from df group by product_name order by total_revenue desc limit 10")
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['product_name','total_revenue'])
        st.dataframe(df)
    elif a=="2.Find the top 5 cities with the highest profit margins":
        mediator.execute("select city, (sum(quantity * sales_price) - sum(cost_price)) as profit_margin from df group by city order by profit_margin desc limit 5")
        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['city','profit_margin'])
        st.dataframe(df)
        
    elif a=="3.Calculate the total discount given for each category":
        mediator.execute("select category, sum(discount) as total_discount from df group by category")

        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['category','total_discount'])
        st.dataframe(df)

    elif a=="4.Find the average sale price per product category":
        mediator.execute("select category, avg(sales_price) as avg_sales_price from df group by category")

        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['category','avg_sales_price'])
        st.dataframe(df)
    elif a=="5.Find the region with the highest average sale price":
        mediator.execute("select region, avg(sales_price) as avg_sales_price from df group by region order by avg_sales_price desc limit 1")

        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['region','avg_sales_price'])
        st.dataframe(df)

    elif a=="6.Find the total profit per category":
        mediator.execute("select category, sum(profit) as total_profit from df group by category")

        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['category','total_profit'])
        st.dataframe(df)  

    elif a=="7.Identify the top 3 segments with the highest quantity of orders":
        mediator.execute("select segment, sum(quantity) as total_quantity from df group by segment order by total_quantity desc limit 3")

        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['segment','total_quantity'])
        st.dataframe(df)  

    elif a=="8.Determine the average discount percentage given per region":
        mediator.execute(" select region, avg(discount_percent) as avg_discount_percent from df group by region")

        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['region','avg_discount_percent'])
        st.dataframe(df)

    elif a=="9.Find the product category with the highest total profit":
        mediator.execute(" select category as product_category, sum(profit) as total_profit from df group by category order by total_profit desc limit 1")

        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['product_cat','total_profitnt'])
        st.dataframe(df)

    elif a=="10.Calculate the total revenue generated per year":
        mediator.execute(" select extract (year from order_date) as year, sum(quantity*sales_price) as total_revenue from df group by year")

        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['year','total_revenue'])
        st.dataframe(df)

    elif a=="11.Find the total revenue generated by each segment":
        mediator.execute(" select df1.segment, sum(df2.sales_price) as totalr_revenue from df1 join df2 on df1.product_id = df2.product_id group by df1.segment")

        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['df1.segment','totalr_revenue'])
        st.dataframe(df)  

    elif a=="12.Find the total profit generated for each region":
        mediator.execute(" select df1.region, sum(df2.profit) as total_profit from df1 join df2 on df1.product_id = df2.product_id group by df1.region")

        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['df1.region','df2.total_profitnt'])
        st.dataframe(df)

    elif a=="13.Matching orders and product details":
        mediator.execute(" select df1.order_id, df1.order_date, df1.ship_mode, df1.product_name, df2.cost_price, df2.list_price from df1 inner join df2 on df1.product_id = df2.product_id")
        data=mediator.fetchall()
        df= pd.DataFrame(np.random.randn(20,6), columns=['df1.order_id', 'df1.order_date', 'df1.ship_mode', 'df1.product_name', 'df2.cost_price', 'df2.list_price'])
        st.bar_chart(df)
    
        #data=mediator.fetchall() 
        #df=pd.DataFrame(data,columns=['df1.order_id', 'df1.order_date', 'df1.ship_mode', 'df1.product_name', 'df2.cost_price', 'df2.list_price'])
        #st.dataframe(df)

    elif a=="14.All Orders with or without Product Details":
        mediator.execute(" select df1.order_id, df1.order_date, df1.product_name, df2.sales_price from df1 left join df2 on df1.product_id = df2.product_id")

        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['df1.order_id', 'df1.order_date', 'df1.product_name', 'df2.sales_price'])
        st.dataframe(df)

    elif a=="15.Find the total discount given for each category":
        mediator.execute("select df1.category, sum(df2.discount) as total_discount from df1 join df2 on df1.product_id=df2.product_id group by df1.category ")
        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['df1.category', 'total_discount'])
        st.dataframe(df)

    elif a=="16.Select total sales price and profit per product category":
        mediator.execute("select df1.category, sum(df2.sales_price) as total_sales, sum(df2.profit) as total_profit from df1 join df2 on df1.product_id = df2.product_id group by df1.category ")
        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['df1.category', 'total_sales', 'total_profit'])
        st.dataframe(df)

    elif a=="17.Count Orders by Segment":
        mediator.execute("select df1.segment, count(df1.order_id) as order_count from df1 inner join df2 on df1.product_id = df2.product_id group by df1.segment ")
        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['df1.segment', 'order_count'])
        st.dataframe(df)

    elif a=="18.Calculate average discount per state":
        mediator.execute("select df1.state, avg (df2.discount) as avg_discount from df1 join df2 on df1.product_id=df2.product_id group by df1.state ")
        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['df1.state', 'avg_discount'])
        st.dataframe(df)

    elif a=="19.Select top 10 most profitable products":
        mediator.execute("select df1.product_name, sum(df2.quantity * df2.sales_price) as total_revenue from df1 join df2 on df1.product_id=df2.product_id group by df1.product_name order by total_revenue desc limit 10 ")
        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['df1.product_name', 'df2.profit'])
        st.dataframe(df)

    elif a=="20.Select the total quantity sold per product":
        mediator.execute("select df1.product_name, sum(df2.quantity) as total_quantity from df1 join df2 on df1.product_id=df2.product_id group by df1.product_name ")
        
        data=mediator.fetchall() 
        df=pd.DataFrame(data,columns=['df1.product_name', 'total_quantity'])
        st.dataframe(df)                      

