import UIStore from './UIStore';
import React from 'react'
import CatStore from './CatStore';

let clientSideStores;

const isServer = typeof window === 'undefined';

export function getStores(initialData = { postStoreInitialData: {} }) {
  if (isServer) {
    return {
    //   postStore: new PostStore(initialData.postStoreInitialData),
      CatStore: new CatStore(),
      UIStore: new UIStore(),
    };
  }
  if (!clientSideStores) {
    clientSideStores = {
    //   postStore: new PostStore(initialData.postStoreInitialData),
      CatStore: new CatStore(),
      UIStore: new UIStore(),
    };
  }

  return clientSideStores;
}

const StoreContext = React.createContext();

export function StoreProvider(props) {
  return <StoreContext.Provider value={props.value}>{props.children}</StoreContext.Provider>;
}

export function useMobxStores() {
  return React.useContext(StoreContext);
}
