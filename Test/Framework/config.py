class Config:

    def __init__(self, env):
        self.base_url = {

            'qa': "http://qa_environment.com",
            'dev': "http://dev_environment.com"
        }[env]

        self.base_port = {

            'qa': "8080",
            'dev': "90"
        }[env]





