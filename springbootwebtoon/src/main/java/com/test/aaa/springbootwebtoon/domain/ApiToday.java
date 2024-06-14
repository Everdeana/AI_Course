package com.test.aaa.springbootwebtoon.domain;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ApiToday {
    String id;
    String title;
    String thumb;

    public ApiToday(String id, String title, String thumb) {
        this.id = id; // 외부에서 들어온 id값을 id에 복사해줌
        this.title = title;
        this.thumb = thumb;

    }

    /* Old Version
    public String getId() {
        return this.id;
    }

    public void setId(String data) {
        this.id = data;
    }*/
}