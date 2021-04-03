import React, { useState, useEffect } from 'react';
import styles from '../../styles/ListView.module.css';

const PAGE_NUMBER = 4;

export default function ListView() {
  const [state, setState] = useState([]);
  const [page, setPage] = useState(PAGE_NUMBER);

  useEffect(() => {
    fetch(`https://dog.ceo/api/breeds/image/random/${page}`)
      .then(res => res.json())
      .then(json => setState([...state, ...json.message]))
  }, [page])
  const scrollToEnd = () => {
    setPage( page + 1 )
  }

  useEffect(() => {
    window.onscroll = function() {
      // 페이지가 bottom까지 scroll됐는지 체크!!
      if (
        window.innerHeight + document.documentElement.scrollTop === document.documentElement.offsetHeight
      ) {
        scrollToEnd()
      }
    }
  })

  return (
    <div className={styles.container}>
      <div className={styles.title}>
        <div>My <span>Page</span></div>
        <img src="/assets/cat.png" alt="cat"/>  
      </div>
      <p>You've liked...</p>    
      <div className={styles.images}>
      {
        state.length > 0 && state.map((elem, i)=>
          <div key={i} className={styles.doggies}>
            <img src={elem} alt="dog" className={styles.dog}/>            
          </div>
        )
      }
      </div>
    </div>    
  )
}