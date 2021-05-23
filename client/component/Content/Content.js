import React, { useState } from "react";
import styles from "./Content.module.css";
import { Toggle } from "../../component";
import { useMobxStores } from "../../stores/stores";

const Content = (props) => {
  const [heart, heartOn] = useState(false);
  const [network, networkOn] = useState(false);
  const [inputTitle, setInputTitle] = useState("");
  const { TitleStore, UserStore } = useMobxStores();
  console.log(TitleStore, UserStore);
  const titleList = TitleStore.list.map((info, key) => (
    <ul>
      <li key={key}>
        <div>{info.title}</div>
        <div>
          <Toggle
            isOn={info.isLiked}
            onClickHandler={null}
            icon="im im-heart"
            activeColor="blue"
          />
          {UserStore.user_id === info.user_id ? (
            <Toggle
              isOn={true}
              onClickHandler={() =>
                TitleStore.modifyTitle({ id: info.id, title: inputTitle })
              }
              icon="im im-gear"
              activeColor="gray"
            />
          ) : null}
          {UserStore.user_id === info.user_id ? (
            <Toggle
              isOn={true}
              onClickHandler={() => TitleStore.deleteTitle(info.id)}
              icon="im im-x-mark-circle-o"
              activeColor="red"
            />
          ) : null}
        </div>
      </li>
    </ul>
  ));

  return (
    <div className={styles.content_wrap}>
      <div className={styles.photo}>
        <img src={props.main_image} alt="content_image" />
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
            onClickHandler={() => heartOn(!heart)}
            icon="im im-heart"
            activeColor="red"
          />
          <Toggle
            isOn={network}
            onClickHandler={() => networkOn(!network)}
            icon="im im-megaphone"
            activeColor="blue"
          />
        </div>
        <div className={styles.title_wrap}>
          <div className={styles.title_list}>{titleList}</div>
          <div className={styles.title_input}>
            <div>
              <input
                type="text"
                value={inputTitle}
                onChange={(e) => setInputTitle(e.target.value)}
              />
            </div>
            <div>
              <button>
                <i className="im im-upload" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Content;
