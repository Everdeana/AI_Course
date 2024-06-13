package com.test.aaa.springbootwebtoon.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class WebToonController {
    @GetMapping("/")
    @ResponseBody
    public String Main() {
        return "스프링부트 로딩...";
    }

    @GetMapping("/home") // localhost:8080/home
    public String Home() {
        return "main";
    }

    @GetMapping("/detail") // localhost:8080/home
    public String Detail() {
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
