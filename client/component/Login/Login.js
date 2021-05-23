import React, { useState } from 'react'
import { modalOpen } from '../../library/UIlibrary';
import styles from './Login.module.css'
import { SignUp } from '../'

const Login = (props) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    return (
        <div className={styles.login}>
            <h2>Login</h2>
            <div className={styles.login_input}>
                <input type="text" placeholder="email을 입력해주세요" onChange={(e)=>setEmail(e.target.value)}/>
                <input type="password" placeholder="password를 입력해주세요" onChange={(e)=>setPassword(e.target.value)}/>
            </div>
            <div className={styles.button_wrap}>
                <button onClick={props.LoginHandler}>로그인</button>
            </div>
            <div className={styles.button_wrap}>
                <button
                    style={{ backgroundColor: "#ccc" }}
                    onClick={()=>modalOpen(<SignUp />)}
                >회원가입</button>
            </div>
        </div>
    )
}

export default Login;