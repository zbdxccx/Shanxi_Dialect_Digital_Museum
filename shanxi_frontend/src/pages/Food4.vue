<template>
  <div>
    <Header class="head"></Header>
    <!-- Breadcrumb Section Start -->
    <div class="background_picture overlay">
      <div class="container" style="background:url(../assets/images/work/dumpling1.jpg);">
        <div class="row">
          <div class="col-12">

            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos-duration="1100">蒸饺</h1>

              <ul class="breadcrumb-menu" data-aos-duration="1500">
                <li>
                  <span>Steamed Dumpling</span>
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
    <div class="section section-margin ">
      <div class="container1 ">
        <div class="row m-b-n30 align-items-center">
          <div class="col-lg-6 m-b-30" data-aos="fade-up" data-aos-duration="1100">
            <div class="about-content mw-100">
              <h2 class="title">蒸饺</h2>
              <span></span>
              <p>菜品简介：蒸饺是中华民族传统节日食品，是每年春节必吃的年节食品。相传是中国东汉南阳"医圣"张仲景首先发明的，在中国许多省市也有冬至吃饺子的习惯。中国南方地区也普遍有饺子这一食品。
                饺子一般只是用猪牛羊肉和蔬菜作馅的传统小吃。但现在不光连鸡、鸭、鱼肉、蛋、海味、山珍、鲜蔬、干菜、果品等都可以作馅。但凡是好吃又富有营养的材料通通都可以作馅。</p>
              <p>
                菜品文化：我国北方人民把吃饺子看得非常"隆重"，北方人都是用饺子来作为冬至等重要节日的佳肴，以饺子为主食。而在成都的西南方向的人民往往把饺子作为小吃，改换口味、调节情趣。但成都的饺子比起北方来说，并不逊色。</p>
              <p>菜皮由来：饺子由馄饨演变而来。在其漫长的发展过程中，名目繁多，古时有"牢丸""扁食""饺饵""粉角"等名称。三国时期称作"月牙馄饨"，南北朝时期称"馄饨"，唐代称饺子为"偃月形馄饨"，宋代称为"角子"，元代、明代称为"扁食";清代则称为"饺子"。饺子起源于东汉时期，为东汉河南邓州人张仲景首创。当时饺子是药用，张仲景用面皮包上一些祛寒的药材用来治病(羊肉、胡椒等)，避免病人耳朵上生冻疮。</p>
        
            </div>
          </div>
          <div class="col-lg-6 order-first order-lg-last m-b-30" data-aos="fade-up" data-aos-duration="1500">
            <div class="about-image service-layer-image ms-auto">
              <img class="about-image-1" src="../assets/images/work/dumpling2.jpg" alt="About Image">
              <img class="about-image-2 img-circle" src="../assets/images/work/dumpling3.jpg" alt="About Image">
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
  name: "Food4",
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

.head {
  z-index: 99;
}

.background_picture {
  height: 618px;
  background: url(../assets/images/work/dumpling1.jpg);
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
  margin-top: 100px;
}

.overlay::before {
  content: '';
  position: absolute;
  top: 60px;
  right: 0;
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

.section, .section-fluid {
  float: left;
  width: 100%;
}


.m-b-n30 {
  margin-bottom: -30px;
}

.row {
  --bs-gutter-x: 30px;
}

.align-items-center {
  align-items: center !important;
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

.aos-animate {
  opacity: 1;
  transform: translateZ(0);
}

.col-lg-6 {
  flex: 0 0 auto;
  width: 50%;

}

.mw-100 {
  max-width: 100% !important;
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


p {
  margin-top: 0;
  margin-bottom: 1rem;
  font-family: "Montserrat", sans-serif;
  font-size: 14px;
  color: #8a8a8a;
  line-height: 2;
  visibility: visible;
}

.service-layer-image {
  position: relative;
  height: 577px;
}

.about-image {
  max-width: 530px;
  margin-left: -100px;
}

.ms-auto {
  margin-left: 0px;
}

.service-layer-image .about-image-1 {
  -webkit-box-shadow: #959ea5 0px 0px 41px;
  box-shadow: #959ea5 0px 0px 41px;
  border-radius: 50px;
}

.service-layer-image .about-image-2 {
  position: absolute;
  right: 0px;
  top: 255px;
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
