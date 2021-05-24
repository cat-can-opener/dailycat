import { observable, action, flow, makeObservable, toJS } from "mobx";

class UserStore {
  constructor() {
    makeObservable(this, {
      user_id: observable,
      isLogin: observable,
      session: observable,
      login: action,
      logout: action,
    });
  }

  url = process.env.BASE_URL;
  endPoint = "/user";

  user_id = 2;
  isLogin = false;
  session = {};

  login = () => {
    this.isLogin = true;
  };

  logout = () => {
    this.isLogin = false;
    this.session = {};
  };

  getSession = () => {};
}

export default UserStore;
