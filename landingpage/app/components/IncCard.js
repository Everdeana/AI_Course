
export default function IncCard() {
	return (
		<div className="CARD">
			<div className="w-full py-[10rem] px-4 bg-white">
				<div className="max-w-[1240px] mx-auto grid grid-cols-3 gap-8">
					<div className="w-full shadow-xl flex flex-col p-4 my-4 rounded-lg hover:scale-105 duration-300">
                        <img className="w-20 mx-auto mt-[-3rem] bg-white" src="/assets/image/atm_card.png" />
                        <h2 className="text-2xl font-bold text-center py-8">무료회원</h2>
                        <p className="text-2xl font-bold text-center">0원</p>
                        <div className="text-center font-medium">
                            <p className="py-2 border-b mx-8 mt-8">무제한 사용가능</p>
                            <p className="py-2 border-b mx-8">1명만 사용가능</p>
                            <p className="py-2 border-b mx-8">최대 1G</p>
                        </div>
                        <button className="bg-[#00df9a] w-[200px] rounded-md font-medium my-6 mx-auto py-3">가입하기</button>
                    </div>
					<p1>1</p1>
					<p1>2</p1>
				</div>
			</div>
		</div>
	)
}