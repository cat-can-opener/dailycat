import React from 'react'
import styles from './Toggle.module.css'

const Toggle = (props) => {
    return(
        <button onClick={props.onClickHandler} className={styles.toggleBtn}>
            <i
                className={props.icon || "im im-heart"}
                style={{color: props.isOn ? (props.activeColor || "red") : "#999"}}
            />
        </button>
    )
}

export default Toggle