
"use client"

import Header from "../components/inc_header";
import Footer from "../components/inc_footer";

import Swal from "sweetalert2";

import { useEffect, useState } from "react";
import axios from "axios";

import LoadingProcess from "../components/loadingProcess";

export default function Home() {
    const [loading, setLoading] = useState(true);
    const [cnt, setCnt] = useState(0);
    const [refModel, setRefModel] = useState(null);
    const [refImage, setRefImage] = useState('http://koraiaai.cafe24.com/koraia/news_logo.png');
    const [refId, setRefId] = useState(-1);

    const chgRefName = (e) => {
        refModel.map((data, index) => {
            if (e.target.value == index) {
                console.log(data.id)
                console.log(data.name)
                console.log(data.image)
                setRefImage(data.image)
                setRefId(data.id)
            }
        })
    }

    const messageClick = () => {
        Swal.fire({
            title : "에러!",
            text : "월요일 오픈예정!",
            icon : "error"
        })
    }

    function plusHandler() {
        setCnt(cnt+1)
    }

    // 서버에 reference 모델 정보 가져오는 함수
    const getRefModel = async () => {
        try {
            setLoading(true);
            const res = await axios.get('/v1/getmodellist')
            console.log(res.data.refModel)
            console.log(res.data.code)
            setRefModel(res.data.refModel)
            setLoading(false);

            if (res.data.code != 1) {
                Swal.fire({
                    title : "데이터 에러!",
                    text : "데이터 가져오기 실패",
                    icon : "error"
                })
            }
        } catch(e) {
            Swal.fire({
                title : "에러!",
                text : "서버에 데이터를 가져오는데 실패하였습니다.",
                icon : "error"
            })
        }
    }

    // 시작시 최초 한번 가동
    useEffect(() => {
        console.log("useEffect 실행")
        // axios 사용법
        getRefModel()
    }, []);

    return (
        <>
        <Header />

        {loading ? 
        <LoadingProcess />
        : 
        <section className="text-gray-600 body-font">
        <form action="http://localhost:8000/api/v1/sendimage/" method="post" encType="multipart/form-data">
        <input type="hidden" name="refId" value={refId} />
        <div className="container px-5 py-5 mx-auto">
            <div className="flex flex-wrap -mx-4 -mb-10 text-center">
            <div className="sm:w-1/2 mb-10 px-4">
                <div className="rounded-lg h-[450px] overflow-hidden">
                <img alt="content" className="object-cover object-center h-full w-full" src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202306/04/138bdfca-3e86-4c09-9632-d22df52a0484.jpg" />
                </div>
                <h2 className="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">내사진 업로드</h2>
                <div className="relative mb-4">
                    <input type="file" accept="image/png, image/gif, image/jpeg" name="myImage" className="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" />
                </div>
                <button type="submit" className="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">사진등록</button>
            </div>
            <div className="sm:w-1/2 mb-10 px-4">
                <div className="rounded-lg h-[450px] overflow-hidden">
                <img alt="content" className="object-cover object-center h-full w-full" src={refImage} />
                </div>
                <h2 className="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">화장모델</h2>
                <select onChange={chgRefName} name="model" id="lang" className="w-full h-[50px] bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
                {refModel.map((data, index) => (
                    <option value={index} key={data.id}>{data.name}</option>
                ))}
                </select>
                <button className="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">모델적용</button>
            </div>
            </div>
        </div>
        </form>
        </section>
        }

        

        <Footer />
        </>
    )
}