import { getStores } from '../stores/stores';

const UIStore = getStores().UIStore

export function modalOpen(content){
    UIStore.handleModal(true, content)
}
