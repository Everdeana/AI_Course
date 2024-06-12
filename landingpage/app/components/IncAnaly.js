
export default function IncAnaly() {
	return (
		<div className="ANALY">
			<div className="w-full px-4">
				<div className="max-w-[1240px] mx-auto grid md:grid-cols-2"> {/* md:grid-cols-2 : 컬럼 개수 */}
					<div className="p-10">
						<img src="/assets/image/medi.png" alt='.' />
					</div>
					<div className="flex flex-col justify-center">
						<h1 className="text-[#354B46] font-bold p-2">쉽게 내 병명을 예측하는 간편한 앱!!!</h1>
						<p className="p-2 md:text-5xl sm:text-4xl text-3xl font-bold md:py-6">맞춤형 질병 예측 프로그램</p>
						<p className="p-2">목 디스크를 낫게 하는 척추 위생 – 신전 자세<br />
							&nbsp;• 서거나 걸을 때 허리를 꼿꼿이 유지하기<br />
							&nbsp;• 스마트폰을 볼 경우, 무조건 높이 들기<br />
							&nbsp;• 모니터 높이 높이기<br />
							&nbsp;• 운전 중 요추 경추 전만 유지, 어깨 허리에 쿠션<br />
							&nbsp;• 자는 동안 경추 전만 유지 위해서 머리는 약간 뒤로 젖혀 주고<br />
							&nbsp;&nbsp;&nbsp;&nbsp;목을 받쳐 주는 푹신한 베개 사용, 바로 누워 자는 것을 가장 추천<br />
						</p>
						<button className="p-2 bg-black text-[#354B46] w-[200px] rounded-md font-medium my-6 mx-auto md:mx-0 py-3">Get Start</button>
					</div>
				</div>

			</div>
		</div>
	)
}