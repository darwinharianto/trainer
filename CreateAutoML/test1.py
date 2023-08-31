from dataModel.user import User
import json
import requests
CVAT_ADDRESS = "http://localhost:8081"

def test_registered_user():
    result = User.check_credentials(username="hdarwin", password="P4sona123")
    if result.status_code == 200:
        return result
    else:
        raise LookupError('User Authentication Error')
    

    
if __name__=="__main__":
    loginResponse = test_registered_user()
    url = CVAT_ADDRESS + "/api/projects"

    headers = {
        "Content-Type": "application/json",
        "Authentication": f"Token {json.loads(loginResponse.content)['key']}"
    }
    print(type(loginResponse.cookies))
    print(headers)
    projects = requests.get(url, headers=headers, cookies=loginResponse.cookies)
    print(projects.content)