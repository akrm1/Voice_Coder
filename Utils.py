import re
import shutil



class File():
    DEFAULT_PATH = '/Users/akr/Desktop/HackathonGPT/Test/'

    def __init__(self, project):
        self.project = project
        self.project_path = self.DEFAULT_PATH + self.project + '/'


    def copy(self, filename, dst_path):
        TEMPLATES_LOCATION = 'templates_components/'
        src_path = self.DEFAULT_PATH + TEMPLATES_LOCATION + filename
        # Use the shutil.copy() function to copy the file
        shutil.copy(src_path, dst_path)


    def read(self, filename):
        filepath = self.project_path + filename
        with open(filepath, 'r') as file:
            contents = file.read()
        return contents


    def edit(self, filename, edit_function):
        filepath = self.project_path + filename
        with open(filepath, 'r') as f:
            file_content = f.read()
        updated_content = edit_function(file_content)
        with open(filepath, 'w') as f:
            f.write(updated_content)


    def insert_at_beginning(self, filename, insert_text):
        filepath = self.project_path + filename
        with open(filepath, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(insert_text + content)



class Regex():
    def __init__(self, text):
        self.text = text


    def get_tag_content(self, tag_name):
        start_delim = f"<{tag_name}>"
        end_delim = f"</{tag_name}>"
        pattern = re.compile(f'({re.escape(start_delim)}.*?{re.escape(end_delim)})', re.DOTALL)
        match = re.search(pattern, self.text)
        return match.group(1) if match else None


    def replace_tag(self, tag, replacement, include_tag=True):
        start_delim = f"<{tag}>"
        end_delim = f"</{tag}>"
        if include_tag:
            pattern = re.compile(f'({re.escape(start_delim)})(.*?){re.escape(end_delim)}', re.DOTALL)
            return re.sub(pattern, replacement, self.text)
        else:
            pattern = re.compile(f'(?<=<{tag}>).*?(?=</{tag}>)', re.DOTALL)
            return re.sub(pattern, replacement, self.text)

    def insert_tag_last(self, tag_name, new_text):
        start_delim = f"<{tag_name}>"
        end_delim = f"</{tag_name}>"
        pattern = re.compile(f'({re.escape(start_delim)}.*?{re.escape(end_delim)})', re.DOTALL)
        return re.sub(pattern, f"{new_text}\\1", self.text)
