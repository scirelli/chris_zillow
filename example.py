#!/usr/bin/env python3
import os

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
