from main import get_cat

def test_get_cat_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        "id":"TBA3JzB9P",
        "url":"https://s3.us-west-2.amazonaws.com/cdn2.thecatapi.com/images/TBA3JzB9P.jpg",
        "width":1200,
        "height":856}]
    assert get_cat() == "https://s3.us-west-2.amazonaws.com/cdn2.thecatapi.com/images/TBA3JzB9P.jpg"

def test_get_cat_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    assert get_cat() is None
