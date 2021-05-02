import React, { useState, useEffect, useRef, useCallback } from "react";
import * as lib from "../../library/UIlibrary";
import styles from "./ListView.module.css";

export default function ListView(props) {
  const [yaxis, setYaxis] = useState(0);
  const [trigger, setTrigger] = useState(false);
  const loadingRef = useRef(null);

  useEffect(() => {
    props.fetchMethod();

    const observer = new IntersectionObserver(
      handleObserver, //callback
      { threshold: 0.7 }
    );
    const target = loadingRef.current;
    observer.observe(target);
    return () => observer && observer.disconnect();
  }, [yaxis]);

  useEffect(() => {
    if (yaxis < window.innerHeight) {
      props.fetchMethod();
    }
  });

  const handleObserver = useCallback((entities, options) => {
    const y = entities[0].boundingClientRect.y;
    setYaxis(y);
    if (yaxis > y) {
      props.fetchMethod();
    }
  }, []);

  const makeViewList = () => {
    const task = [...props.data];
    const result = [];
    while (task.length > 0) {
      result.push(task.splice(0, props.column));
    }
    return result;
  };
  //   console.log(yaxis < window.innerHeight);
  const list = makeViewList();
  return (
    <div className={styles.container}>
      <div className={styles.title}></div>
      <div className={styles.images}>
        {list.length > 0 &&
          list.map((elem, i) => (
            <div key={i} className={styles.doggies}>
              {elem.map((info, key) => (
                <div className={styles.doggiesImages_wrap} key={key}>
                  <img
                    onClick={() =>
                      lib.modalOpen(
                        <img src={info} style={{ maxWdith: "600px" }} />
                      )
                    }
                    src={info}
                    alt="dog"
                    // className={styles.dog}
                  />
                </div>
              ))}
            </div>
          ))}
      </div>
      <div ref={loadingRef}>
        <div>Loading</div>
      </div>
    </div>
  );
}
