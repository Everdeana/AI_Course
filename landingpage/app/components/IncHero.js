
"use client"

import { ReactTyped } from "react-typed"

export default function IncHero() {
	return(
		<div className="HERO text-white">
			{/* <div className="max-w-[800px] mt-[96px] w-full h-screen mx-auto text-center flex flex-col justify-center"></div> */}
			<div className="py-10 max-w-[800px] mt-[40px] w-full mx-auto text-center flex flex-col justify-center">
			<p className="text-[#354B46] font-bold p-2">병원에 가지 않아도 진단을 받을 수 있다!!!</p>
			<h1 className="md:text-6xl sm:text-5xl text-3xl font-bold md:py-6">질병 예측 서비스</h1>
			<div>
				<p className="md:text-4xl sm:text-3xl text-xl font-bold">
					<ReactTyped
					className=''
					strings = {['쉽고 빠른 진단 프로그램 다운로드 하세요!!', '새로운 서비스를 경험해보세요.', 'MedEase를 추천드려요.']}
					typeSpeed={100}
					backSpeed={60}
					loop
					/>
				</p>
			</div>
			<button className="bg-[#00df9a] w-[200px] rounded-md fint-medium my-6 mx-auto py-3 text-black">Get Start</button>
			</div>
		</div>
	)

}