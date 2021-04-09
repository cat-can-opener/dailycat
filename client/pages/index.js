import Head from 'next/head'
import { Content, Toggle, Layout } from '../component'
import styles from '../styles/Home.module.css'
import { useMobxStores } from '../stores/stores'
import * as UIlib from '../library/UIlibrary'
import { observer } from 'mobx-react'
import React, { useState } from 'react'

function Home() {

  const [togl, setToggle] = useState(false)

  const onClickHandler = () => {
    setToggle(!togl)
  }

  const { UIStore } = useMobxStores()
  const modalContent = (<div style={{width: "300px", height: "300px", backgroundColor: "#fff"}}>isModal</div>)
  
  return (
    <div className={styles.container}>
      <div className={styles.app_wrap}>
        <Layout />
        <Content />
        <button onClick={()=>UIlib.modalOpen(modalContent)}>modal!</button>
        <Toggle isActive={togl} onClickHandler={onClickHandler} resource={"/images/checkbutton.png"}/>
      </div>
    </div>
  )
}

export default Home
