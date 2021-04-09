import { TopBar, Modal } from '../';
import { useMobxStores } from '../../stores/stores';
import { observer } from 'mobx-react';

const Layout = () => {
    const { UIStore } = useMobxStores()
    return(
        <>
            <Modal
                isActive={UIStore.modalOpen}
                close={()=>UIStore.handleModal(false, null)}
                content={UIStore.modalContent}
            />
            <TopBar/>
        </>
    )
}

export default observer(Layout)