
// 선언 부분
import axios from 'axios';
import { createRequire } from 'module' 
const require = createRequire(import.meta.url);
const express = require('express') // import
const cors = require('cors')
const app = express() // var 사용 가능
const PORT = 4000 // PORT 4000번

// 웹에서 받은 정보 파싱 처리
app.use(express.urlencoded({ extended: true }))
app.use(express.json())
app.use(cors())

// // 웹 경로 지정
// // '/' -> root로 들어왔을 때 -> request(받은 값을), response(결과값으로 보냄)
// app.get('/', (req, res)=>{
// 	res.send('테스트...')
// }) 

const database = [];

async function getSD(content, sampler, sizeX, sizeY) {
	// stable diffusion에 보낼 정보  // 비동기로 보내지 않으면 죽어버림
	try {
		const diffusionPrompt = content
        let domainName = "SD Company"
        const negativePrompt = "EasyNegative, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans,extra fingers,fewer fingers,((watermark:2)),(white letters:1), (multi nipples), lowres, bad anatomy, bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worst quality, low qualitynormal quality, jpeg artifacts, signature, watermark, username,bad feet, {Multiple people},lowres,bad anatomy,bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worstquality, low quality, normal quality,jpegartifacts,signature, watermark, blurry,bad feet,cropped,poorly drawn hands,poorly drawn face,mutation,deformed,worst quality,low quality,normal quality,jpeg artifacts,signature,extra fingers,fewer digits,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,text,error,missing fingers,missing arms,missing legs,extra digit,"

		const request = await axios.post("http://211.216.177.2:7860/sdapi/v1/txt2img", { // 이 서버로 데이터를 보낼 때 CORS 포함해서 전송해야함
				prompt: diffusionPrompt,
				seed : -1, // random
				batch_size: 1,
				steps : 20, // 학습량 -> attention 사용하여 step 줄임(?)
				cfg_scale : 7, // 정보 70%
				width : sizeX, 
				height : sizeY,
				negative_prompt: negativePrompt,
				sampler_index : sampler
			 // await로 보내면
		});
		// console.log("getSD try end")
		// request로 받음
		// console.log('req = ' + request.data);

		let logoImage = await request.data.images;
		return { logoImage, domainName };
	} catch(err) {
		// console.log("getSD error")
		// console.log(error)
		console.error(err);
	}
}

// API 경로
app.post('/api', async (req, res) => {
	const { sampler } = req.body;
    const { sizeX } = req.body;
    const { sizeY } = req.body;
	const { prompt } = req.body;

    console.log('prompt = ' + prompt)
    console.log('sampler = ' + sampler)
    console.log('sizeX = ' + sizeX)
    console.log('sizeY = ' + sizeY)

	const result = await getSD(prompt, sampler, sizeX, sizeY);
	database.push(result);
	res.json({ message: "Retrieved successfully!", result: database });
	
	// const data = {
	// 	'id' : 1,
	// 	'name' : '장국진',
	// 	'tel' : '000-0000-0000'
	// }
	
	// res.send(data) // 데이터 전송
});

// 서버 가동
app.listen(PORT, () => {
	console.log(`Server listening on ${PORT}`);
});