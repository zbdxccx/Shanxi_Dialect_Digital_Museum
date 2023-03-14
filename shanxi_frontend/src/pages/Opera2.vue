<template>
  <div>
    <Header></Header>
    <div class="background_picture section breadcrumb-section overlay" data-bg-image="../assets/images/work/opera1.jpg">
      <div class="container">
        <div class="row">
          <div class="col-12">

            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos="fade-up" data-aos-duration="1100">山西秧歌</h1>

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
                <img class="img-circle img-shadow" src="../assets/images/work/index_opera2.jpg" alt="Blog Details">
              </div>

              <h2 class="blog-details-title m-b-20" data-aos="fade-up" data-aos-duration="1300"> 山西秧歌</h2>
              <p class="text" data-aos="fade-up" data-aos-duration="1100">
                秧歌在山西戏曲剧种占有大的比重。广泛流布于山西各地的秧歌戏有15个，主要包括晋中秧歌、晋北大秧歌、襄武秧歌、祁太秧歌等，是山西剧种数量最多的戏曲表演形式。</p>
              <p class="text" data-aos="fade-up" data-aos-duration="1100">
                这些秧歌戏从音乐唱腔上说，并非一个类型，有的为民歌体，如“祁太秧歌”、“沁源秧歌”，有的为板腔体，如“壶关秧歌”、“襄垣秧歌”、“武乡秧歌”：有的早已加入丝弦伴奏，如“繁峙秧歌”等：有的仍为徒歌干板演唱，如汾阳、孝义干板秧歌等：有的长期保持了民歌小戏特点，如“泽州秧歌”等；有的由于移植了梆子戏剧目，已成为板腔体、民歌体混用的“风搅雪”艺术形式，如“朔县大秧歌”等。总之，花样繁多，流布范围却较小。</p>

              <div class="blog-content-image m-t-40 m-b-n50">
                <div class="blog-content-thumb m-b-50" data-aos="fade-up" data-aos-duration="1400">
                  <img class="img-circle img-shadow" src="../assets/images/work/opera3.jpg" alt="">
                </div>
                <div class="blog-content m-b-50" data-aos="fade-up" data-aos-duration="1600">
                  <p>
                    山西秧歌与方言的联系比较紧密，是秧歌戏划分的基本依据、界限，当然这些秧歌与方言的关系界限并非十分紧密。另外，山西是民歌的故乡，山西民歌深受当地方言音调的影响，历经千年而不消亡，在此背景下，山西秧歌基本上是在山西民歌小调的基础上演变而来的，因此，山西秧歌剧种的方言韵味更加浓郁，出翼城秧歌分布在中原官话区内外，其余都分布在晋语区内，受外来语言音调影响小。</p>
                  <p>
                    秧歌是一种歌舞形式的剧种，起伏大、动感强，所以地势高、地形变化较大的太行山区、吕梁山区、晋北、晋东南区非常适宜山西各地不同艺术门类秧歌的分布。如流布于晋中一带，以祁县、太谷为中心的祁太秧歌，其形成应不晚于明代末期，它是受汾孝秧歌的影响而产生的，唱词道白用方言乡语。其它如繁峙大秧歌的道白为蒲白与繁峙方言混合。襄武秧歌、介休干调秧歌、广灵秧歌都是用当地语言音调的方言演唱。</p>
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
