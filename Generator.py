from Project import Project
from App import *
from Components import *


def generate_project():
    project = Project()
    project.create()

    app = App(project.project)

    home_page = create_home_page()
    nav_bar = create_navigation_bar()
    route = create_route('/', nav_bar)

    app.run(route)
    project.start(in_background=True)

    output_log = 'Project successfully created'
    print(output_log)
    return output_log


