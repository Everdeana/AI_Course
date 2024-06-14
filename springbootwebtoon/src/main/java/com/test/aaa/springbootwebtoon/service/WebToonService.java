package com.test.aaa.springbootwebtoon.service;

import com.test.aaa.springbootwebtoon.domain.ApiEpisodes;
import com.test.aaa.springbootwebtoon.domain.ApiToday;
import lombok.RequiredArgsConstructor; // Lombok
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;


@RequiredArgsConstructor
@Service
public class WebToonService {

    // 서버에서 데이터 불러오기
    public ArrayList<ApiToday> ApiToday() {
        RestTemplate restTemplate = new RestTemplate(); // API 가져오기
        String url = "https://webtoon-crawler.nomadcoders.workers.dev/today";
        ResponseEntity<String> response = restTemplate.getForEntity( // Axios와 유사
                url, String.class
        );
        System.out.println("code = " + response.getStatusCode());
        System.out.println("data = " + response.getBody());

        // data 파일 처리 방법 - Json
        JSONArray jsonData = null;
        try {
            jsonData = new JSONArray(response.getBody());
        } catch (JSONException e) {
            throw new RuntimeException(e);
        }
        System.out.println("JSON Data = " + jsonData);

        // 배열에 적용
        ArrayList<ApiToday> todayData = new ArrayList<ApiToday>();
        // 데이터 가져오기
        String id;
        String title;
        String thumb;

        System.out.println("Total Data = " + jsonData.length());
        
        // ApiToday 배열에 삽입
        for(int i = 0; i < jsonData.length(); i++){
            // 객체 선언
            JSONObject obj = jsonData.getJSONObject(i);
            id = obj.getString("id");
            title = obj.getString("title");
            thumb = obj.getString("thumb");

            todayData.add(new ApiToday(id, title, thumb));

            System.out.println("id = " + id);
            System.out.println("title = " + title);
            System.out.println("thumb = " + thumb);
        }
        return todayData;
        
    }

    public ArrayList<ApiEpisodes> ApiEpisodeData(String eid) {
        RestTemplate restTemplate = new RestTemplate(); // API 가져오기
        String url = "https://webtoon-crawler.nomadcoders.workers.dev/" + eid + "/episodes";
        ResponseEntity<String> response = restTemplate.getForEntity( // Axios와 유사
                url, String.class
        );
        System.out.println("code = " + response.getStatusCode());
        System.out.println("data = " + response.getBody());

        // data 파일 처리 방법 - Json
        JSONArray jsonData = null;
        try {
            jsonData = new JSONArray(response.getBody());
        } catch (JSONException e) {
            throw new RuntimeException(e);
        }
        System.out.println("JSON Data = " + jsonData);

        // 배열에 적용
        ArrayList<ApiEpisodes> episodeData = new ArrayList<ApiEpisodes>();
        // 데이터 가져오기
        String id;
        String title;
        String thumb;
        String rating;
        String date;

        System.out.println("Total Data = " + jsonData.length());

        // ApiToday 배열에 삽입
        for(int i = 0; i < jsonData.length(); i++){
            // 객체 선언
            JSONObject obj = jsonData.getJSONObject(i);
            id = obj.getString("id");
            title = obj.getString("title");
            thumb = obj.getString("thumb");
            rating = obj.getString("rating");
            date = obj.getString("date");

            episodeData.add(new ApiEpisodes(id, title, thumb, rating, date));

            System.out.println("id = " + id);
            System.out.println("title = " + title);
            System.out.println("thumb = " + thumb);
            System.out.println("rating = " + rating);
            System.out.println("date = " + date);
        }
        return episodeData;
    }
}
