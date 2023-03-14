<template>
  <div style="margin-top: -70px">
    <div class="temporary6" id="temporary_6" style="background-image: url('./../static/HomeBackground.png')">
      <div class="wrap">
        <div class="foucs">
          <div class="img">
            <div>
              <!--              <img class=" lazyloaded" data-src="https://img.dpm.org.cn/Uploads/Picture/2022/09/29/s6335484ae944d.jpg" src="https://img.dpm.org.cn/Uploads/Picture/2022/09/29/s6335484ae944d.jpg">-->
              <img class=" lazyloaded" src="./../../static/news/s6335484ae944d.jpg">
            </div>
          </div>
          <div class="frame1">
            <div class="child" id="temporary6">

              <div class="text">
                <div class="list">
                  <div class="item">
                    <h2>
                      <a class="nolink">和合共生——故宫•国博藏文物联展</a>
                      <span class="label ic-zc">展出</span>
                    </h2>
                    <p>
                      <span style="float:left;">中国国家博物馆</span>
                      <span style="float:right;">2022/09/28 - 2023/01/03</span>
                    </p>
                    <p style="clear:both;"></p>
                  </div>
                  <div class="item">
                    <h2>
                      <a class="nolink">来试人间第二泉——惠山茶会人文主题特展</a>
                      <span class="label ic-zc">展出</span>
                    </h2>
                    <p>
                      <span style="float:left;">无锡博物院</span>
                      <span style="float:right;">2022/09/28 - 2023/01/04</span>
                    </p>
                    <p style="clear:both;"></p>
                  </div>
                  <div class="item">
                    <h2>
                      <a class="nolink">高古奇骇——陈洪绶书画作品展</a>
                      <span class="label ic-zc">展出</span>
                    </h2>
                    <p>
                      <span style="float:left;">绍兴博物馆（徐渭艺术馆）</span>
                      <span style="float:right;">2022/09/28 - 2022/12/20</span>
                    </p>
                    <p style="clear:both;"></p>
                  </div>
                  <div class="item">
                    <h2>
                      <a class="nolink">园说Ⅳ——这片山水这片园</a>
                      <span class="label ic-zc">展出</span>
                    </h2>
                    <p>
                      <span style="float:left;">颐和园博物馆</span>
                      <span style="float:right;">2022/09/28 - 2023/02/05</span>
                    </p>
                    <!--                    <p style="clear:both;"></p>-->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div style="margin: 50px">&nbsp;</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dialect',
  components: {

  },
  data() {
    return {
      activeName: ['1']
    };
  },
  methods: {
    handleChange(val) {
      console.log(val);
    }
  }
};
</script>

<style scoped>
.wrap {
  width: 1258px;
  height: 100%;
  margin: 0 auto;
  position: relative;
}
.temporary6 .title2 {
  margin-bottom: 50px;
}
.temporary6 .title2 {
  overflow: hidden;
}
.title2 {
  margin-top: 50px;
  text-align: center;
  font-size: 26px;
  color: #474747;
  line-height: 1;
}
.temporary6 .title2 span {
  position: relative;
  display: inline-block;
}
.temporary6 .title2 span .s1 {
  left: -500px;
  background: url(../assets/images/work/temporary-title.png) no-repeat right center;
}
.temporary6 .title2 span i {
  display: block;
  width: 483px;
  height: 100%;
  position: absolute;
  top: 0;
}
i, em {
  font-style: normal;
  font-weight: normal;
}
.title2 span img {
  height: 65px;
  width: auto;
}
img {
  border: 0;
  outline: 0;
  vertical-align: middle;
  max-width: 100%;
  max-height: 100%;
}
.temporary6 .title2 span .s2 {
  right: -500px;
  background: url(../assets/images/work/temporary-title1.png) no-repeat left center;
}
.temporary6 .title2 span i {
  display: block;
  width: 483px;
  height: 100%;
  position: absolute;
  top: 0;
}
.temporary6 .foucs {
  position: relative;
  overflow: hidden;
}
.temporary6 .img {
  width: 50%;
  height: 100%;
  float: left;
  overflow: hidden;
}
.temporary6 .img img {
  cursor: inherit;
}
.temporary6 .img img {
  /*cursor: pointer;*/
  cursor: inherit;
  transform: scale(1);
  transition-property: all;
  transition-duration: .6s;
  -webkit-transform: scale(1);
  -webkit-transition-property: all;
  -webkit-transition-duration: .6s;
}
.temporary6 .frame1 {
  overflow: hidden;
  width: 50%;
  height: 100%;
  float: left;
}
.temporary6 .child {
  height: 495px;
}
.temporary6 .text .item h2:hover a.nolink{
  opacity:1;
}
.temporary6 .text {
  width: 100%;
  height: 100%;
  background: url(../assets/images/work/temporary6-pic2.jpg) no-repeat center;
  position: relative;
}
.temporary6 .text .list {
  padding-top: 20px;
}
.temporary6 .text .item {
  padding: 20px 0;
  margin: 0 30px;
  background: url(../assets/images/work/temporary6-pic3.jpg) repeat-x left bottom;
}
.temporary6 .text .item h2 {
  font-size: 16px;
  color: #fff;
  padding-left: 20px;
  background: url(../assets/images/work/temporary6-icon1.png) no-repeat left center;
  text-align: left;
}
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
  color: inherit;
}
a {
  text-decoration: none !important;
  color: inherit;
}
#temporary6 .ic-zc {
  background: #6b2420 none repeat scroll 0 0;
}
.temporary6 .text .item h2 .label {
  float: none;
  border-radius: 3px;
  color: #fff;
  display: inline-block;
  font-size: 14px;
  margin: 0 10px;
  padding: 5px 5px;
}
.temporary6 .text .item h2 span {
  font-family: Arial;
  float: right;
}
.temporary6 .text .item p {
  font-size: 14px;
  color: #fff;
  padding-left: 20px;
  margin-top: 10px;
}
.temporary6 .text .pages {
  padding: 32px 0;
  color: #fff;
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
}
.pages {
  padding: 35px 0;
  text-align: center;
}
.temporary6 .text .pages a.now {
  background: url(../assets/images/work/page_a1.png) no-repeat scroll center center;
}
.pages a.now {
  background: #987444;
  border-radius: 50%;
  padding: 5px;
  color: #fff;
}
.pages a {
  display: inline-block;
  min-width: 30px;
  min-height: 30px;
  line-height: 30px;
  margin: 0 5px;
  font-size: 18px;
  font-family: Arial;
  vertical-align: middle;
}
.temporary3 h2 {
  font-size: 16px;
  color: #474747;
  line-height: 1.2;
  margin-top: 12px;
  text-align: center;
}
.temporary3 {
  padding: 65px 0 80px;
}
</style>
