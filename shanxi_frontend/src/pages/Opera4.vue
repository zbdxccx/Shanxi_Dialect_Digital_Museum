<template>
  <div>
    <Header></Header>
    <div class="background_picture section breadcrumb-section overlay" data-bg-image="../assets/images/work/opera1.jpg">
      <div class="container">
        <div class="row">
          <div class="col-12">

            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos="fade-up" data-aos-duration="1100">晋北戏曲</h1>

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
                <img class="img-circle img-shadow" src="../assets/images/work/index_opera4.jpg" alt="Blog Details">
              </div>

              <h2 class="blog-details-title m-b-20" data-aos="fade-up" data-aos-duration="1300"> 晋北戏曲</h2>
              <p class="text" data-aos="fade-up" data-aos-duration="1100">
                晋北戏曲剧种方言区。以大同市为中心，南至朔州、忻州市。受蒲州梆子的影响，早期北路梆子的多用蒲白，以后逐渐使用本地的语言。晋北戏曲剧种方言区以的“七声清乐音节徴调式”为主，激昂慷慨边塞风骨。</p>
              <p class="text" data-aos="fade-up" data-aos-duration="1100">
                方言音调除广灵地区为北方官话保唐片外，“入声不分阴阳”成为其它地区最主要的方言声调。本区戏曲剧种中大量使用“哎、咳、啊、嗨呀、哎咳、哎呀哈”等衬词，并且多次重复演唱。忻州的部分地区历史上归太原府管辖，所以对中路梆子的流布范围就不仅是局限于本地地区。正所谓清中叶以后，蒲剧在晋语区并州片“音随地改”虽出现了梆子戏的“上路调”、“中路调”。
                </p>

              <div class="blog-content-image m-t-40 m-b-n50">
                <div class="blog-content-thumb m-b-50" data-aos="fade-up" data-aos-duration="1400">
                  <img class="img-circle img-shadow" src="../assets/images/work/opera3.jpg" alt="">
                </div>
                <div class="blog-content m-b-50" data-aos="fade-up" data-aos-duration="1600">
                  <p>
                    此外,晋东北的广灵地处广灵盆地，方言为北方官话。与晋北其它地区方言有别。但历史上归大同府管辖，方言虽然与其它地区有别，但行政区划上的一致性，为戏曲剧种方言的传播提供了便利。
                    方言区划表现为吕梁地区与太原、晋中地区分割开来。而戏曲剧种方言区划是一个整体，归入一个区。因而，两地在语言和文化等方面能够不被山脉所阻断，处于沟通和融合的行政管理之中。所以戏曲方言具有一致性。封闭的自然地理环境使该区方言不受外界干扰。方言特性和音调与其他区不同。另外，戏曲方言为艺术表演的形式，它所具有文化标志的语言给人的冲击远比书面语言以及人的流动迅速。
                    就是说，语言文化的适应性要比移民的移居要快，或者说语言文化可以通过极少数人员的流动影响到整个异地的居民语言习惯。
                  </p>
                  <p>
                     </p>
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
  name: "Opera4",
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
