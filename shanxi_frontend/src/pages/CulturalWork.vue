<template>
  <div>
    <Header></Header>
    <!-- 图文巨幕 -->
    <div class="bigp back">
      <h1 class="head1 mar-pic">山西方言作品</h1>
      <p class="lead p1-pic mar-pic">
        山西方言，中国研究古代汉语和近代汉语的活化石
      </p>
      <hr class="my-4 mar-pic line" />
      <img class="pic" src="../assets/images/work/pic1.png" />
    </div>

    <!-- 山西民俗 -->
    <div class="main pic ld_library">
      <div class="block news-wrap">
        <div class="content news">
          <div class="sub-title">
            <a @click="changePage(12)">
              <h2>山西民俗</h2>
              <h3>SHANXI FOLK</h3>
            </a>
            <div class="yellow-rectangle"></div>
          </div>
          <div class="card-wrap">
            <div class="img-wrap img-shadow1">
              <a @click="changePage(5)">
                <img src="../assets/images/work/culture_index_1.jpg" />
              </a>
            </div>
            <div class="list">
              <a @click="changePage(5)">
                <p class="title g-ellipsis p1">物质民俗</p>
                <p class="p1">
                  物质民俗，是指劳动人民在创造和消费物质财富的过程中不断重复的带有模式性的活动，以及由这种活动所产生的带有类型……
                </p>
              </a>
              <hr class="city-hr" />
              <a @click="changePage(6)">
                <p class="title g-ellipsis p1">精神民俗</p>
                <p class="p1">
                  精神民俗，是指在物质文化与制度文化基础上形成的有关意识形态方面的民俗。它是人类在认识和改造自然与社会过程中形……
                </p>
              </a>
              <hr class="city-hr" />
              <a @click="changePage(7)">
                <p class="title g-ellipsis p1">语言民俗</p>
                <p class="p1">
                  语言民俗，是指口语约定俗成，集体传承的信息交流系统。它包括民俗语言和民间文学。山西民歌中表现的语言民俗主要有……
                </p>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 文学作品 -->
    <div class="body ld_library" style="overflow: hidden">
      <div class="ld_library_3">
        <div class="wrap">
          <div>
            <a @click="changePage(13)">
              <h2>文学作品</h2>
              <h3>LITERARY WORK</h3>
            </a>
            <div class="yellow-rectangle"></div>
          </div>
          <div class="library_s1" style="margin: 0px 0 30px 0px">
            <div class="clearfix">
              <div class="s1">
                <span class="l">名称：</span>

                  <input
                    id="title_publishes"
                    type="text"
                    class="inp"
                    v-model="title_search"
                  />

              </div>
              <div class="s1">
                <span class="l">作者：</span>
                <div class="r">
                  <input
                    id="author_publishes"
                    type="text"
                    class="inp"
                    v-model="author_search"
                  />
                </div>
              </div>
              <div class="s1">
                <span class="l">出版社：</span>
                <div class="r">
                  <input
                    id="author_publishes"
                    type="text"
                    class="inp"
                    v-model="publisher_search"
                  />
                </div>
              </div>

              <div class="s2">
                <input
                  id="btn_publishes"
                  type="button"
                  value="搜 索"
                  @click="searchBook"
                />
              </div>
            </div>
          </div>
          <div class="ajaxList">
            <ul class="clearfix">
              <li class="adjust">
                <a href="/journal_detail/258029.html" target="_blank"
                  ><img src="../assets/images/work/book1.jpg" alt=""
                /></a>
              </li>
              <li class="adjust">
                <a href="/journal_detail/258030.html" target="_blank"
                  ><img src="../assets/images/work/book2.jpg" alt=""
                /></a>
              </li>
              <li class="adjust">
                <a href="/journal_detail/258031.html" target="_blank"
                  ><img src="../assets/images/work/book3.jpg" alt=""
                /></a>
              </li>
              <li class="adjust">
                <a href="/journal_detail/258031.html" target="_blank"
                  ><img src="../assets/images/work/book11.jpg" alt=""
                /></a>
              </li>
              <li class="adjust">
                <a href="/journal_detail/258031.html" target="_blank"
                  ><img src="../assets/images/work/book9.jpg" alt=""
                /></a>
              </li>
              <li class="adjust">
                <a href="/journal_detail/258031.html" target="_blank"
                  ><img src="../assets/images/work/book6.jpg" alt=""
                /></a>
              </li>
              <li class="adjust">
                <a href="/journal_detail/258031.html" target="_blank"
                  ><img src="../assets/images/work/book7.jpg" alt=""
                /></a>
              </li>
              <li class="adjust">
                <a href="/journal_detail/258031.html" target="_blank"
                  ><img src="../assets/images/work/book8.jpg" alt=""
                /></a>
              </li>
              <li class="adjust">
                <a href="/journal_detail/258031.html" target="_blank"
                  ><img src="../assets/images/work/book12.jpg" alt=""
                /></a>
              </li>
              <li class="adjust">
                <a href="/journal_detail/258031.html" target="_blank"
                  ><img src="../assets/images/work/book5.jpg" alt=""
                /></a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- 饮食文化 -->
    <div class="block city-wrap ld_library">
      <div class="content city">
        <div class="sub-title">
          <a @click="changePage(14)">
            <h2>饮食文化</h2>
            <h3>DIET CULTURE</h3>
          </a>
          <div class="yellow-rectangle"></div>
        </div>
        <div class="card-list">
          <div class="card1 img-shadow1" @click="changePage(1)">
            <a>
              <div class="img-wrap1">
                <img class="img1" src="../assets/images/work/diet1.jpg" />
              </div>
              <h3 class="g-ellipsis h3-1">刀削面</h3>
              <p class="title g-ellipsis p2">传统面食 中厚边薄 外滑内筋</p>
              <p class="p2">
                刀削面流行于山西省及其周边地区，据传是唐朝驸马柴绍始创，各种口味的臊子、调料食用。
              </p>
            </a>
            <div class="item-list">
              <router-link to="/Food1" class="item g-ellipsis a1"
                >菜品简介</router-link
              >
              <a
                target="_blank"
                href="delicious1.html"
                class="item g-ellipsis a1"
                >菜品由来</a
              >
              <a
                target="_blank"
                href="delicious1.html"
                class="item g-ellipsis a1"
                >菜品做法</a
              >
              <a
                target="_blank"
                href="delicious1.html"
                class="item g-ellipsis a1"
                >营养价值</a
              >
            </div>
          </div>
          <div class="card1 img-shadow1" @click="changePage(2)">
            <a>
              <div class="img-wrap1">
                <img class="img1" src="../assets/images/work/diet2.jpg" />
              </div>
              <h3 class="g-ellipsis h3-1">烙饼</h3>
              <p class="title g-ellipsis p2">传统面食 营养丰富</p>
              <p class="p2">
                烙饼是用面粉、鸡蛋等材料烙制而成的中国传统面食之一，可以配各种肉、蛋、蔬菜一起食用。
              </p>
            </a>
            <div class="item-list">
              <a class="item g-ellipsis">菜品源流</a>
              <a class="item g-ellipsis">菜品制作</a>
              <a class="item g-ellipsis">文化特色</a>
              <a class="item g-ellipsis">菜品评价</a>
            </div>
          </div>
          <div class="card1 img-shadow1" @click="changePage(3)">
            <a>
              <div class="img-wrap1">
                <img class="img1" src="../assets/images/work/diet3.jpg" />
              </div>
              <h3 class="g-ellipsis h3-1">花糕</h3>
              <p class="title g-ellipsis p2">各目繁多 印花脱饼</p>
              <p class="p2">
                多以米粉、豆粉等为原料，发酵，更点缀以枣、栗、杏仁等果馕，同时加糖蒸制而成。
              </p>
            </a>
            <div class="item-list">
              <a class="item g-ellipsis">菜品历史</a>
              <a class="item g-ellipsis">传说典故</a>
              <a class="item g-ellipsis">成菜特征</a>
              <a class="item g-ellipsis">食材原料</a>
            </div>
          </div>
          <div class="card1 img-shadow1" @click="changePage(4)">
            <a>
              <div class="img-wrap1">
                <img class="img1" src="../assets/images/work/diet4.jpg" />
              </div>
              <h3 class="g-ellipsis h3-1">蒸饺</h3>
              <p class="title g-ellipsis p2">传统小吃 百饺百格 回味无穷</p>
              <p class="p2">
                蒸饺是中华民族传统节日食品，是每年春节必吃的年节食品。相传是东汉南阳"医圣"张仲景发明。
              </p>
            </a>
            <div class="item-list">
              <a class="item g-ellipsis">历史文化</a>
              <a class="item g-ellipsis">制作方法</a>
              <a class="item g-ellipsis">成菜特征</a>
              <a class="item g-ellipsis">外界评价</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 5张图 -->
    <!-- introduction -->
    <div class="introduction ld_library">
      <a @click="changePage(15)">
        <h2>山西戏曲</h2>
        <h3>SHANXI OPERA</h3>
      </a>
      <div class="yellow-rectangle"></div>
      <div class="introduction_main">
        <ul class="introduction_ul">
          <li>
            <div class="introduction_div">
              <a @click="changePage(8)"
                ><img
                  class="introduction_picture"
                  src="../assets/images/work/index_opera1.jpg"
                  alt="无法显示"
                  title="图片1"
              /></a>
            </div>
            <div class="introduction_text">
              <span class="introduction_span1"
                ><p class="introduction_p">
                  山西四大梆子最早的活动地区分别在晋中、晋南、晋北、晋东南，与山西方言的内部区划相一致。
                </p>
              </span>
            </div>
          </li>
          <li>
            <div class="introduction_div">
              <a @click="changePage(9)"
                ><img
                  class="introduction_picture"
                  src="../assets/images/work/index_opera2.jpg"
                  alt="无法显示"
                  title="图片2"
              /></a>
            </div>
            <div class="introduction_text">
              <span class="introduction_span2"
                ><p class="introduction_p">
                  秧歌在山西戏曲剧种占有大的比重。广泛流布于山西各地的秧歌戏有15个，花样繁多，流布范围较小。
                </p>
              </span>
            </div>
          </li>
          <li>
            <div class="introduction_div">
              <a @click="changePage(10)"
                ><img
                  class="introduction_picture"
                  src="../assets/images/work/index_opera3.jpg"
                  alt="无法显示"
                  title="图片3"
              /></a>
            </div>
            <div class="introduction_text">
              <span class="introduction_span3"
                ><p class="introduction_p">
                  受道教影响，道情戏是山西戏曲中独特的剧种。与当地的语言音调结合，形成其独特的声腔音韵风格。
                </p>
              </span>
            </div>
          </li>
          <li class="introduction_li">
            <div class="introduction_div">
              <a @click="changePage(11)"
                ><img
                  class="introduction_picture"
                  src="../assets/images/work/index_opera4.jpg"
                  alt="无法显示"
                  title="图片4"
              /></a>
            </div>
            <div class="introduction_text">
              <span class="introduction_span4"
                ><p class="introduction_p">
                  方言在民俗文化与活动中亦有所体现。山西民歌等载体中的方言描绘了山西的自然景观与人文景观。
                </p>
              </span>
            </div>
          </li>
        </ul>
      </div>
    </div>

    <Footer></Footer>
  </div>
