import secrets
import subprocess


class Project():

    DEFAULT_PATH = '/Users/akr/Desktop/HackathonGPT/Test'

    def __init__(self, project_name='Project'):
        self.project = self.generate_name(project_name)
        self.target_path = self.DEFAULT_PATH

    def generate_name(self, project_name):
        key = secrets.token_hex(16)
        return project_name + "_" + key


    def create(self):
        script_name = 'create_ionic_project.sh'
        command = ['bash', script_name, self.project]
        result = subprocess.run(command, cwd=self.target_path, capture_output=True)

        if result.returncode == 0:
            return self.project
        else:
            return result.returncode, result.stdout.decode()


    def start(self, in_background=True):
        script_name = 'start_ionic_project.sh'
        command = ['bash', script_name, self.project]

        process = None
        if in_background:
            process = subprocess.Popen(command, cwd=self.target_path)
        else:
            process = subprocess.run(command, cwd=self.target_path, capture_output=True)

        return process



