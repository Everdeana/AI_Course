"use client"
import { ReactTyped } from "react-typed"

export default function IncHero() {
    return(
        <div className="HERO text-white">
            <div className="py-10 max-w-[800px] mt-[40px] w-full mx-auto text-center flex flex-col justify-center">
                <p className="text-[#00df9a] font-bold p-2">쉽게 약값을 줄이는 간편한 앱!!!</p>
                <h1 className="md:text-6xl sm:text-5xl text-3xl font-bold md:py-6">맞춤형 약값 견적프로그램</h1>
                <div>
                    <p className="md:text-4xl sm:text-3xl text-xl font-bold">
                        <ReactTyped
                        className=''
                        strings={[
                            '쉽고 간편 약값 견적프로그램 다운로드 하세요.',
                            '새로운 서비스를 경험해보세요.',
                            'AITECH3를 추천드려요.',
                            '6월말일까지 30% 할인행사 합니다.'
                        ]}
                        typeSpeed={80}
                        backSpeed={80}
                        loop
                        />
                    </p>
                </div>
                <button className="bg-[#00df9a] w-[200px] rounded-md font-medium my-6 mx-auto py-3 text-black">Get Start</button>
            </div>
        </div>
    )
}