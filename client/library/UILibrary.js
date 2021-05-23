import { getStores } from '../stores/stores';

const UIStore = getStores().UIStore

export function modalOpen(content){
    UIStore.handleModal(false, null)
    UIStore.handleModal(true, content)
}