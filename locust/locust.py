from locust import HttpUser, constant, task


class NoOrmUser(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = constant(0)

    @task
    def select_operation(self):
        with self.client.get("/", name="GET /", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status: {response.status_code}")

    @task
    def insert_operation(self):
        payload = {"description": "load-test"}
        headers = {"Content-Type": "application/json"}
        with self.client.post(
            "/",
            json=payload,
            headers=headers,
            name="POST /",
            catch_response=True,
            timeout=10,
        ) as response:
            if response.status_code != 201:
                response.failure(f"Unexpected status: {response.status_code}")
