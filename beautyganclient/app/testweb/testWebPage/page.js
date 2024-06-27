'use client'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { useData } from '../../context/DataContext'

export default function TestWebPage() {
    const { symptoms, prediction, setPrediction } = useData()
    const [loading, setLoading] = useState(true)
    const router = useRouter()

    useEffect(() => {
        const fetchPrediction = async () => {
            try {
                const response = await fetch('http://your-django-backend-url/predict/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ symptoms })
                })
                const data = await response.json()
                setPrediction(data)
            } catch (error) {
                console.error('Error fetching prediction:', error)
            } finally {
                setLoading(false)
            }
        }

        fetchPrediction()
    }, [symptoms, setPrediction])

    if (loading) {
        return <div>Loading...</div>
    }

    return (
        <div>
            <h1>Prediction Results</h1>
            <p>Predicted Disease: {prediction?.disease}</p>
            <p>Probability: {prediction?.probability}</p>
            {/* 추가 결과 표시... */}
        </div>
    )
}
