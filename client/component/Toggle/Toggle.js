import React from 'react'
import styles from './Toggle.module.css'

const Toggle = (props) => {
    return(
        <button onClick={props.onClickHandler} className={styles.toggleBtn}>
            <img src="/images/dog.jpg" className={styles.toggle_dog_like}/>
        </button>
    )
}

export default Toggle