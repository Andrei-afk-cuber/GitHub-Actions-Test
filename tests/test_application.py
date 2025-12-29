from app import app

class TestApplication:
    # test successful running
    def test_run_application(self, response):
        print(response.status_code)
        assert response.status_code == 200, "Server error"

    # test page data
    def test_check_page_data(self, response):
        assert response.data.decode("utf-8") == "Its develop application", "Incorrect data"