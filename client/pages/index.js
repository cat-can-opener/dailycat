import Head from "next/head";
import { Content, Layout } from "../component";
import styles from "../styles/Home.module.css";
import { useMobxStores } from "../stores/stores";
import * as UIlib from "../library/UIlibrary";
import { observer } from "mobx-react";
import React, { useEffect } from "react";

function Home() {
  const { CatStore } = useMobxStores()

  useEffect(() => {
    CatStore.fetchCat()
  }, [])


  return (
    <div className={styles.container}>
      <div className={styles.app_wrap}>
        <Layout />
        <Content main_image={CatStore.list[0]} />
      </div>
    </div>
  );
}

export default observer(Home);
