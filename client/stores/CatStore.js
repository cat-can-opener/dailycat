import { observable, action, flow, makeObservable } from 'mobx';

class CatStore {

    constructor() {
        makeObservable(this,{
            list: observable,
            fetchCat: action,
            removeCatList: action
        })
    }

    url = process.env.BASE_URL
    endPoint = "/cat"

    list = []

    fetchCat = flow(function* (page) {
        console.log(url, endPoint)
        const call = function(params) {
            return fetch(`https://dog.ceo/api/breeds/image/random/${params}`)
        }

        try {
            const res = yield call(page)
            if(res.status === "success"){
                catList.concat(res.message)
                return catList
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
