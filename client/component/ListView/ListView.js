import React, { useState, useEffect, useRef, useCallback } from 'react';
import styles from './ListView.module.css';

const PAGE_NUMBER = 9;

export default function ListView(props) {
	const [state, setState] = useState([]);
	// const [page, setPage] = useState(PAGE_NUMBER);
	const [yaxis, setYaxis] = useState(0);
	const [count, setCount] = useState(0);
	const loadingRef = useRef(null);

	// useEffect(
	// 	() => {
	// 		fetch(`https://dog.ceo/api/breeds/image/random/${page}`)
	// 			.then((res) => res.json())
	// 			.then((json) => setState(state.concat(json.message)));
	// 	},
	// 	[page]
	// );

	const fetchImage = () => {
		console.log('fetch image called')
		fetch(`https://dog.ceo/api/breeds/image/random/${PAGE_NUMBER}`)
			.then((res) => res.json())
			.then((json) => setState(state.concat(json.message)));
	}

	// const scrollToEnd = () => {
	// 	setPage(page + 1);
	// };

	// const handleObserver = (entities, options) => {
	// 	const y = entities[0].boundingClientRect.y;
	// 	console.log('handleobserver start')
	// 	console.log(y)
	// 	console.log(yaxis)
	// 	console.log(state)
	// 	setYaxis(y);
	// 	if (yaxis > y) {
	// 		console.log('handleobserver work')
	// 		fetchImage();
	// 		// const lastUser = this.state.users[this.state.users.length - 1];
	// 		// this.getUsers(curPage);
	// 		// this.setState({ page: curPage });
	// 	}
	// 	setYaxis(y);
	// }

	const handleObserver = useCallback(
		(entities, options) => {
			console.log('Click happened');
			const y = entities[0].boundingClientRect.y;
			console.log(y)
			console.log(yaxis)
			console.log(state)
			if (yaxis > y) {
				fetchImage();
			}
			setYaxis(y);
			console.log(yaxis)
		},
		[], // Tells React to memoize regardless of arguments.
	);

	useEffect(() => {
		console.log('first time')
		fetchImage();
		var options = {
			root: null, // Page as root
			rootMargin: "0px",
			threshold: 1.0
		};
		const observer = new IntersectionObserver(
			handleObserver, //callback
			options
		);
		const target = loadingRef.current;
		observer.observe(target);
		console.log(observer)
		console.log(target)
	}, [])

	// useEffect(() => {
	// 	window.onscroll = function () {
	// 		// 페이지가 bottom까지 scroll됐는지 체크!!
	// 		console.log(window.pageYOffset, document.documentElement.scrollTop, document.documentElement.scrollHeight);
	// 		scrollToEnd();
	// 		if (
	// 			window.pageYOffset + document.documentElement.scrollTop >=
	// 			document.documentElement.scrollHeight - 100
	// 		) {
	// 			// scrollToEnd();
	// 			fetchImage();
	// 			return
	// 		}
	// 	};
	// });

	const makeViewList = () => {
		const task = [...state];
		const result = [];
		while (task.length > 0) {
			result.push(task.splice(0, props.column));
		}
		return result;
	};

	const list = makeViewList();

	return (
		<div className={styles.container}>
			<div className={styles.title}>
				<div>
					My <span>Page</span>
				</div>
				{/* <img src="/images/dog.jpg" alt="cat"/>   */}
			</div>
			<button onClick={fetchImage}>fetch image</button>
			<button onClick={() => setYaxis(yaxis + 1)}>add yaxis</button>
			<p className={styles.sentence}>You've liked…</p>
			<div className={styles.images}>
				{list.length > 0 &&
					list.map((elem, i) => (
						<div key={i} className={styles.doggies}>
							{elem.map((info, key) => (
								<div className={styles.doggiesImage}>
									<img style={{ width: '300px' }} src={info} key={key} alt="dog" className={styles.dog} />
								</div>
							))}
						</div>
					))}
			</div>
			<div
				ref={loadingRef}
			>
				<div>Loading</div>
			</div>
		</div>
	);
}