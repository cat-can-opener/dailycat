import React, { useState } from "react";
import { Content, Toggle, Layout } from "../../component";
import containerStyles from "../../styles/Home.module.css";
import { ListView } from "../../component";

export default function MyPage() {
  const [data, setData] = useState([]);

  const fetchImage = () => {
    const PAGE_NUMBER = 9;
    fetch(`https://dog.ceo/api/breeds/image/random/${PAGE_NUMBER}`)
      .then((res) => res.json())
      .then((json) => setData(data.concat(json.message)));
  };

  return (
    <div className={containerStyles.container}>
      <div className={containerStyles.app_wrap}>
        <Layout />
        {/* <p className={styles.sentence}>You've liked…</p> */}
        <ListView column={3} fetchMethod={fetchImage} data={data} />
      </div>
    </div>
  );
}
