import React from "react";
import Link from "next/link";
import styles from "./TopBar.module.css";
import { useMobxStores } from "../../stores/stores";
import { observer } from "mobx-react";
import { modalOpen } from "../../library/UIlibrary";
import { Login } from "../";

const TopBar = () => {
  const { UserStore } = useMobxStores();
  return (
    <div className={styles.top_bar}>
      <div>
        <Link href="/">Daily Cats</Link>
      </div>
      {/* 로그인 되어있을 경우에는 mypage, 로그인 안되어있을 경우 login */}
      <div>
        {!UserStore.isLogin ? (
          <button
            className={styles.loginBtn}
            onClick={() => modalOpen(<Login />)}
          >
            <i className="im im-user-circle"></i>
          </button>
        ) : (
          <Link href="/MyPage">
            <button className={styles.loginBtn}>
              <i class="im im-plus-circle"></i>
            </button>
          </Link>
        )}
      </div>
    </div>
  );
};

export default observer(TopBar);
