import React, { useState, useEffect, useRef, useCallback } from "react";
import * as lib from "../../library/UIlibrary";
import styles from "./ListView.module.css";
import { observer } from "mobx-react";

function ListView(props) {
  const loadingRef = useRef(null);

  useEffect(() => {
    // fetch for the first time to fill out all screen
    props.fetchMethod();
    props.fetchMethod();
  }, [])

   const handleObserver = useCallback((entries) => {
     const target = entries[0];
     // fetch only target is currently intersecting
     if (target.isIntersecting) {
       props.fetchMethod();
     }
   }, [props.fetchMethod()])

  useEffect(() => {
    const observer = new IntersectionObserver(
      handleObserver, //callback
      { threshold: 1 }
    );
    const target = loadingRef.current;
    observer.observe(target);
    // unobserve
    return () => observer.unobserve(loadingRef.current);
  }, [loadingRef]);

  const makeViewList = () => {
    const task = [...props.data];
    const result = [];
    while (task.length > 0) {
      result.push(task.splice(0, props.column));
    }
    return result;
  };

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

export default observer(ListView)
