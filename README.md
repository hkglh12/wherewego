# wherewego

## Our Project consists of Frontend(android) - Backend(Python_Django Web Framework) model.
  ### Our projects service modeling follows...
    1. A user put a name of place (for ex. "상암동") at Frontend-App
    2. Choose one of his/her trip concept. like "chilling or best restaurant"
    3. those infos will be transfered to Backend
    4. Our Backend program finds places which is uploaded on Naver Blog post
       - this might be curious, why use Naver Blog posts? 
         - A : Some company, restaurant might pay for Ads. and we can't sure their infos, or scores.
               but we can trust real reviews, and the very easiest way to get those review is posts.
    5. Our BackEnd Program scores places, and returns some places got good score.
       - which means our project recommanding places
    6. Backend program returns places' coords. and Front will find places by that.



## Wrote at 17th.Aug.2019

### OnDevelop.

## Here is our project develop schedule.

1. Backend Develop will be started from 3rd.Sep.2019
2. Frontend Develop will be suspended until 15th.Sep.2019 but after that, it will get started developing 
   at the same time backend developing.
3. From 17.08.19 ~ 2nd.Sep.2019, We will develop our Internal Algorithm.

## Until now..

1. Backend isn't prepared at all including modeling, design for everything.
2. Frontend was suspeneded after importing google API. which is functional now.
3. In Source, Crawler code fully functional which is in "enhanced folder"
   - also, this code excludes some \t, \^ sort of things.

## Why Back, Frontend development suspended?

  *** From 17.Aug.2019 - to 2nd.Sep.2019, we will develop our internal Algorithm.
  - Which is scoring our results. 
    - If our Algorithm returns some name of restaurant, places, then it must be scored. which is good or not.
    - We are using TenserFlow, Pandas. 
    - It should be done or at least done by 50% until 2nd.Sep.2019. So we will work on it.