</template>

<script>
import Header from "../components/header";
import Footer from "../components/ShanxiFooter";

export default {
  name: "CulturalWork",
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      title_search: "",
      author_search: "",
      publisher_search: "",
    };
  },
  methods: {
    changePage(index) {
      console.log(index);
      console.log(this.$router);
      switch (index) {
        case 1:
          this.$router.replace("/Food1");
          break;
        case 2:
          this.$router.push("/Food2");
          break;
        case 3:
          this.$router.push("/Food3");
          break;
        case 4:
          this.$router.push("/Food4");
          break;
        case 5:
          this.$router.push("/MaterialFolk");
          break;
        case 6:
          this.$router.push("/SpiritualFolk");
          break;
        case 7:
          this.$router.push("/DialectFolk");
          break;
        case 8:
          this.$router.push("/Opera1");
          break;
        case 9:
          this.$router.push("/Opera2");
          break;
        case 10:
          this.$router.push("/Opera3");
          break;
        case 11:
          this.$router.push("/Opera4");
          break;
        case 12:
          this.$router.push("/ShanxiFolk");
          break;
        case 13:
          this.$router.push("/ShanxiLiterature");
          break;
        case 14:
          this.$router.push("/ShanxiFood");
          break;
        case 15:
          this.$router.push("/ShanxiOpera");
          break;
      }
    },
    searchBook() {
      this.$router.push({
        path: "SearchBook",
        query: {
          title_search: this.title_search,
          author_search: this.author_search,
          publisher_search: this.publisher_search,
        },
      });
    },
  },
};
</script>

