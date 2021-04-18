import React, { useState, useEffect } from 'react';
import styles from './ListView.module.css';

const PAGE_NUMBER = 9;

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

  const makeViewList = () => {
    const result = []
    while(state.length > 0){
      result.push(state.splice(0,3))
    }
    return result
  }

  const list = makeViewList()

  return (
    <div className={styles.container}>
      <div className={styles.title}>
        <div>My <span>Page</span></div>
        {/* <img src="/images/dog.jpg" alt="cat"/>   */}
      </div>
      <p className={styles.sentence}>You've liked...</p>    
      <div className={styles.images}>
      {
        list.length > 0 && list.map((elem, i)=>
          <div key={i} className={styles.doggies}>
            {elem.map((info, key) => (<img style={{width: "300px"}} src={info} key={key} alt="dog" className={styles.dog}/>))}
          </div>
        )
      }
      </div>
    </div>    
  )
}