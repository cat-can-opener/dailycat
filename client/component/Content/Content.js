import React from 'react';
import styles from './Content.module.css';

const Content = () => {
  return (
    <div className={styles.content_wrap}>
      <div className={styles.photo}></div>
      <div className={styles.desc}></div>
    </div>
  )
}

export default Content