<style scoped>
@import url("https://img.dpm.org.cn/Public/static/themes/css/page.css?v=415121113");
@import url("https://img.dpm.org.cn/Public/static/themes/css/global.css?v=415121113");

/* 图文巨幕 */

.pic {
  left: 0;
  bottom: 0;
  opacity: 1;
}

.bigp {
  height: 688px;
}

.head1 {
  padding-top: 90px;
  font-size: 36px;
}

.p1-pic {
  margin-top: 20px;
  color: #4f4f4f;
}

.p2-pic {
  margin-bottom: 55px;
}

.mar-pic {
  margin-left: 100px;
}

.back {
  text-align: left;
  background-image: url(../assets/images/work/big_picture2.png);
}

.line {
  width: 700px;
  color: #474747;
}

/*山西民俗*/
h2 {
  font-size: 36px;
  font-weight: 600;
  color: #343434;
}

h3 {
  font-size: 14px;
  font-weight: 300;
  color: #8e8d8d;
  margin: 10px;
  line-height: 2;
}

.img-wrap {
  height: 423px;
}

.main {
  color: #330;
  /*background: #f7f6f8;*/
  min-width: 1200px;
  position: relative;
}
.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

.img-shadow1 {
  box-shadow: #959ea5 0px 0px 20px;
}

