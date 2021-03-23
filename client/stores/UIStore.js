import { observable, action, makeObservable } from 'mobx';

class UIStore {

    constructor() {
        makeObservable(this,{
            searchOverlayOpen: observable,
            setSearchOverlayOpen: action
        })
    }

    searchOverlayOpen = false;

    setSearchOverlayOpen(value) {
        this.searchOverlayOpen = value;
    }


}

export default UIStore;
