package com.test.aaa.springbootwebtoon.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WebToonApiController {
    @GetMapping("/api/ver")
    public String main() {
        return "{'API Version' : '1.2'}";
    }
}
