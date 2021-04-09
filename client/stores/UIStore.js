import { observable, action, makeObservable } from 'mobx';

class UIStore {

    constructor() {
        makeObservable(this,{
            modalOpen: observable,
            handleModal: action
        })
    }

    modalOpen = false
    modalContent = null
    handleModal(value, content) {
        this.modalOpen = value
        this.modalContent = content
    }
}

export default UIStore;
