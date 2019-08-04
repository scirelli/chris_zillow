#!/usr/bin/env python3
import os

import mysql.connector
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

address = '8501 Katy Reid Ct.'
zipcode = '23832'

zillow_data = ZillowWrapper(os.environ.get('ZILLOW_API_KEY', ''))
deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
result = GetDeepSearchResults(deep_search_response)
for prop in ['zillow_id', 'home_type', 'home_detail_link', 'graph_data_link', 'map_this_home_link', 'latitude', 'longitude', 'tax_year', 'tax_value', 'year_built', 'property_size', 'home_size', 'bathrooms', 'bedrooms', 'last_sold_date',
             'last_sold_price_currency', 'last_sold_price', 'zestimate_amount', 'zestimate_last_updated', 'zestimate_value_change',
             'zestimate_valuation_range_high', 'zestimate_valuationRange_low', 'zestimate_percentile']:
    value = getattr(result, prop)
    print(f'{prop} = {value}')

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd=os.environ.get('MYSQL_PASSWORD', ''),
    database='chris_zillow_example')

try:
    mycursor = mydb.cursor()
    sql_command = '''
                INSERT INTO zillow_results (zillow_id, home_type, tax_year, tax_value, year_built, property_size, bathroom)
                VALUES(%s, %s, %s, %s, %s, %s, %s)'''

    values = (result.zillow_id, result.home_type, result.tax_year, result.tax_value, result.year_built, result.property_size, result.bathrooms)
    mycursor.execute(sql_command, values)
    mydb.commit()
except mysql.connector.errors.ProgrammingError as err:
    print('sql insert addresses function generated an error => {}'.format(err))

except mysql.connector.errors.IntegrityError as err:
    print('sql insert addresses function generated an error => {}'.format(err))
