import UIStore from "./UIStore";
import React from "react";
import CatStore from "./CatStore";
import UserStore from "./UserStore";
import TitleStore from "./TitleStore";

let clientSideStores;

const isServer = typeof window === "undefined";

export function getStores(initialData = { postStoreInitialData: {} }) {
  if (isServer) {
    return {
      //   postStore: new PostStore(initialData.postStoreInitialData),
      CatStore: new CatStore(),
      UIStore: new UIStore(),
      UserStore: new UserStore(),
      TitleStore: new TitleStore(),
    };
  }
  if (!clientSideStores) {
    clientSideStores = {
      //   postStore: new PostStore(initialData.postStoreInitialData),
      CatStore: new CatStore(),
      UIStore: new UIStore(),
      UserStore: new UserStore(),
      TitleStore: new TitleStore(),
    };
  }

  return clientSideStores;
}

const StoreContext = React.createContext();

export function StoreProvider(props) {
  return (
    <StoreContext.Provider value={props.value}>
      {props.children}
    </StoreContext.Provider>
  );
}

export function useMobxStores() {
  return React.useContext(StoreContext);
}
