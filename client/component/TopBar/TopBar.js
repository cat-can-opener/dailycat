import React from 'react'
import Link from 'next/link'
import styles from './TopBar.module.css'
import Modal from '../Modal/Modal'
import { modalOpen } from '../../library/UIlibrary'
import { Login } from '../'

const TopBar = () => {
  return (
  <div className={styles.top_bar}>
    <div>
      <Link href="/">
      Daily Cats
      </Link>
    </div>
    {/* 로그인 되어있을 경우에는 mypage, 로그인 안되어있을 경우 login */}
    <div>
      <button onClick={()=>modalOpen(<Login  />)}>login</button>
      {/* <Link href="/MyPage">
        img
      </Link> */}
    </div>
    
  </div>
  )
}

export default TopBar