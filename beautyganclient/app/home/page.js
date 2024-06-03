
"use client"

import Footer from "../components/inc_footer"
import Header from "../components/inc_header"
import Swal from "sweetalert2"

import { useEffect, useState } from "react"
import axios from "axios"
import LoadingProcess from "../components/loadingprocess"

export default function Home() {

	const [loading, setLoading] = useState(true);
	const [cnt, setCnt] = useState(0);
	const [refModel, setRefModel] = useState(null);

	const messageClick = () => {
		// alert('test')
		Swal.fire({
			title: "Error",
			text: "서버에 데이터를 가져오는데 실패했습니다.",
			icon: "error"
		})
	}

	function plusHandler() {
		setCnt(cnt + 1)
	}

	// 서버에 reference 모델 정보 가져오는 함수
	const getRefModel = async () => {
		try {
			setLoading(true);
			const res = await axios.get('/v1/getmodellist') // const res = axios.get(url 정보)
			console.log(res.data.refModel)
			console.log(res.data.code)
			setRefModel(res.data.refModel)
			setLoading(false);


			if (res.data.code != 1) {
				Swal.fire({
					title: "Data Error",
					text: "데이터를 가져오는데 실패했습니다.",
					icon: "error"
				})
			}
		} catch (e) {
			Swal.fire({
				title: "Error",
				text: "서버에 데이터를 가져오는데 실패했습니다.",
				icon: "error"
			})
		}
	}

	// 시작시 최초 1번 가동
	useEffect(() => {
		console.log("useEffect 실행");
		// axios 사용법
		getRefModel()
	}, []);


	return (
		<>
			<Header />

			{loading ? <LoadingProcess />
			: 
			<section className="text-gray-600 body-font">
				<div className="container px-5 py-5 mx-auto">
					<div className="flex flex-wrap -mx-4 -mb-10 text-center">
						<div className="sm:w-1/2 mb-10 px-4">
							<div className="rounded-lg h-[450px] overflow-hidden">
								<img alt="content" className="object-cover object-center h-full w-full" src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202306/04/138bdfca-3e86-4c09-9632-d22df52a0484.jpg" />
							</div>
							<h2 className="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">내사진 업로드</h2>
							<div className="relative mb-4"><input type="file" id="name" name="name" className="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" /></div>
							<button onClick={messageClick} className="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">사진등록</button>
						</div>
						<div className="sm:w-1/2 mb-10 px-4">
							<div className="rounded-lg h-[450px] overflow-hidden">
								<img alt="content" className="object-cover object-center h-full w-full" src="https://ilyo.co.kr/contents/article/images/2022/1220/1671505705044397.jpg" />
							</div>
							<h2 className="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">화장모델</h2>
							<select name="model" id="lang" className="w-full h-[50px] bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
								<option value="모델">A모델</option>
								<option value="B모델">B모델</option>
							</select>
							<button className="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">모델적용</button>
						</div>
					</div>
				</div>
			</section>
			}

			{refModel ? "refModel = none" : "refModel = data"}
			
			카운터 : {cnt}
			<button onClick={plusHandler} className="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">카운터 증가</button>

			<section className="text-gray-600 body-font">
				<div className="container px-5 py-5 mx-auto">
					<div className="flex flex-wrap -mx-4 -mb-10 text-center">
						<div className="sm:w-1/2 mb-10 px-4">
							<div className="rounded-lg h-[450px] overflow-hidden">
								<img alt="content" className="object-cover object-center h-full w-full" src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202306/04/138bdfca-3e86-4c09-9632-d22df52a0484.jpg" />
							</div>
							<h2 className="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">내사진 업로드</h2>
							<div className="relative mb-4"><input type="file" id="name" name="name" className="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" /></div>
							<button onClick={messageClick} className="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">사진등록</button>
						</div>
						<div className="sm:w-1/2 mb-10 px-4">
							<div className="rounded-lg h-[450px] overflow-hidden">
								<img alt="content" className="object-cover object-center h-full w-full" src="https://ilyo.co.kr/contents/article/images/2022/1220/1671505705044397.jpg" />
							</div>
							<h2 className="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">화장모델</h2>
							<select name="model" id="lang" className="w-full h-[50px] bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
								<option value="모델">A모델</option>
								<option value="B모델">B모델</option>
							</select>
							<button className="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">모델적용</button>
						</div>
					</div>
				</div>
			</section>
			<Footer />
		</>
	)
}