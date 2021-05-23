import React, { useState } from 'react'
import { modalOpen } from '../../library/UIlibrary';
import styles from './SignUp.module.css'
import { Login } from '../'

const SignUp = (props) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');

    const passwordCheck = password2 === password

    const emailRegExp = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;

    const isValidEmail = email.match(emailRegExp)
    

    return (
        <div className={styles.signup}>
            <h2>SignUp</h2>
            <div className={styles.signup_input}>
                <input type="text" placeholder="email을 입력해주세요" onChange={(e)=>setEmail(e.target.value)}/>
                { email && !isValidEmail ? <span>올바른 형태의 이메일을 입력해주세요</span> : null}

                <input type="password" placeholder="password를 입력해주세요" onChange={(e)=>setPassword(e.target.value)}/>
                <input type="password" placeholder="password를 다시 입력해주세요" onChange={(e)=>setPassword2(e.target.value)}/>
                {password === password2 ? null : <span>비밀번호가 일치하지 않습니다</span>}
            </div>
            <div className={styles.button_wrap}>
                <button onClick={props.SignUpHandler}>회원가입</button>
            </div>
            <div className={styles.button_wrap}>
                <button
                    style={{ backgroundColor: "#ccc" }}
                    onClick={()=>modalOpen(<Login/>)}
                >로그인하러가기</button>
            </div>
        </div>
    )
}

export default SignUp;