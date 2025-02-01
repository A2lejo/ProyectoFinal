from locust import HttpUser, task, between

class MyUser(HttpUser): #Esta clase hereda de HttpUser, que se utiliza para pruebas de rendimiento HTTP
    wait_time = between(1, 2) #Esto establece un tiempo de espera aleatorio entre 1 y 2 segundos entre tareas.
    
    @task
    def index(self): #El método index envía una solicitud GET a la URL especificada.
        response = self.client.get("http://application1_pf:5000/")