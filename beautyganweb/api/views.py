from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# 장고 파일 처리
from django.core.files.storage import FileSystemStorage

# 인공지능 파일
from beautygan_lib import makeup

# 직접 생성한 Model 사용 -> Table 사용
# QuerySet
from .models import RefModels

# Create your views here.
def api_index(request):
    return HttpResponse("ChicBytes API v1.0")

@csrf_exempt
def api_getmodellist(request):
    print("getmodelist")
    # DB
	# select * from api_refmodels
    datas = RefModels.objects.all()

    sendData = []

    for data in datas:
        # print(data)
        sendData.append({
            "id" : data.id,
            "name" : data.names,
            "image" : data.image,
            "item" : data.item,
            "shop" : data.shop,
            "doc" : data.doc,
            # "dates" : data.dates
        })

    data = {
        "refModel" : sendData,
        "code" : 1,
    }

    return JsonResponse(
        data, 
        safe=False, 
        json_dumps_params={'ensure_ascii':False},
        status=200
        )

@csrf_exempt
def api_sendimage(request):
    # 변수
    org_img = ''
    ref_img = './media/ref/1.jpg'

    # html 파일
    if request.method != 'POST':
        return HttpResponse("잘못된 정보입니다.")
    
    refId = request.POST.get('refId', '')

    # 이미지 파일 처리 경로 설정
    fs = FileSystemStorage(
        location=f'media/source', 
        base_url=f'media/source')
    
    # 파일 받아오기
    try:
        myImage = request.FILES['myImage']
        print("파일이름 : ", myImage.name)
        # 파일저장
        save_file = fs.save(myImage.name, myImage)
        print("save_file = ", save_file)
        org_img = './media/source/' + save_file
    except:
        print("error")

    # 인공지능 처리구현
    rst_img = makeup(org_img, ref_img)
    print("생성된 결과 : ", rst_img)

    send_org = "http://localhost:8000" + org_img.split(".")[1] + "." + org_img.split(".")[2]
    send_ref = "http://localhost:8000" + ref_img.split(".")[1] + "." + ref_img.split(".")[2]
    send_rst = "http://localhost:8000" + rst_img.split(".")[1] + "." + rst_img.split(".")[2]


    url = f'http://localhost:11000/result?org={send_org}&ref={send_ref}&rst={send_rst}'

    return redirect(url)
def api_index2(request):
    return HttpResponse("ChicBytes API v2.0")
