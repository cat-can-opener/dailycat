import React from "react";
import { Layout } from "../../component";
import containerStyles from "../../styles/Home.module.css";
import { useMobxStores } from "../../stores/stores";
import { ListView } from "../../component";
import { observer } from "mobx-react";

function MyPage() {
  const {CatStore} = useMobxStores()
  
  return (
    <div className={containerStyles.container}>
      <div className={containerStyles.app_wrap}>
        <Layout />
        <ListView column={3} fetchMethod={CatStore.fetchCat} data={CatStore.list} />
      </div>
    </div>
  );
}

export default observer(MyPage)