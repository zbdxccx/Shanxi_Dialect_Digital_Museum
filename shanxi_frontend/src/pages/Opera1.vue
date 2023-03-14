<template>
  <div>
    <Header></Header>
    <div class="background_picture section breadcrumb-section overlay" data-bg-image="../assets/images/work/opera1.jpg">
      <div class="container">
        <div class="row">
          <div class="col-12">

            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos="fade-up" data-aos-duration="1100">晋南戏曲</h1>

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
                <img class="img-circle img-shadow" src="../assets/images/work/index_opera1.jpg" alt="Blog Details">
              </div>

              <h2 class="blog-details-title m-b-20" data-aos="fade-up" data-aos-duration="1300"> 晋南戏曲</h2>
              <p class="text" data-aos="fade-up" data-aos-duration="1100">
                晋南戏曲剧种方言区。又称河东戏曲剧种方言区。指临汾地区与运城地区，所包括县市与山西戏曲剧种文化区一致。在中原官话的影响下，由于自然地理环境相同，临汾与运城地区方言音调是一致的，方言音调为无入声，不属于晋语系。主要包括今长治、晋城两市，从晋方言看，由于历史原因，这里东跨河北西南部，南连豫北。</p>
              <p class="text" data-aos="fade-up" data-aos-duration="1100">
                </p>

              <div class="blog-content-image m-t-40 m-b-n50">
                <div class="blog-content-thumb m-b-50" data-aos="fade-up" data-aos-duration="1400">
                  <img class="img-circle img-shadow" src="../assets/images/work/opera3.jpg" alt="">
                </div>
                <div class="blog-content m-b-50" data-aos="fade-up" data-aos-duration="1600">
                  <p>
                    因而本区的戏曲剧种唱腔音调也表现为“无入声”，本区声腔以“七声燕乐音阶徵调式”的梆子腔为主，因而音域宽，高亢激昂，朴实奔放。衬词大量使用，委婉，丰富的“哪、呀、啊、哎＂等词。蒲州作为蒲州梆子的诞生地，蒲剧作为该区戏曲剧种声腔的典型代表，表现为强势文化，具声腔、音调不仅仅影响到晋南地区的其它地方小剧种，也成为中路梆子、北路梆子、上党梆子萌芽期的声腔用语。本区虽然与中原地区接壤，容易受南方声腔的影响，但梆子声腔依然占有绝对的主导地位。
                    山陕梆子传到上党区较早，但它在晋语区上党片“音随地改”，变成了独具特色上党梆子声腔音调，后来主要衍变在念白中使用。其风格直率与委婉，热情与开朗。＂咳、哎、啊、垲了了，咳、得儿”，后缀“儿”化音，前缀“垲”，戏曲方言音调“入声不分阴阳”。本区的腔调为“徴调式与宫调式”，音节中缺少“清角”，高亢激越、朴实粗犷。
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
  name: "Opera3",
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
