import Head from 'next/head'
import { Topbar, Content,Toggle } from '../component'
import styles from '../styles/Home.module.css'
import { useMobxStores } from '../stores/stores';
import { observer } from 'mobx-react';
import React, { useState } from 'react'

function Home() {

  const [togl, setToggle] = useState(false)

  const onClickHandler = () => {
    setToggle(!togl)
  }

  const { UIStore } = useMobxStores()
  console.log(togl)
  return (
    <div className={styles.container}>
      {UIStore.modalOpen ? <div className={styles.dim}>
        <div className={styles.modal}>
          {String(UIStore.modalOpen)}
          <button onClick={()=>UIStore.setModal(!UIStore.modalOpen)}>setmodal</button>
        </div>
      </div> : null}
      <div className={styles.app_wrap}>
        <Topbar />
        <Content />
        <Toggle isActive={togl} onClickHandler={onClickHandler} resource={"/images/checkbutton.png"}/>
      </div>
    </div>
  )
}

export default observer(Home)
