from cloudant import Cloudant
from locust import HttpLocust, Locust, TaskSet, task
import json
import os
import random


def random_subset(col, num=1):
    indices = random.sample(range(len(col)), num)
    return [col[i] for i in sorted(indices)]


class UserBehavior(TaskSet):

    def on_start(self):
        with open('fixture.json', 'r') as infile:
            fixture = json.load(infile)
        self.ids = fixture['ids']
        self.teams = fixture['teams']

    @task
    def all_docs(self):
        id = random_subset(self.ids, 1)[0]
        team = random_subset(self.teams, 1)[0]
        keys = "[[\"{}\", \"{}\"]]".format(team, id)
        self.client.get('/test/_design/api/_view/all_docs',
            params={'include_docs': "true", 'keys': keys},
            auth = (os.environ['CLOUDANT_USERNAME'], os.environ['CLOUDANT_PASSWORD']))
        # print(self.client.get_view_raw_result('_design/api', 'all_docs', include_docs=True, keys=[[team, id]]))

class CloudantLocust(HttpLocust):
    def __init__(self, *args, **kwargs):
        # c = Cloudant(self.username,
        #              self.password,
        #              account=self.username)
        #
        # c.connect()
        # self.db = c[self.test_db]
        # self.client = self.db.r_session
        pass

class OvationUser(HttpLocust):
    task_set = UserBehavior

    min_wait = 1000 #default
    max_wait = 1000 #default
