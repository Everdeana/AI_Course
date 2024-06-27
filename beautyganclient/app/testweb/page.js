'use client'

import { useRouter } from 'next/navigation'
import { useState } from 'react'
import { useData } from '../context/DataContext'

export default function TestWebPage() {
    const router = useRouter()
    const { setSymptoms } = useData()
    const [inputValues, setInputValues] = useState([])

    const handleCheckboxChange = (event) => {
        const value = event.target.value;
        setInputValues(prev =>
            prev.includes(value) ? prev.filter(v => v !== value) : [...prev, value]
        );
    };

    const handleClick = () => {
        setSymptoms(inputValues)
        router.push('/testweb/testWebPage')
    }

    return (
        <div>
            <h1>Test Web Page</h1>
            <form>
                {/* 여러 증상들에 대한 체크박스를 나열 */}
                <label>
                    <input type="checkbox" value="symptom1" onChange={handleCheckboxChange} /> Symptom 1
                </label>
                <label>
                    <input type="checkbox" value="symptom2" onChange={handleCheckboxChange} /> Symptom 2
                </label>
                {/* 추가 증상들... */}
                <button type="button" onClick={handleClick}>Go to Another Page</button>
            </form>
        </div>
    )
}
