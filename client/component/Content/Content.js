import React, { useState } from "react";
import styles from './Content.module.css';
import { Toggle } from "../../component";

const Content = (props) => {
  const [heart, heartOn] = useState(false);
  const [network, networkOn] = useState(false);
  
  return (
    <div className={styles.content_wrap}>
      <div className={styles.photo}>
        <img src={props.main_image} alt="content_image"/>
      </div>
      <div className={styles.desc}>
        <div className={styles.icon_bar}>
          <Toggle
              isOn={true}
              onClickHandler={null}
              icon="im im-info"
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
              icon="im im-megaphone"
              activeColor="blue"
          />
        </div>
        <div className={styles.title_wrap}>
          <div className={styles.title_input}>
            <div>
              <input type="text" />
            </div>
            <div>
              <button>
                <i className="im im-upload"/>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Content