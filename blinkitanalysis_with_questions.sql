-- What is the total sales, average sales, number of items, and average rating for each item fat content category?
select Item_Fat_Content,
round(sum(Sales),2) as total_sales ,
round(avg(Sales),2) as average_sales,
count(*) as no_of_items,
round(avg(Rating),2)  as average_rating
from blinkitdb.blinkit_data
group by 1
order by 2 desc;

-- What is the total sales, average sales, number of items, and average rating for each item type?
select Item_Type,
round(sum(Sales),2) as total_sales ,
round(avg(Sales),2) as average_sales,
count(*) as no_of_items,
round(avg(Rating),2)  as average_rating
from blinkitdb.blinkit_data
group by 1
order by 2 desc;

-- How do low fat and regular item sales compare across different outlet location types?
SELECT 
  Outlet_Location_Type,
  ROUND(SUM(CASE WHEN Item_Fat_Content = 'Low Fat' THEN Sales ELSE 0 END), 2) AS Low_Fat,
  ROUND(SUM(CASE WHEN Item_Fat_Content = 'Regular' THEN Sales ELSE 0 END), 2) AS Regular
FROM 
  blinkitdb.blinkit_data
GROUP BY 
  Outlet_Location_Type
ORDER BY 
  Outlet_Location_Type;

-- What is the total sales and percentage of sales for each outlet size?
select Outlet_Size,
round(sum(Sales),2) as Total_Sales,
cast((sum(Sales)*100.0/sum(sum(sales)) over()) as decimal (10,2)) as percentage_sales
FROM 
  blinkitdb.blinkit_data
  group by 1
  order by 2 desc;
  
-- What is the total sales and percentage of sales for each outlet location type?
  select Outlet_Location_Type,
round(sum(Sales),2) as Total_Sales,
cast((sum(Sales)*100.0/sum(sum(sales)) over()) as decimal (10,2)) as percentage_sales
FROM 
  blinkitdb.blinkit_data
  group by 1
  order by 2 desc;
  
-- What is the total sales, average sales, number of items, and average rating for each outlet type?
  select Outlet_Type,
round(sum(Sales),2) as total_sales ,
round(avg(Sales),2) as average_sales,
count(*) as no_of_items,
round(avg(Rating),2)  as average_rating
from blinkitdb.blinkit_data
group by 1
order by 2 desc

