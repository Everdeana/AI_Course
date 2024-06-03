"use client"

import Header from "../components/inc_header";
import Footer from "../components/inc_footer";
import { useSearchParams } from "next/navigation";

export default function Result() {
    const params = useSearchParams();
    const orgImg = params.get('org');
    const refImg = params.get('ref');
    const rstImg = params.get('rst');

    console.log("orgImg =" + orgImg)
    console.log("refImg =" + refImg)
    console.log("rstImg =" + rstImg)

    return (
        <>
        <Header />

        <section class="text-gray-600 body-font">
        <div class="container px-5 py-10 mx-auto">
            <div class="flex flex-wrap -m-4">
            <div class="lg:w-1/3 lg:mb-0 mb-6 p-4">
                <div class="h-full text-center">
                <img alt="testimonial" class="w-80 h-80 mb-8 object-cover object-center rounded-full inline-block border-2 border-gray-200 bg-gray-100" src={orgImg} />
                <p class="leading-relaxed">하루에 한 번 얼굴을 씻어주세요. 매일 아침 혹은 밤에 클렌저로 얼굴을 닦아준다면 좋습니다.
                    피부 타입에 맞는 클렌저를 해주세요. 지성 피부용, 중성 피부용, 건성 피부용 등 다양한 제품이 있습니다.</p>
                <span class="inline-block h-1 w-10 rounded bg-indigo-500 mt-6 mb-4"></span>
                <h2 class="text-gray-900 font-medium title-font tracking-wider text-sm">ChatGPT 3.5 Turbo</h2>
                <p class="text-gray-500">LangChain</p>
                </div>
            </div>
            <div class="lg:w-1/3 lg:mb-0 mb-6 p-4">
                <div class="h-full text-center">
                <img alt="testimonial" class="w-80 h-80 mb-8 object-cover object-center rounded-full inline-block border-2 border-gray-200 bg-gray-100" src={refImg} />
                <p class="leading-relaxed">일반적으로 선홍빛의 피부색과 잡티, 주름이 없는 매끄러운 피부는 건강한 피부로 간주됩니다. 피부 상태를 유지하기 위해 적절한 관리와 스킨케어를 지속하시면 좋을 것 같아요!</p>
                <span class="inline-block h-1 w-10 rounded bg-indigo-500 mt-6 mb-4"></span>
                <h2 class="text-gray-900 font-medium title-font tracking-wider text-sm">모델 장원영</h2>
                <p class="text-gray-500"><a href="https://www.amoremall.com/kr/ko/product/detail?onlineProdSn=57027&onlineProdCode=131170000186" target="_blank">재품 상세 정보</a></p>
                </div>
            </div>
            <div class="lg:w-1/3 lg:mb-0 p-4">
                <div class="h-full text-center">
                <img alt="testimonial" class="w-80 h-80 mb-8 object-cover object-center rounded-full inline-block border-2 border-gray-200 bg-gray-100" src={rstImg} />
                <p class="leading-relaxed">
                    피부 상태를 개선하려면 물과 보습을 충분히 섭취하고, 선크림을 사용하세요. 이러한 기본적인 습관을 지키면 피부 건강을 유지할 수 있습니다.
                    </p>
                <span class="inline-block h-1 w-10 rounded bg-indigo-500 mt-6 mb-4"></span>
                <h2 class="text-gray-900 font-medium title-font tracking-wider text-sm">AI 분석결과</h2>
                <p class="text-gray-500">LangChain</p>
                </div>
            </div>
            </div>
        </div>
        </section>

        <Footer />
        </>
    )
}