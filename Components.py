from App import create_component


def create_route(url_path, inner=''):
    route_url = f'exact path=\'{url_path}\''
    route_comp = create_component('Route', route_url, inner, has_dependency=False)
    return route_comp

def create_button(button_text=''):
    button_comp = create_component('Button')
    return button_comp

def create_home_page():
    home_comp = create_component('HomePage')
    return home_comp

def create_navigation_bar():
    nav_comp = create_component('NavigationBar')
    return nav_comp
