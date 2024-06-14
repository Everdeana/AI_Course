package com.test.aaa.springbootwebtoon.controller;

import com.test.aaa.springbootwebtoon.domain.ApiEpisodes;
import com.test.aaa.springbootwebtoon.domain.ApiToday;
import com.test.aaa.springbootwebtoon.service.WebToonService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.ArrayList;

@Controller
public class WebToonController {

    // 클래스 연결 선언
    private WebToonService webtoonService;

    public WebToonController(WebToonService webtoonService){
        this.webtoonService = webtoonService;
    }

    @GetMapping("/")
    @ResponseBody
    public String Main() {
        return "스프링부트 로딩...";
    }

    @GetMapping("/home") // localhost:8080/home
    public String Home(Model model) {
        ArrayList<ApiToday> todayData = webtoonService.ApiToday();
        /*webtoonService.ApiToday();*/

        // 받은 데이터 확인
        System.out.println("................Controller Get Data.....................");
        for(ApiToday data : todayData) {
            System.out.println("get Data id = " + data.getId());
            System.out.println("get Data title = " + data.getTitle());
            System.out.println("get Data thumb = " + data.getThumb());

        }
        // 모델 데이터를 홈페이지에 적용
        model.addAttribute("today", todayData);

        return "main";
    }

    @GetMapping("/detail/{id}") // localhost:8080/home
    public String Detail(@PathVariable("id") String id, Model model) { // 파라미터의 값을 id로 인식
        System.out.println("ID = " + id);
        ArrayList<ApiEpisodes> episodeData = webtoonService.ApiEpisodeData(id);

        model.addAttribute("detail", episodeData);
        model.addAttribute("eid", id);
        return "detail";
    }

    @GetMapping("/mypage") // localhost:8080/home
    public String Mypage() {
        return "mypage";
    }

    @GetMapping("/login") // localhost:8080/home
    public String Login() {
        return "login";
    }

    @GetMapping("/signup") // localhost:8080/home
    public String Signup() {
        return "signup";
    }


}
