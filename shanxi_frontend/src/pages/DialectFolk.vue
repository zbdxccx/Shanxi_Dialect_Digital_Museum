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
              <h1 class="title text-white" data-aos-duration="1100">语言民俗</h1>

              <ul class="breadcrumb-menu" data-aos-duration="1500">
                <li>
                  <span>Material Folk</span>
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
              <h2 class="title m-b-40">语言民俗</h2>
              <p>
                语言民俗，是指口语约定俗成，集体传承的信息交流系统。它包括民俗语言和民间文学。山西民歌中表现的语言民俗主要有谚语、串语和俗语等。</p>
              <p>山西民歌中一个显著的特征是叠字运用广泛，这在山西民间口头语中也是大量存在的。</p>
              <p>
                “青草弯弯杨柳叶摆，红丹丹的桃李花花开。” “画眉眉那羊羔羔虎头头，柔软软的绒毛毛绵溜溜。” “麻阴阴天气雾沉沉，想亲亲哭成泪人人。”</p>
              <p>
               叠字在我国古代的歌曲中就有应用，尤其是在明清戏曲及小令、套曲中。在戏曲中，大多用来烘托和加深情绪。山西民歌中的叠字，一方面是从古代民歌中沿袭下来，另一方面是对民间的口头语的提炼。</p>
              <p>山西民歌中保留了大量的民间土语，这些“土得掉渣”的乡语乡音是非常有地方特色的。“人家回来你不回，你在那口外外刮野鬼。“刮野鬼”，是指像鬼一样在外边到处野跑和流浪。“骑马不骑那黄海溜，为朋友不为那洋烟猴。”黄海溜，是指一种淡色的劣种马；洋烟猴，泛指吸鸦片的人。另外还有，“吗们”（指我们的意思）,“袭人”（指女子长得好看）,“二不溜溜”（指不大不小）,“洋枪棒”（用羊腿骨做成的烟袋）,“鬼嚼”（指胡说八道）,“大大”（指爸爸）,“灰塌二溜”（形容没有生气，灰溜溜的样子）。</p>
              <p>山西民歌中的谚语含量也很大。例如： “樱桃好吃树难栽，朋友好为口难开。” “疥蛤蟆上树遭小灾，十指连心咋离开？” “鱼离小坑树剥皮，死好分开活难离。” “三十年水道河成河，三十年媳妇熬成婆。”</p>
              <p>
                山西民歌的语言民俗，充分反映了山西人民丰富的想象力和创造力，以及质朴、豪放和诙谐的性格。</p>

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
  name: "DialectFolk",
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