.pic {
  padding-top: 70px;
}

.sub-title {
  text-align: center;
}

.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

.news img {
  width: 751px;
  height: 423px;
  position: absolute;
  top: 0;
  left: 0;
}

.news .list {
  position: absolute;
  top: 0;
  right: 0;
  width: 449px;
}

.news .list a {
  position: relative;
  display: block;
  height: 141px;
  font-size: 14px;
  line-height: 21px;
  color: #8e8d8d;
  padding: 27px;
  box-sizing: border-box;
  transition: 0.3s;
  text-decoration: none;
}

.news {
  height: 628px;
}

.content {
  width: 1200px;
  position: relative;
  margin: 0 auto;
}

.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

a {
  text-decoration: none;
}

.news .list {
  position: absolute;
  top: 0;
  right: 0;
  width: 449px;
}

.news .list .title {
  font-size: 24px;
  font-weight: 400;
  color: #343434;
  line-height: 30px;
  margin-bottom: 14px;
  margin-top: 0;
}

.g-ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.p1 {
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}

.list a:hover p {
  color: cornflowerblue;
}

.city-hr {
  margin: 0;
}

body,
td,
th {
  font: 14px -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Ubuntu,
    Helvetica Neue, Helvetica, Arial, PingFang SC, Hiragino Sans GB,
    Microsoft YaHei UI, Microsoft YaHei, Source Han Sans CN, sans-serif;
}

h3,
li,
ol,
p,
ul {
  list-style: none;
}

h1,
h2,
h3,
h4,
h5,
h6,
p,
ul {
  margin: 0;
  padding: 0;
}

.yellow-rectangle {
  width: 40px;
  height: 9px;
  background: #ffb400;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 30px;
}

.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

/*文学作品*/


.adjust {
  height: 343px !important;
}

.ld_library_3 {
  height: 940px;
  padding-top: 60px;
  position: relative;
  z-index: 10;
}

/* 特色美食 */
.city {
  height: 668px;
}

.content {
  width: 1200px;
  position: relative;
  margin: 0 auto;
}

.city .sub-title {
  padding-top: 50px;
  margin-bottom: 20px;
}

.sub-title[data-v-6f74154e] {
  text-align: center;
}

.city .card-list {
  margin-left: -43px;
}

.card1 {
  width: 266px;
  height: 416px;
  background: #fff;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.05);
  display: inline-block;
  margin-left: 40px;
  margin-bottom: 35px;
  vertical-align: top;
  font-size: 14px;
  color: #8e8d8d;
  line-height: 21px;
  position: relative;
}

