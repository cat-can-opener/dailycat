import { observable, action, flow, makeObservable, toJS } from "mobx";

class TitleStore {
  constructor() {
    makeObservable(this, {
      list: observable,
      fetchTitle: action,
      modfiyTitle: action,
      deleteTitle: action,
    });
  }

  url = process.env.BASE_URL;
  endPoint = "/title";

  list = [
    {
      id: 0,
      title: "정말로 못생긴 고양이네요",
      user_id: 2,
      user_name: "임진규",
      isLiked: false,
    },
    {
      id: 1,
      title: "정말로 못생긴 고양이네요1",
      user_id: 2,
      user_name: "임진규",
      isLiked: true,
    },
    {
      id: 2,
      title: "정말로 잘생긴 고양이네요",
      user_id: 3,
      user_name: "패트릭",
      isLiked: false,
    },
  ];

  fetchTitle = () => {};

  addTitle = (data) => {
    this.list = this.list.concat(data);
  };

  modfiyTitle = (data) => {
    this.list = this.list.map((info) => {
      if (info.id === data.id) {
        info.title = data.title;
        return info;
      }
      return info;
    });
  };

  deleteTitle = (id) => {
    this.list = this.list.filter(id !== id);
  };
}

export default TitleStore;
