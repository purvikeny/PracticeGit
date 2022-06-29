from utilities.BaseClass import BaseClass
from algoliasearch.search_client import SearchClient
import config
import re

class TestAlgolia(BaseClass):
    tenet = config.tenet
    applicationName = config.applicationNameMyfont
    authenv = config.environment

    def test_validate_results(self):

        client = SearchClient.create("RLPEOSLXDV", "f68bcfb891edf1a8c1cbcc3fa98a2946")

        # Create a new index and add a record
        index = client.init_index("product_data")

        #Search the index and print the results
        res = index.search('T', {
            'attributesToRetrieve': [
                'title',
                'tags',
                'foundry_title'
            ],
            'hitsPerPage': 8
        })
        results = res["hits"]
        results = str(results)
        fonts = re.findall(", 'title': '(.*?)', '", results)
        print(fonts)
        print("test complete")
