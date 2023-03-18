from Utils import *

dependencies = set()

def add_dependency(dependency):
    global dependencies
    dependencies.add(dependency)


def create_component(tag, attrs='', inner='', has_dependency=True):
    if has_dependency:
        add_dependency(tag)

    if not inner:
        return f'<{tag} {attrs}/>'
    else:
        return f'<{tag} {attrs}>\n{inner}\n</{tag}>'


class App():
    def __init__(self, project):
        self.project = project
        self.file = File(self.project)


    def setup_app(self):
        global dependencies
        imports = ''

        for dependency in dependencies:
            # copy components into {Project}/src/components/{Component}.tsx
            comp_file = f"{dependency}.tsx"
            target_path = File.DEFAULT_PATH + self.project + '/src/components/' + comp_file
            self.file.copy(comp_file, target_path)

            imports += f"import {dependency} from './components/{dependency}';\n"

        app_file = 'src/App.tsx'
        self.file.insert_at_beginning(app_file, imports)

    def apply_components(self, components):
        app_file = 'src/App.tsx'
        app_content = self.file.read(app_file)
        self.file.edit(app_file,
                       lambda file_content: Regex(app_content).replace_tag('IonRouterOutlet', components, include_tag=False))


    def run(self, content):
        self.setup_app()
        self.apply_components(content)