.img-wrap1 {
  width: 266px;
  height: 152px;
  overflow: hidden;
}

.img1 {
  width: 265px;
  height: 150px;
  vertical-align: middle;
  border: 0px;
}

.p2 {
  color: #8e8d8d;
  margin: 0 23px 7px;
}

.item-list {
  margin-left: -10px;
  position: absolute;
  bottom: 9px;
  width: 270px;
}

.item {
  width: 93px;
  line-height: 29px;
  padding: 0 5px;
  text-align: center;
  border-radius: 15px;
  color: #8e8d8d;
  display: inline-block;
  border: 1px solid #8e8d8d;
  margin-left: 16px;
  margin-bottom: 11px;
}

.h3-1 {
  font-size: 24px;
  line-height: 25px;
  font-weight: 300;
  margin: 21px 23px 7px;
  color: #000;
}

.item:hover {
  width: 95px;
  line-height: 31px;
  background: #ffb400;
  color: #fff;
  border: none;
  text-decoration: none;
}

.card1 a:hover {
  color: gray;
}

.card1 a:hover h3 {
  color: #00cb86;
}

/*5张图*/
.introduction {
  width: 100%;
  padding-top: 80px;
  padding-bottom: 100px;
}

.introduction_main {
  width: 1000px;
  margin: 0px auto 0px;
}
.introduction_tit {
  margin-top: 10px;
  margin-bottom: 10px;
  line-height: 20px;
}

.introduction_i {
  display: block;
  width: 30px;
  height: 3px;
  background-color: blue;
  margin-top: 15px;
  margin-bottom: 10px;
}

.introduction_ul {
  width: 1000px;
  overflow: hidden;
  padding-left: 0;
  margin-top: 0;
  margin-bottom: 0;
}

.introduction_ul li {
  list-style: none;
  width: 230px;
  float: left;
  margin-right: 26px;
}

.introduction_div {
  width: 230px;
  height: 165px;
  border: 1px solid gray;
}

.introduction_picture {
  width: 220px;
  height: 155px;
  padding-left: 1px;
  padding-right: 1px;
  padding-top: 4px;
  padding-bottom: 2px;
  vertical-align: top;
}

.introduction_text {
  width: 230px;
  margin-top: 10px;
}

.introduction_ul .introduction_li {
  list-style: none;
  width: 230px;
  float: left;
  margin-right: 0px;
}

/*<roll>*/

.roll_img {
  width: 158px;
  height: 120px;
  padding-left: 0px;
  padding-right: 0px;
  padding-top: 0px;
  padding-bottom: 0px;
  vertical-align: top;
}

.roll_pic1 {
  margin: 0px 5px 0 0;
  flex-shrink: 0;
}

.wrag {
  position: absolute;
  margin: 0 auto;

  left: auto;
  right: auto;
  width: 1000px;
  height: 150px;
  white-space: nowrap;
  overflow-x: scroll;
  overflow-y: hidden;
}

.roll {
  display: flex;
}

.roll_div {
  width: 100%;
}

.rollmain_div {
  width: 1000px;
  margin: 60px auto 230px;
}

.roll_tit {
  margin-bottom: 15px;
}

.roll_pic {
  margin: 0px 5px;
  flex-shrink: 0;
}

.inp {
    display: block;
    width: 78%;
    padding-right: 0%;
    line-height: 20px;
    text-indent: 1em;
  margin-top:  10px;
   display:inline;
  float:right;

}
.s1{
    width: 337px;
    height: 40px;
    float: left;
    background: url(../assets/images/work/s_1-1.png) repeat-x center;
    margin-right: 40px;
   display:inline
}
.l{
  float: left;
    line-height: 40px;
    width: 70px;
    text-align: right;
}
.libary_s1 .s1 .l, .libary_s2 .s1 .l, .libary_s3 .s1 .l {
    float: left;
    line-height: 40px;
    width: 70px;
    text-align: right;
}
.s2 {
    float: right;
    width: 127px;
    display: block;
    line-height: 40px;
    height: 40px;
    text-align: center;
    background: url(../assets/images/work/s_2.png) no-repeat center;
}
input{
  overflow: visible;
}

</style>
