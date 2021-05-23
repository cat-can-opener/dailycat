import React, { useState, useEffect } from 'react'
import styles from './Modal.module.css'

const Modal = (props) => {
    const [animate, setAnimate] = useState(false)

    useEffect(() => {
        if(props.isActive){
            setAnimate(true)
        }
        return ()=>setAnimate(false)
        
    }, [props.isActive]);

    if(!props.isActive){ return null }
    return(
        <div className={styles.dim + ` ${animate ? styles.dim_active : ''}` } onClick={props.close}>
            <div className={styles.modal} onClick={(e)=>e.stopPropagation()}>
                <button className={styles.modal_close} onClick={props.close}>X</button>
                {props.content}
            </div>
        </div>
    )
}

export default Modal