<template>
  <div>
    <Header></Header>
    <div class="background_picture section breadcrumb-section overlay" data-bg-image="../assets/images/work/opera1.jpg">
      <div class="container">
        <div class="row">
          <div class="col-12">

            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos="fade-up" data-aos-duration="1100">山西戏剧</h1>

              <ul class="breadcrumb-menu" data-aos="fade-up" data-aos-duration="1500">

                <li>
                  <span>Shanxi Opera</span>
                </li>
              </ul>
            </div>
            <!-- Breadcrumb wrapper End -->

          </div>
        </div>
      </div>
    </div>
    <!-- Breadcrumb Section End -->

    <!-- Blog Grid Section Start -->
    <div class="section section-margin">
      <div class="container">

        <div class="row">
          <div class="col-lg-8 m-auto p-lg-0">
            <div class="blog-details-wrapper">
              <div class="blog-details-image m-b-40" data-aos="fade-up" data-aos-duration="1100">
                <img class="img-circle img-shadow" src="../assets/images/work/opera2.jpg" alt="Blog Details">
              </div>

              <h2 class="blog-details-title m-b-20" data-aos="fade-up" data-aos-duration="1300">山西戏曲</h2>
              <p class="text" data-aos="fade-up" data-aos-duration="1100">
                受道教影响，道情戏是山西戏曲中独特的剧种，从南到北有四处：永济道情（又称河东道情）、洪洞道情、临县道情、晋北道情，其中晋北道情分布面广，分布于雁北与忻州的干旱的高原山区。道情一般多分布于远离中心城市偏远的山区。但洪洞道情除外，其分布于地理条件好的汾河下游的平川。</p>
              <p class="text" data-aos="fade-up" data-aos-duration="1100">
                道情源于道教音乐，这一历史渊源，使它在萌芽时期就走上了“唱情”之路。戏曲道情承袭道家“唱情”的特征，突出地表现在虚词（衬字、助）、衬腔（拖腔）的广泛运用上。山西道情戏与当地的语言音调结合，形成了道情戏独特的声腔音韵风格。</p>

              <div class="blog-content-image m-t-40 m-b-n50">
                <div class="blog-content-thumb m-b-50" data-aos="fade-up" data-aos-duration="1400">
                  <img class="img-circle img-shadow" src="../assets/images/work/opera3.jpg" alt="">
                </div>
                <div class="blog-content m-b-50" data-aos="fade-up" data-aos-duration="1600">
                  <p>
                    在道藏中有大量的诗词为历代道中高人的抒情之作，全真道王重阳“尤长于以诗词劝诱士人”川（仅王重阳一人的词曲载入道藏的就达300首之多）。其歌咏的词曲的最大的特点在于増加了虚词衬字：“哎、啊、哪、呀、吧”等虚词村字，多拖腔。虚字衬词的添加是为了直抒“迢远之意”，也为了“徐徐吟咏”，极具艺术特色。声情效果，唱奏交替，有起有落，相互衬托，浑然天成。戏曲道情所要传达的“情”就通过这种形式充分表达出来。</p>
                  <p>
                    道情用词比较典雅。西路道情以韩阳为代表，包括辛店、王店、双店、盘底等村，群众又叫它为韩阳道情。这些艺人多在黄河两岸演出，吸收了当地的语言艺术，在一定程度上受秦曲、眉户的影响，伴奏以三义板击拍为主，旋律缠绵，幽雅动听，具有抒情味。</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Footer class="foot"></Footer>
    </div>
    <!-- Blog Grid Section End -->

  </div>

</template>

<script>
import Header from "../components/header";
import Footer from "../components/ShanxiFooter";

export default {
  name: "ShanxiOpera",
  components: {
    Header,
    Footer,
  },
}
</script>


<style scoped>
.foot {
  margin-top: 220px;
}

.background_picture {
  height: 618px;
  background: url(../assets/images/work/opera1.jpg);
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  overflow: hidden;
  /*background-image: linear-gradient(to right, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);*/
}

.breadcrumb-section {
  height: 650px;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
}

