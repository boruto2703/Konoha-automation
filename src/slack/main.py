"""
list_of_result = {
  "team": [],
  "project": [],
  "repo": []
}
"""


class SlackMessage():

    def __init__(self, type: str):
        self.list_of_result[type] = []
        pass

    def add_result(self, result):
        self.list_of_result[type].append(result)
        pass

    def show_result(self):
        for category, res in self.list_of_result.items():
            print(f'\n ** Result in {category}')
            for r in res:
                print(f'\n - {r}')

    def send_message_to_slack(self):
        pass
