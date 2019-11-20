sudo pip3 install -r deployment/required_python_packages.txt

# Run tests and save with format by date
pytest -v src/main/suite_all_tests.py  --json=src/slack/test_results/test_result_`date '+%C%y%m%d_%H_%M'`.json

# Json file has been save. Now get the result and send to Slack

