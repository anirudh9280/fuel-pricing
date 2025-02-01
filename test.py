# from apify_client import ApifyClient
# from sample_data import json_data

# # Initialize the ApifyClient with your API token
# client = ApifyClient("apify_api_6UFFKtdX6Gt5RXDzVCGX2EuNCdoEMJ4j8mFB")

# # Prepare the Actor input
# run_input = {
#     "location": "Los Angeles",
#     "maxCrawledPlacesPerSearch": 5,
# }

# run = client.actor("SRhw0dF53pcnChdvL").call(run_input=run_input)

# for item in client.dataset(run["defaultDatasetId"]).iterate_items():
#     print(item)

import pandas as pd
import json

def load_data_as_dataframe():
    json_data = """
    [
        {
            "title": "Chevron",
            "address": "16801 Ventura Blvd, Encino, CA 91436",
            "gasPrices": [
                {
                    "priceTag": "$4.90",
                    "updatedAt": "2025-01-16T05:50:06.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.9,
                    "gasType": "Regular"
                },
                {
                    "priceTag": "$5.00",
                    "updatedAt": "2025-01-15T16:07:00.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 5,
                    "gasType": "Midgrade"
                },
                {
                    "priceTag": "$5.30",
                    "updatedAt": "2025-01-16T05:35:12.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 5.3,
                    "gasType": "Premium"
                },
                {
                    "priceTag": "$5.80",
                    "updatedAt": "2025-01-16T05:35:12.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 5.8,
                    "gasType": "Diesel"
                }
            ],
            "website": "https://www.chevron.com/",
            "phone": "(818) 990-9464",
            "totalScore": 3.5,
            "rank": 5,
            "reviewsCount": 15,
            "isAdvertisement": false,
            "categoryName": "Gas station",
            "searchString": "gas station",
            "url": "https://www.google.com/maps/search/?api=1&query=Chevron&query_place_id=ChIJEXeSOzCYwoARRvtjAivyoyk"
        },
        {
            "title": "Mobil",
            "address": "17661 Ventura Blvd, Encino, CA 91316, United States",
            "gasPrices": [
                {
                    "priceTag": "US$4.60",
                    "updatedAt": "2025-01-15T16:04:00.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.6,
                    "gasType": "Regular"
                },
                {
                    "priceTag": "US$4.80",
                    "updatedAt": "2025-01-15T16:04:00.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.8,
                    "gasType": "Midgrade"
                },
                {
                    "priceTag": "US$5.10",
                    "updatedAt": "2025-01-16T06:09:59.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 5.1,
                    "gasType": "Premium"
                }
            ],
            "website": "https://www.exxon.com/en/find-station/mobil-encino-ca-masisenterprisesinc-200317003?utm_medium=referral&utm_source=yxt-google&utm_campaign=us_fue_ret_xom_yxt",
            "phone": "+1 818-788-3626",
            "totalScore": 3.9,
            "rank": 4,
            "reviewsCount": 111,
            "isAdvertisement": false,
            "categoryName": "Gas station",
            "searchString": "gas station",
            "url": "https://www.google.com/maps/search/?api=1&query=Mobil&query_place_id=ChIJiTfY0UyYwoARxts3wUrLnZA"
        },
        {
            "title": "United Oil",
            "address": "19706 Ventura Blvd, Woodland Hills, CA 91364",
            "gasPrices": [
                {
                    "priceTag": "$4.20",
                    "updatedAt": "2025-01-16T05:15:38.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.2,
                    "gasType": "Regular"
                },
                {
                    "priceTag": "$4.30",
                    "updatedAt": "2025-01-09T11:24:00.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.3,
                    "gasType": "Midgrade"
                },
                {
                    "priceTag": "$4.60",
                    "updatedAt": "2025-01-16T07:35:04.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.6,
                    "gasType": "Premium"
                }
            ],
            "website": "https://rocketstores.com/",
            "phone": "(818) 609-9323",
            "totalScore": 4.3,
            "rank": 3,
            "reviewsCount": 215,
            "isAdvertisement": false,
            "categoryName": "Gas station",
            "searchString": "gas station",
            "url": "https://www.google.com/maps/search/?api=1&query=United%20Oil&query_place_id=ChIJ6YxDVEeZwoARNQadXeqSoJ8"
        },
        {
            "title": "Shell",
            "address": "17660 Burbank Blvd, Encino, CA 91316",
            "gasPrices": [
                {
                    "priceTag": "$4.28",
                    "updatedAt": "2025-01-16T08:43:28.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.28,
                    "gasType": "Regular"
                },
                {
                    "priceTag": "$4.48",
                    "updatedAt": "2025-01-16T05:15:00.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.48,
                    "gasType": "Midgrade"
                },
                {
                    "priceTag": "$4.68",
                    "updatedAt": "2025-01-16T11:42:02.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.68,
                    "gasType": "Premium"
                },
                {
                    "priceTag": "$4.88",
                    "updatedAt": "2025-01-15T09:43:00.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.88,
                    "gasType": "Diesel"
                }
            ],
            "website": "https://find.shell.com/us/fuel/10007891-17660-burbank-blvd/en_US",
            "phone": "(818) 705-7311",
            "totalScore": 3.4,
            "rank": 1,
            "reviewsCount": 77,
            "isAdvertisement": false,
            "categoryName": "Gas station",
            "searchString": "gas station",
            "url": "https://www.google.com/maps/search/?api=1&query=Shell&query_place_id=ChIJ5SLkiLCZwoARD3u8xutOgeo"
        },
        {
            "title": "Shell",
            "address": "18101 Ventura Blvd, Tarzana, CA 91356",
            "gasPrices": [
                {
                    "priceTag": "$4.80",
                    "updatedAt": "2025-01-16T09:31:00.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.8,
                    "gasType": "Regular"
                },
                {
                    "priceTag": "$5.00",
                    "updatedAt": "2025-01-16T05:15:37.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 5,
                    "gasType": "Midgrade"
                },
                {
                    "priceTag": "$5.10",
                    "updatedAt": "2025-01-16T11:52:02.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 5.1,
                    "gasType": "Premium"
                },
                {
                    "priceTag": "$4.90",
                    "updatedAt": "2025-01-15T07:06:00.000Z",
                    "unit": "gallon",
                    "currency": "USD",
                    "price": 4.9,
                    "gasType": "Diesel"
                }
            ],
            "website": "https://find.shell.com/us/fuel/10005953-18101-ventura-blvd/en_US",
            "phone": "(818) 578-5095",
            "totalScore": 3.7,
            "rank": 2,
            "reviewsCount": 40,
            "isAdvertisement": false,
            "categoryName": "Gas station",
            "searchString": "gas station",
            "url": "https://www.google.com/maps/search/?api=1&query=Shell&query_place_id=ChIJod00UamZwoARndjeKGUQHbM"
        }
    ]
    """
    
    # Parse JSON data
    data = json.loads(json_data)
    df = pd.DataFrame(data)
    
    # Mapping between desired capitalized column names and original keys
    columns_mapping = {
        "Title": "title",
        "Address": "address",
        "Gas Prices": "gasPrices",
        "Website": "website",
        "Phone": "phone",
        "Total Score": "totalScore",
        "Rank": "rank",
        "Reviews Count": "reviewsCount",
        "Is Advertisement": "isAdvertisement",
        "Category Name": "categoryName",
        "Search String": "searchString",
        "URL": "url"
    }
    
    # Build a new DataFrame that only contains the columns we intend to output
    df_new = pd.DataFrame()
    for new_col, orig_col in columns_mapping.items():
        df_new[new_col] = df[orig_col]
        df_new[orig_col] = df[orig_col]
    
    # Order columns: first the capitalized names then the original keys
    ordered_cols = []
    for new_col, orig_col in columns_mapping.items():
        ordered_cols.extend([new_col, orig_col])
    
    df_new = df_new[ordered_cols]
    return df_new

if __name__ == "__main__":
    df = load_data_as_dataframe()
    print(df)