import Footer from "../components/inc_footer"
import Header from "../components/inc_header"
export default function Result() {
	return (
		<>
			<Header />
			<section className="text-gray-600 body-font">
				<div className="container px-5 py-10 mx-auto">
					<div className="flex flex-wrap -m-4">
						<div className="lg:w-1/3 lg:mb-0 mb-6 p-4">
							<div className="h-full text-center">
								<img alt="testimonial" className="w-80 h-80 mb-8 object-cover object-center rounded-full inline-block border-2 border-gray-200 bg-gray-100" src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202306/04/138bdfca-3e86-4c09-9632-d22df52a0484.jpg" />
									<p className="leading-relaxed">하루에 한 번 얼굴을 씻어주세요. 매일 아침 혹은 밤에 클렌저로 얼굴을 닦아준다면 좋습니다.
										피부 타입에 맞는 클렌저를 해주세요. 지성 피부용, 중성 피부용, 건성 피부용 등 다양한 제품이 있습니다.</p>
									<span className="inline-block h-1 w-10 rounded bg-indigo-500 mt-6 mb-4"></span>
									<h2 className="text-gray-900 font-medium title-font tracking-wider text-sm">ChatGPT 3.5 Turbo</h2>
									<p className="text-gray-500">LangChain</p>
							</div>
						</div>
						<div className="lg:w-1/3 lg:mb-0 mb-6 p-4">
							<div className="h-full text-center">
								<img alt="testimonial" className="w-80 h-80 mb-8 object-cover object-center rounded-full inline-block border-2 border-gray-200 bg-gray-100" src="https://ilyo.co.kr/contents/article/images/2022/1220/1671505705044397.jpg" />
									<p className="leading-relaxed">일반적으로 선홍빛의 피부색과 잡티, 주름이 없는 매끄러운 피부는 건강한 피부로 간주됩니다. 피부 상태를 유지하기 위해 적절한 관리와 스킨케어를 지속하시면 좋을 것 같아요!</p>
									<span className="inline-block h-1 w-10 rounded bg-indigo-500 mt-6 mb-4"></span>
									<h2 className="text-gray-900 font-medium title-font tracking-wider text-sm">모델 장원영</h2>
									<p className="text-gray-500"><a href="https://www.amoremall.com/kr/ko/product/detail?onlineProdSn=57027&onlineProdCode=131170000186" target="_blank">재품 상세 정보</a></p>
							</div>
						</div>
						<div className="lg:w-1/3 lg:mb-0 p-4">
							<div className="h-full text-center">
								<img alt="testimonial" className="w-80 h-80 mb-8 object-cover object-center rounded-full inline-block border-2 border-gray-200 bg-gray-100" src="https://img.khan.co.kr/news/2023/05/12/news-p.v1.20230512.e5fffd99806f4dcabd8426d52788f51a_P1.png" />
									<p className="leading-relaxed">
										피부 상태를 개선하려면 물과 보습을 충분히 섭취하고, 선크림을 사용하세요. 이러한 기본적인 습관을 지키면 피부 건강을 유지할 수 있습니다.
									</p>
									<span className="inline-block h-1 w-10 rounded bg-indigo-500 mt-6 mb-4"></span>
									<h2 className="text-gray-900 font-medium title-font tracking-wider text-sm">AI 분석결과</h2>
									<p className="text-gray-500">LangChain</p>
							</div>
						</div>
					</div>
				</div>
			</section>
			<Footer />
		</>
	)
}