import responses, requests, unittest
from poller import poll

class TestPollerMethods(unittest.TestCase):
    # Testing for common HTTP issues
    @responses.activate
    def test_my_api_error(self):
        responses.get(
            "https://stat.ripe.net/data/country-resource-list/data.json?resource=us&v4_format=prefix",
            status=404,
        )

        with self.assertRaises(SystemExit):
            poll.poll_url("https://stat.ripe.net/data/country-resource-list/data.json", {'resource': 'us', "v4_format":"prefix"})

    @responses.activate
    def test_my_api_success(self):
        responses.get(
            "https://stat.ripe.net/data/country-resource-list/data.json?resource=us&v4_format=prefix",
            status=200,
            json={"data": "some_data"}
        )

        result = poll.poll_url("https://stat.ripe.net/data/country-resource-list/data.json", {'resource': 'us', "v4_format":"prefix"})

        assert result == {"data": "some_data"}

if __name__ == '__main__':
    unittest.main()