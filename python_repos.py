import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

def get_config():
    chart_config = {}
    my_style = LS('#333366', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 14
    my_config.label_font_size = 14
    my_config.major_label_font_size = 10
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000
    my_config.tooltip_font_size = 10
    my_config.value_font_size = 10
    
    chart_config = {
        'config': my_config,
        'style' : my_style
    }
    
    return chart_config
    
def get_repo_dict():
    URL = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(URL)
    print('Status code: ', r.status_code) # Status code 200 is success

    response_dict = r.json()
    print("Total repositories:", response_dict['total_count'])

    repo_dicts = response_dict['items']
    print("Repositories returned:", len(repo_dicts))
    
    return repo_dicts

repo_dicts = get_repo_dict()

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    if not repo_dict['stargazers_count']:
        repo_dict['stargazers_count'] = 'null'
        print("Repository has no count:" + repo_dict['name'])
    
    if not repo_dict['description']:
        repo_dict['description'] = ''
        print("Repository has no description:" + repo_dict['name'])
           
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    
    }
    plot_dicts.append(plot_dict)

chart_config = get_config();
chart = pygal.Bar(chart_config['config'], style = chart_config['style'])
chart.title = 'Most Starred Python Projects in GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
