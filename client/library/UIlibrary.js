import { getStores } from "../stores/stores";

const UIStore = getStores().UIStore;

export function modalOpen(content) {
  UIStore.handleModal(true, content);
}

export function modalClose() {
  UIStore.handleModal(false, null);
}
