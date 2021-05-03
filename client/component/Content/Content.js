import React, { useState } from "react";
import styles from './Content.module.css';
import { Toggle } from "../../component";

const Content = () => {
  const [heart, heartOn] = useState(false);
  const [bug, bugOn] = useState(false);
  const [network, networkOn] = useState(false);
  
  return (
    <div className={styles.content_wrap}>
      <div className={styles.photo}></div>
      <div className={styles.desc}>
        <Toggle
            isOn={bug}
            onClickHandler={()=>bugOn(!bug)}
            icon="im im-bug"
            activeColor="orange"
        />
        <Toggle
            isOn={heart}
            onClickHandler={()=>heartOn(!heart)}
            icon="im im-heart"
            activeColor="red"
        />
        <Toggle
            isOn={network}
            onClickHandler={()=>networkOn(!network)}
            icon="im im-network"
            activeColor="blue"
        />
      </div>
    </div>
  )
}

export default Content