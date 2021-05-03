import React from 'react'
import Link from 'next/link'
import styles from './TopBar.module.css'

const TopBar = () => {
  return (
  <div className={styles.top_bar}>
    <div>
      <Link href="/">
      Daily Cats
      </Link>
    </div>
    
    <div>
      <Link href="/MyPage">
        img
      </Link>
    </div>
    
  </div>
  )
}

export default TopBar