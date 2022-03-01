import requests
import pygal
from pygal.style import Style
py_url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
js_url = "https://api.github.com/search/repositories?q=language:javascript&sort=stars"
py_responce = requests.get(py_url)
js_responce = requests.get(js_url)
print(f"Python status code : {py_responce.status_code}")
print(f"JavaScript status code :  {js_responce.status_code}")
py_response_dict = py_responce.json()
js_response_dict = js_responce.json()
py_repo_dicts = py_response_dict["items"]
js_repo_dicts = js_response_dict["items"]
py_stars = []
js_stars = []
i = 0
x = 0
for py_repo_dict in py_repo_dicts:
    py_stars.append(py_repo_dicts[i]["stargazers_count"])
    i += 1
for js_repo_dict in py_repo_dicts:
    js_stars.append(js_repo_dicts[x]["stargazers_count"])
    x += 1
custom_style = Style(colors =("#E80080", "#404040", "#9BC950"))
chart = pygal.Bar(style=custom_style, x_label_rotation=90, show_legend=True)
chart.title = "Most-Starred Python and JavaScript Projects on GitHub"
chart.add("Python", py_stars)
chart.add("JavaScript", js_stars)
chart.render_in_browser()