.section, .section-fluid {
  float: left;
  width: 100%;
}

.overlay {
  position: relative;
}

.overlay::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1;
  background: linear-gradient(to right, rgba(20, 20, 20, 0.8) 0%, rgba(20, 20, 20, 0.8) 0%);
}

.container {
  max-width: 1200px;
  padding-right: var(--bs-gutter-x, 15px);
  padding-left: var(--bs-gutter-x, 15px);
  width: 100%;
  margin-right: auto;
  margin-left: auto;
}

.row {
  --bs-gutter-x: 30px;
  --bs-gutter-y: 0;
  display: flex;
  flex-wrap: wrap;
  margin-top: calc(var(--bs-gutter-y) * -1);
  margin-right: calc(var(--bs-gutter-x) / -2);
  margin-left: calc(var(--bs-gutter-x) / -2);
}

.col-12 {
  flex: 0 0 auto;
  width: 100%;
}

.row > * {
  flex-shrink: 0;
  width: 100%;
  max-width: 100%;
  padding-right: calc(var(--bs-gutter-x) / 2);
  padding-left: calc(var(--bs-gutter-x) / 2);
  margin-top: var(--bs-gutter-y);
}

.breadcrumb-wrapper {
  text-align: center;
  position: relative;
  z-index: 99;
  padding-top: 40px;
}

.breadcrumb-wrapper .title {
  font-weight: 400;
  font-size: 56px;
  margin-bottom: 0;
}

.text-white {
  color: #fff !important;
}

h1, h2, h3, h4, h5, h6 {
  font-family: "Vidaloka", serif;
  font-weight: 600;
  line-height: 1.2;
  color: #232324;
}

.breadcrumb-wrapper .breadcrumb-menu {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  margin-top: 30px;
}

ul {
  margin: 0;
  padding: 0;
}

ul li {
  list-style: none;
}

.breadcrumb-wrapper .breadcrumb-menu li span {
  color: #ffffff;
  font-size: 16px;
}

.section-margin {
  margin-top: 120px;
  margin-bottom: 0px;
}

.section, .section-fluid {
  float: left;
  width: 100%;
}

.container {
  padding-right: var(--bs-gutter-x, 15px);
  padding-left: var(--bs-gutter-x, 15px);
}

.row {
  --bs-gutter-x: 1.5rem;
  --bs-gutter-y: 0;
  display: flex;
  flex-wrap: wrap;
  margin-top: calc(var(--bs-gutter-y) * -1);
  margin-right: calc(var(--bs-gutter-x) / -2);
  margin-left: calc(var(--bs-gutter-x) / -2);
}

h2 {
  font-family: "Vidaloka", serif;
  font-weight: 600;
  line-height: 1.2;
  color: #232324;
  font-size: 36px;
}

.p-lg-0 {
  padding: 0 !important;
}

.m-auto {
  margin: auto !important;
}

.col-lg-8 {
  flex: 0 0 auto;
  width: 66.6666666667%;
}

.m-b-40 {
  margin-bottom: 40px;
}

.img-shadow {
  box-shadow: #959ea5 0px 0px 41px;
}

.img-circle {
  border-radius: 50px;
}

img {
  max-width: 100%;
}

img, svg {
  vertical-align: middle;
}

p {
  margin-top: 0;
  margin-bottom: 1rem;
  text-align: left;
}

.blog-details-wrapper .blog-content-image {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
}

.m-b-n50 {
  margin-bottom: -50px;
}

.m-t-40 {
  margin-top: 40px;
}

.blog-details-wrapper .blog-content-image .blog-content-thumb {
  margin-right: 40px;
  width: 360px;
}

.blog-details-wrapper .blog-content-image .blog-content-thumb img {
  max-width: 100%;
  width: 100%;
  display: block;
}

.blog-details-wrapper .blog-content-image .blog-content {
  width: calc(100% - 360px);
}

.blog-details-wrapper p {
  color: #4f4f4f;
  font-family: "Montserrat", sans-serif;
  font-size: 14px;
  line-height: 2;
  visibility: visible;
}
</style>
