import { observable, action, flow, makeObservable, toJS } from 'mobx';

class CatStore {

    constructor() {
        makeObservable(this,{
            list: observable,
            removeCatList: action
        })

        this.fetchCat = this.fetchCat.bind(this);
    }

    url = process.env.BASE_URL
    endPoint = "/cat"

    list = []

    fetchCat = flow(function* (page) {
        const PAGE_NUMBER = 9
        const call = function() {
            return fetch(`https://dog.ceo/api/breeds/image/random/${PAGE_NUMBER}`)
        }
    
        try {
            const res = yield call(page)
            if(res.status === 200){
                const result = yield res.json()
                const list = toJS(this.list)
                this.list = list.concat(result.message)
                return list
            }
        } catch(err) {
            console.log(err.message)
        }
        
    })

    removeCatList = () => {
        this.catList = []
    }

}

export default CatStore;
