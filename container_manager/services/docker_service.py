import docker


class DockerService:
    def __init__(self):
        self.client = docker.from_env()

    def get(self, name):
        return self.client.containers.get(name)

    def get_all(self):  # Future use case
        return self.client.containers.list()

    def create(self, name, image, envs, command):
        return self.client.containers.run(
            image=image,
            name=name,
            environment=envs,
            command=command,
            detach=True,
        )

    def update(self, name, image, envs, command):
        self.delete(name)
        return self.create(name, image, envs, command)

    def update_name(self, old_name, new_name):  # Future use case
        container = self.get(old_name)
        container.containers.rename(new_name)

    def delete(self, name):
        container = self.get(name)
        container.remove(force=True)
