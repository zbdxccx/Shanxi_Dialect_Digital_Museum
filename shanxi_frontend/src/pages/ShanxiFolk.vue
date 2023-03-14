<template>
  <div>
    <Header class="head"></Header>
    <!-- Breadcrumb Section Start -->
    <div class="background_picture overlay">
      <div class="container" style="background:url(../assets/images/work/mfolk1.jpg);">
        <div class="row">
          <div class="col-12">

            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos-duration="1100">山西民俗</h1>

              <ul class="breadcrumb-menu" data-aos-duration="1500">
                <li>
                  <span>Shanxi Folk</span>
                </li>
              </ul>
            </div>
            <!-- Breadcrumb wrapper End -->

          </div>
        </div>
      </div>
    </div>


    <!-- Breadcrumb Section End -->

    <!-- About Section Start -->
    <div class="section section-margin">
      <div class="container1">
        <div class="row m-b-n30">
          <div class="col-lg-6 align-self-center m-b-30" data-aos="fade-up" data-aos-duration="1100">
            <div class="about-content">
              <h2 class="title m-b-40">山西民俗</h2>
              <p>
                山西民俗，是指在物质文化与制度文化基础上形成的有关意识形态方面的民俗。它是人类在认识和改造自然与社会过程中形成的心理经验，这种经验一旦形成为集体的理习惯，并表现为特定的行为方式并世化传承，就成精神民俗。精神民俗主要包括民间信仰、民间巫术、民间哲学伦理观念及民间艺术等。</p>
              <p>
                山西民歌中反映出的精神民俗主要表现为多神崇拜和鬼魂崇拜。山西人是多神论者，什么神都敬。需要解决什么问题，就敬什么神。如民歌《水刮西包头》中详细表述了“光绪三十年整”,“水刮西包头”的异事，然后道出了“七月十五河神会，许下一个大河边放河灯＂的习俗来由。如山西常闹旱灾，很多村庄建有龙圧庙，供奉河神、龙王。祈雨在民间以前很盛行，当时官吏为了顺应民心，也在祈雨时随众迎接水神。解放后，祈雨活动渐渐绝迹。</p>
              <p>
                “一朵朵红云空中悬，那云头上倒坐众位八仙，脚踏住云头笑呵呵。”民歌《红云》中唱述的八仙是中国家喻户晓的传奇人物。“刘海云头撤金钱，将金钱撒在五福堂前，富寿荣华万万年。”对八仙的赞颂表现了山西人民对美好生活的向往与追求。</p>
              <p>
                “四月里来四月八，奶奶庙上把香插。”在山西，几乎每个村庄都有奶奶庙，供奉送子奶奶，送子观音，祈求多子多孙。</p>
              <p>
                与神灵崇拜并存的另一种精神民俗是鬼魂崇拜，过去，由于自然条件限制，人们不能解释生死、梦境等现象，就认为人死后并没有消失，而是还存于一个灵魂的世界。”正月正来正月正，牛头马面来把门，来了个二鬼勾上魂，我家老婆得了病，哎！要了她的命。“民歌《小寡妇上坟》中，也有“梦见我丈夫附了我个身”,“我给丈夫蒸供献”的情节，对鬼魂的祭奠更突出了生者的悲凉和对死者的思念。</p>


            </div>
          </div>
          <div class="col-lg-6 order-first m-b-30" data-aos="fade-up" data-aos-duration="1500">
            <div class="about-image me-auto">
              <img class="img-circle img-shadow" src="../assets/images/work/mfolk2.jpg" alt="About Image">
            </div>
          </div>
        </div>
      </div>
      <Footer class="foot"></Footer>
    </div>
    <!-- About Section End -->


  </div>


</template>

<script>

import Header from "../components/header";
import Footer from "../components/ShanxiFooter";

export default {
  name: "ShanxiFolk",
  components: {
    Header,
    Footer,
  },
}
</script>


<style scoped>
.foot {
  margin-top: 150px;
}

.head {
  z-index: 99;
}

.background_picture {
  height: 618px;
  background: url(../assets/images/work/mfolk1.jpg);
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  overflow: hidden;
  /*background-image: linear-gradient(to right, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);*/
}

.text-white {
  color: #fff !important;
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

.container {
  padding-right: 15px;
  padding-left: 15px;
  margin-left: 109px;
  margin-right: 109px;
  margin-top: 200px;
}

.container1 {
  padding-right: 15px;
  padding-left: 15px;
  margin-left: 109px;
  margin-right: 109px;
  margin-top: 150px;
}

.overlay::before {
  content: '';
  position: absolute;
  top: 60px;
  right: 0px;
  bottom: 170px;
  left: 0;
  z-index: 1;
  background: -webkit-gradient(linear, left top, right top, from(rgba(20, 20, 20, 0.8)), color-stop(0%, rgba(20, 20, 20, 0.8)));
  background: -webkit-linear-gradient(left, rgba(20, 20, 20, 0.8) 0%, rgba(20, 20, 20, 0.8) 0%);
  background: -o-linear-gradient(left, rgba(20, 20, 20, 0.8) 0%, rgba(20, 20, 20, 0.8) 0%);
  background: linear-gradient(to right, rgba(20, 20, 20, 0.8) 0%, rgba(20, 20, 20, 0.8) 0%);
}

.container {
  max-width: 1200px;
}

.row {
  --bs-gutter-x: 30px;
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

.col-12 {
  flex: 0 0 auto;
  width: 100%;

}

.breadcrumb-wrapper {
  text-align: center;
  position: relative;
  z-index: 99;
  padding-top: 40px;
}

.about-content {
  text-align: left;
}

.about-content span {
  position: relative;
  margin-top: 20px;
  padding-bottom: 30px;
  display: block;
  text-align: left;
}

.about-content span:after {
  position: absolute;
  content: '';
  width: 60px;
  height: 1px;
  background: #a295df;
}

.about-content {
  max-width: 495px;
}

.breadcrumb-wrapper .title {
  font-weight: 400;
  font-size: 56px;
  margin-bottom: 0;
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
  list-style-type: disc;
}

ul li {
  list-style: none;
}

.breadcrumb-wrapper .breadcrumb-menu li span {
  color: #ffffff;
  font-size: 16px;
}

.section-margin {
  margin-top: 0px;
  margin-bottom: 0px;
}

.section {
  float: left;
  width: 100%;
}


.m-b-n30 {
  margin-bottom: -30px;
}

.row {
  --bs-gutter-x: 30px;
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


.col-lg-6 {
  flex: 0 0 auto;
  width: 50%;

}


h2 {
  font-size: 36px;
}

h1, h2, h3, h4, h5, h6 {
  font-family: "Vidaloka", serif;
  font-weight: 600;
  line-height: 1.2;
  color: #232324;
}


.m-b-40 {
  margin-bottom: 40px;
}

.about-image {
  max-width: 530px;
}

.me-auto {
  margin-right: auto !important;
}

.img-shadow {
  box-shadow: #959ea5 0px 0px 41px;
}


p {
  color: #8a8a8a;
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


</style>
