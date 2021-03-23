# 팀 캔따개 Client 작업문서

## 개발환경
- react
- next.js
- mobx
- gitflow
- jest


## 개발시 주의사항
1. [gitflow](http://amazingguni.github.io/blog/2016/03/git-branch-%EA%B7%9C%EC%B9%99)에 따른 브랜치 관리 규칙을 따라주세요
```bash
/* 개발환경에서는 master branch를 사용하시면 안됩니다. */

git checkout develop
git pull

git checkout feature/작업이름
```

```bash
/* 푸쉬할경우 */
git push origin feature/작업이름
```

2. 작업 시작전 git pull / npm install은 필수입니다!

```bash
git pull  //develop branch
npm install
npm run dev
```

3. pages디렉토리에 컴포넌트를 추가하지마세요 next.js 특성상 pages 디렉토리에 만들 js파일은 자동으로 라우트가 연결됩니다.

4. pages componet 제작시 각 루트디렉토리가 아닌 별개 디렉토리로 구분하여 작업해주세요
```
예 ) pages/MyPage/index.js   // url: http://localhost:3000/Mypage
예 ) component/ModalPopup/ModalPopup.js
```

---

## Mobx Store 사용방법
1. useMobxSotres와 observer를 각각 import 합니다.
```javascript
import { useMobxStores } from '../stores/stores';
import { observer } from 'mobx-react';
```
2. import한 useMobxStores로부터 사용할 Store를 불러와 사용합니다
```javascript
const Text = () => {
    const { UIStore } = useMobxStores()
    const str = String(UIStore.searchOverlayOpen)
    return(
        <div>{str}</div>
    )

}
```

3. export시 observer함수를 사용하여 컴포넌트를 내보냅니다. (Store에 observable 인스턴스를 사용한 경우)
```javascript
export default observer(Text)
```

## Mobx Store 생성방법
1. stores 디렉토리에 새로운 스토어.js 생성

```javascript
import { observable, action, makeObservable } from 'mobx';

class UIStore {
    constructor() {
        makeObservable(this,{
            searchOverlayOpen: observable,
            setSearchOverlayOpen: action
        })
    }

    searchOverlayOpen = false;

    setSearchOverlayOpen(value) {
        this.searchOverlayOpen = value;
    }

}
export default UIStore;

```
2. stores/stores.js 파일 getStores 함수수정

```javascript
/*
서버사이드 렌더링을 자동으로 지원하는 next.js에 특성상
서버사이드 렌더링이 될 경우와 클라이언트 사이드 렌더링이 될 경우에 분기처리를 해야합니다.
*/
export function getStores(initialData = { postStoreInitialData: {} }) {
  if (isServer) {
    return {
    //   postStore: new PostStore(initialData.postStoreInitialData),
    //   해당위치에 새로운 스토어 인스턴스를 생성합니다.
      UIStore: new UIStore(),
    };
  }
  if (!clientSideStores) {
    clientSideStores = {
    //   postStore: new PostStore(initialData.postStoreInitialData),
    //   해당위치에 새로운 스토어 인스턴스를 생성합니다.
      UIStore: new UIStore(),
    };
  }

  return clientSideStores;
}

```


