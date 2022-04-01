# CeneoScraper

### Struktura opinii w serwisie [Ceneo] https://www.ceneo.pl/) ###

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|||
|indentyfikator opinii|div.js_product-review\
["data-entry-id"\]|||
|autor opinii|span.user-post__author-name|||
|rekomendacja|span.user-post__author-recomendation > 
em|||
|liczba gwiazdek|span.user-post__score-count|||
|tresc opinii|div.user-post__text|||
|lista zalet|div[class$="positives"] ~ div.reviews-feature__item|||
|lista wad|div[class$="negatives"] ~ div.reviews-feature__item|||
|dla ilu osób przydatne|span[id^=votes-yes"] button.vote-yes > span <br> data-total-yes["data-total-vote"]|||
|dla ilu osób nieprzydatne|span[id^=votes-no"] button.vote-no > span <br> data-total-no["data-total-vote"]|||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|||
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|||