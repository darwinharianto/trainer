import reflex as rx
from requests.cookies import RequestsCookieJar
from ..dataModel.user import User
import json
from enum import Enum

class Roles:
    @staticmethod
    def role(itr:int):
        match itr:
            case 0:
                return "unknown"
            case 1:
                return "superuser"
            case 2:
                return "business"
            case 3:
                return "user"
            case 4:
                return "worker"
            case _:
                return "unknown"

class LoginStatus:
    @staticmethod
    def status(itr:int):
        match itr:
            case 0:
                return "succeed"
            case 1:
                return "fail"
            case 2:
                return "waiting"
            
class State(rx.State):
    """The app state."""
    username: str
    password :str
    token: str
    loginStatus: str = LoginStatus.status(2)

    @rx.var
    def user_role(self) -> str:
        # TODO query from database for user roles, or maybe from CVAT?
        return "aa"#Roles.role(1)

    @rx.var
    def logged_in(self) -> bool:
        # TODO query from database if user still logged in
        return self.loginStatus == LoginStatus.status(0)
    
    @rx.var
    def login_fail(self) -> bool:
        # TODO query from database if user still logged in
        return self.loginStatus == LoginStatus.status(1)
    
    @rx.var
    def client_ip(self):
        return self.get_client_ip()

    @rx.var
    def current_page(self):
        return self.get_current_page()

    @rx.var
    def cookies(self):
        return str(self.get_cookies())

    def reroute(self):
        if not self.logged_in:
            return rx.redirect("/login")

    def user_login(self):
        response = User.check_credentials(username=self.username, password=self.password)
        if response.status_code != 200:
            self.loginStatus = LoginStatus.status(1)
            return
        
        self.loginStatus = LoginStatus.status(0)
        self.password = None # delete reference to password, is this enough?
        self.token = json.loads(response.content)['key']
        for cookie in response.cookies:
            rx.set_cookie(cookie.name, cookie.value)
            
        return rx.redirect("/projects")
    
    def register_user(self):
        # raise NotImplementedError
        return