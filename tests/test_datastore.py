import unittest, json

from storage import datastore

class TestStore(unittest.TestCase):
    def test_store_return_type(self):

        url_data = json.loads('{"data": {"resources": {"ipv4": [ "1","2"] } } }')
        print(type(url_data))
        mylist = datastore.store(url_data)
        assert isinstance(mylist, list)

if __name__ == '__main__':
    unittest.main()