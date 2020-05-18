def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    base_port = app_config.base_port
    assert base_url == "http://qa_environment.com"
    assert base_port == "8080"


def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    base_port = app_config.base_port
    assert base_url == "http://dev_environment.com"
    assert base_port == "90"
