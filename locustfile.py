from locust import HttpUser, task, between

class MyUser(HttpUser): 
    wait_time = between(1, 2)
    
    @task
    def index(self):
        response = self.client.get("http://nginx_load_balancer:80/")