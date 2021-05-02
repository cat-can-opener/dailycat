import Head from "next/head";
import { Content, Layout } from "../component";
import styles from "../styles/Home.module.css";
import { useMobxStores } from "../stores/stores";
import * as UIlib from "../library/UIlibrary";
import { observer } from "mobx-react";
import React, { useState } from "react";

function Home() {
  return (
    <div className={styles.container}>
      <div className={styles.app_wrap}>
        <Layout />
        <Content />
      </div>
    </div>
  );
}

export default Home;
