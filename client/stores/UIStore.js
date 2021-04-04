import { observable, action, makeObservable } from 'mobx';

class UIStore {

    constructor() {
        makeObservable(this,{
            searchOverlayOpen: observable,
            setSearchOverlayOpen: action,
            modalOpen: observable,
            setModal: action
        })
    }

    modalOpen = false
    setModal(value) {
        this.modalOpen = value
    }


    searchOverlayOpen = false;

    setSearchOverlayOpen(value) {
        this.searchOverlayOpen = value;
    }


}

export default UIStore;
