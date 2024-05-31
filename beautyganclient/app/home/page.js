import Footer from "../components/inc_footer"
import Header from "../components/inc_header"

export default function Home() {
	return (
		<>
			<Header />
			<section className="text-gray-600 body-font">
				<div className="container px-5 py-5 mx-auto">
					<div className="flex flex-wrap -mx-4 -mb-10 text-center">
						<div className="sm:w-1/2 mb-10 px-4">
							<div className="rounded-lg h-[450px] overflow-hidden">
								<img alt="content" className="object-cover object-center h-full w-full" src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202306/04/138bdfca-3e86-4c09-9632-d22df52a0484.jpg" />
							</div>
							<h2 className="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">내사진 업로드</h2>
							<div className="relative mb-4"><input type="file" id="name" name="name" className="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" /></div>
							<button href="image_result.html" className="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">사진등록</button>
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
