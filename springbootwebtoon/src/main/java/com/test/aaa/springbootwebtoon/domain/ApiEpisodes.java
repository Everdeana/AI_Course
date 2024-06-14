package com.test.aaa.springbootwebtoon.domain;


import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ApiEpisodes {

    String id;
    String title;
    String thumb;
    String rating;
    String date;


    public ApiEpisodes(String id, String title, String thumb, String rating, String date) {
        this.id = id; // 외부에서 들어온 id값을 id에 복사해줌
        this.title = title;
        this.thumb = thumb;
        this.rating = rating;
        this.date = date;

    }
}
