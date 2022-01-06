import pandas as pd
import requests


def run_query():
    #query tarkov unofficial api with defined request *query*
    def run_query(query):
        response = requests.post('https://tarkov-tools.com/graphql', json={'query': query})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))

    #specifies the attributes sent to the graphql database - doc: https://tarkov-tools.com/___graphql
    def query_live_data():

        #query params
        new_query = """
        {
            itemsByName(name: "") {
                id
                name
                types
            }
        }
        """

        #send the query, returns error if unsuccesful
        result = run_query(new_query)
        #normalize data and input into pandas dataframe
        df = pd.json_normalize(result['data']['itemsByName'])
        return df
    
    df = query_live_data()
    return df

df = run_query()
df.to_csv('items_by_id.csv')