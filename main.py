import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# imported requests moduke
# store the url of the api call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# call get and pass it to the the url, store the response object in varible r
r = requests.get(url)
# print status code to ensure that a call was succesful
print("Status code:", r.status_code)

# API returns the information in JSON format, so we use the json() method
response_dict = r.json()

print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repositories returend:", len(repo_dicts))

repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])


# explore information about repositories
names, plot_dicts = [], []
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    
    description = repo_dict['description']
    if not description:
        description = "No description provided."
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
    }
    plot_dicts.append(plot_dict)
    
    # Make visualization
    my_style = LS('#333366', base_style=LCS)
    my_style.title_font_size = 24
    my_style.label_font_size = 14
    my_style.major_label_font_size = 18
    
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000
    
    
    
    chart = pygal.Bar(style=my_style, x_label_rotating=45, show_legend=False)
    chart.title = 'Most-Starred Python Projects on Github'
    chart.x_labels = names
    
    
    chart.add('', plot_dicts)
    chart.render_to_file('python_repos.svg')
    
    
    
    
    
    
    
    # print("\nName:" , repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('Repository:', repo_dict['html_url'])
    # print('Description:', repo_dict['description'])


