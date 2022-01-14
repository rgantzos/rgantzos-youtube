import requests
from flask import Flask, jsonify
app = Flask('app')
import os
os.system('pip install scratchconnect')
my_secret = os.environ['Password']
# the value should be your password - no one else will be able to see it

@app.route('/')
def hello_world():
  while True:
    userdata = requests.get('https://api.scratchstatus.org/523967150/views/').text

    partitioned_string = userdata.partition(':')
    before_first_period = partitioned_string[2]
    partitioned_string = before_first_period.partition('}')
    title = partitioned_string[0]

    import scratchconnect

    user = scratchconnect.ScratchConnect("rPYTHONbot", my_secret)

    project = user.connect_project(project_id=628483514,
                               access_unshared=True)
    variables = project.connect_cloud_variables()
    set = variables.set_cloud_variable(variable_name="Views", value=title)

    if set:
        print('Set!')
    
    return jsonify({"views":int(title)})

app.run(host='0.0.0.0', port=8000)
