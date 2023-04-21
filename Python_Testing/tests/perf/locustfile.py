from locust import HttpUser, task

class ProjectPerfTest(HttpUser):

    @task
    def test_perf_loading_competition(self):
        self.client.get('/book/Spring%20Festival/Simply%20Lift')

    @task
    def test_perf_update_data(self):
        self.client.post('/purchasePlaces', data={ 'club' : 'Simply Lift', 'competition' : 'Spring Festival',  'places' : 3})
