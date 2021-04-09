import { observable, action, flow, makeObservable } from 'mobx';

class CatStore {

    constructor() {
        makeObservable(this,{
            catList: observable,
            fetchCat: action
        })
    }

    catList = []

    fetchCat = flow(function* (page) {

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

}

export default CatStore;
