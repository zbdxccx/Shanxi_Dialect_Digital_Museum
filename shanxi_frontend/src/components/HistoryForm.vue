<template>
    <div class="history-form">
        <div class="timeline">
            <a-timeline pending=" ">
                <a-timeline-item color="rgba(171, 117, 42)"><a href="#historic">史前时期的晋语</a></a-timeline-item>
                <a-timeline-item color="rgba(171, 117, 42)"><a href="#jin">晋国时期的晋语</a></a-timeline-item>
                <a-timeline-item color="rgba(171, 117, 42)"><a href="#fight">战国时期的晋语</a></a-timeline-item>
            </a-timeline>
            <div class="bgc">
                <el-color-picker v-model="color1">选择颜色</el-color-picker>
                <a-button icon="check" size="small"  @click="finishEdit()">
                </a-button>
            </div>
        </div>
        <a-drawer
        title="笔记"
        placement="right"
        :closable="true"
        :visible="visible"
        :after-visible-change="afterVisibleChange"
        @close="onClose">
          <a-card v-for="(item, i) in editList" :key="i">
            <p :style="{color: colors[i]}">{{item}}</p>
          </a-card>
        </a-drawer>
        <div class="content">
            <h3 id="historic">史前时期的晋语</h3>
            <img src="../assets/shanxi.png" alt="" align="right" width="250" hspace="5" vspace="5">
            <p v-for="(count,index) in firstFormContent"  :id="first(index)">{{count}}</p>
             <h3 id="jin">晋国时期的晋语</h3>
             <img src="../assets/Jin.png" alt="" align="left" width="250" hspace="5" vspace="5">
             <p v-for="(count,index) in secondFormContent" :id="second(index)">{{count}}</p>
             <h3 id="fight">战国时期的晋语</h3>
             <p v-for="(count,index) in thirdFormContent" :id="third(index)">{{count}}</p></div>
        </div>
</template>
<script>
import {Message} from 'element-ui'
export default {
  data () {
    return {
      color1: '#000',
      visible: false,
      colors: [],
      firstFormContent: [
        '山西地处黄土高原东部，黄河是山西西部及南部与邻省的天然界线。黄河流域被誉为“中华文明的摇篮”。随着考古发掘及研究的深入，人们认识到古代黄河流域(主要指中游地区)是远古华夏族最重要的、最集中的聚居区之一，新石器时代的“仲韶文化”遗址就散布在以关中、豫西、晋南一带为中心的广大西北地区。这一区域也正是传说中黄帝部落的活动中心。众多的氏族部落可能各有自己的文化、语言，但在长期的接触、战争、兼并中逐渐融合。其中炎帝族和黄帝族两个部落对华夏族的形成起过重要的历史作用。',
        '随着华夏族的形成，各部族的语言也融合成为华夏语。“黄帝族语言发展到夏禹时己由氏族共同语逐渐发展为部落联盟的共同语，并且成为春秋时称为‘雅言’(夏言),汉以后称为汉语的初步基础和源头。”这种原始汉语已经很难知道它的真正面貌，但它既然发源于黄河流域，其中自然应该包含了许多生活在黄河流域的山西先民的语言成分。董达武先生便认为周秦共同语(雅言)的基础方言在大约今天河南-山西-陕西这一三角地带。',
        '建国以来,山西境内发现大批原始文化遗址，这些古文化遗址很大程度上集中于运城和临汾两个地区，这两个地区又习惯合称为晋南地区。这一区域不仅在数量上拥有了将近70%的遗址，而且其代表意义也是无与伦比的。如西侯度遗址被考古学家认定为世界上已知的最早的文化遗址之一。晋南地区无疑是山西境内原始文化时期最先进、人口最集中的地区。地处最北边的雁北地区拥有的文化公遗址数量仅次于运城和临汾，而且具有很明显的连续性。山西各地区原始文化的发展并非互不相关，考古学家们认为:“从现有资料观察，山西北部(大同、朔县、宁武)、西部(河曲、保德、离石)和东部(寿阳、平定)的石器，晚于纵贯南北的汾河沿岸的丁村文化，而丁村文化又晚于南部(芮城、平陆、垣曲)的石器。这现象很可能说明:旧石器文化在山西是由南向北发展的。”这些现象似乎说明山西自古以来南北就是一个整体，这个整体自然包括文化和语言上的一致。就其使用的语言来讲，今山西境内各地在这一时期虽有差异，但也有不少共同之处。'
      ],
      secondFormContent: [
        '晋国之前，活动于这一区域的是古唐国。古唐国最早是帝尧所居之地。在其势力兴盛时期，古唐国是他们活动的中心区域。根据考古和相关文献，他们的活动区域应该是绛州翼城。在古唐国的发展中，有迁入者，也有迁出者，是各种外来移民的结合。周成王灭唐后，将该地封给了其弟叔虞。',
        '晋国的历史般从唐叔虞受封说起。居《史记》:“唐在河、汾之东，方百里”。后叔虞之子燮将国号改为晋。这是晋国的开始。晋国最早的都城是翼(今临汾翼城东南)，晋献公八年(公元前669年)，晋国迁都于绛，即所谓“故绛”(今临汾翼城城关)。而早在唐叔虞受封之前，在今山西地区已有不少小的方国，如虞、芮、黎、霍等。近年又有学者根据甲骨刻辞确定了一些当时居住于山西境内的国族，如先、丕、缶、亘、基、重等。我们对于这些小国的了解大都只限于它们的名称，晋国发展的历史首先便是吞并这些国族。',
        '晋国初立，面积很小，即《史记·晋世家》所载“方百里”。根据文献资料，直到东周初年，晋国只是当时北方众多小诸侯国之一。晋国取得较大发展是在晋献公时期。在晋献公晚年，晋国的声势已非昔日可比。“当此时，晋强，西有河西，与秦接境，北边翟，东至河内。”晋献公去世之年，时人宰孔曾云:“晋侯将死矣!景霍以为城，而汾、河、涑、浍以为渠，戎狄之民实环之。”“景霍”即今霍山。晋惠公夷吾为回国继位，曾“路秦伯以河外列城五，东尽虢略，南及华山，内及皆梁城。既而不与。”杜预注曰:“河外，河南也。华山在弘农华阴县西南。”可见当时晋国不仅基本占据了今天的临汾、运城两地区的大部，而且拥有一部分河南、陕西靠近运城地区的区域。',
        '晋景公四年(前598年)晋国军队向居于晋东南地区的赤狄发起进攻，最终赤狄败北，不复见诸经传，面积广大的晋东南地区成为晋国领土的一部分。',
        '周朝时，以并州晋阳为内涵的“太原”是戎狄的一个著名的聚居区。最早见于记载的晋国与戎狄的战争发生在公元前790年，“晋人败北戎于汾隰，戎人灭姜氏之邑”。"杜预注曰:“汾隰，汾水边。”公元前627年(晋文公去世之年)，晋国败狄于箕。“箕”位于太原附近。《左传·成公十三年》载晋卿吕相在与秦绝交时回忆狄难情况称:“入我河县，焚我箕、郜，芟夷我农功。”杜预注曰“太原阳邑县南有箕城。”顾栋高《春秋大事表》释之云:“今太原府太谷东南三十五里有箕城。”说明在晋文公时，晋国的疆界已扩展到山西中部。晋国北上的路线依然以汾河为主。前541年，晋国与北面的戎狄进行了一场大战，取得了决定性胜利，从此在晋中地区建立了稳固的统治。戎狄在这次失败后活动范围收缩至今吕梁地区及黄河以西。之后，晋国又进一步将东部边界推到了太行山一线。',
        '领土扩张的过程中，伴随着人口的流动。一方面是晋国将新的领士分封给诸侯，诸侯由晋国的发源地晋南迁移到中、北部，一方面是战败的戎狄势力不断萎缩，大量戎狄沦为奴隶。如:“晋侯赏桓子狄臣千室，亦赏士伯以瓜衍之县，日:‘吾获狄土，子之功也。’”这一过程中势必会有文化和语言的传播、融合。根据上述晋国的建立和扩展史，可以猜测:晋国初建之时，其臣民由周朝迁来，语言应该与周朝王畿一带的语言相差不多。但其初建之时仅“方百里”，周围都是当地土著，在相互的接触征战中，势必会相互影响，晋国的语言也会在不知不觉中发生变化，与周朝王畿-带的语言差异逐渐增大，而自身的方言特征逐步加强，成为一种独立的方言。到春秋时期，晋国成为中原霸主，其疆域已领有今晋南、晋东南、晋中的大部分地区。战国时，又领有今雁北地区。随着其领土的打张，它的语言也相应由晋南带到晋东南、晋中、晋北。此时的晋语由南向北传播扩张，虽然也在同戎狄语言的接触中悄悄发生着变化，但总体说来内部差异并不明显，这一时期晋语的情况应该就是其早期的面貌，我们称之为古晋语。古晋语的语音、词汇、语法等情况，则由于材料匮乏而无法考证。'
      ],
      thirdFormContent: [
        '战国时期，韩赵魏三国疆土的进一步扩张，拉开了古晋语内部分化的序幕。韩国先定都平阳(今临汾市西北)，前416年迁都宜阳(今河南省宜阳西南)，后来又迁阳翟(今河南省禹县)，公元前317年，韩哀侯灭郑，又迁都新郑(今河南新郑)。韩在领土扩张的过程中不断向周洛地区靠拢;韩又是一个工商业很发达的国家，与周洛带往来密切，其语言也受周洛方言的影响，古晋语的特征逐渐磨灭，与周洛方言越来越接近。据《汉书·地理志》说:“秦既灭韩，徙天 下不轨之民于南阳，故其俗夸奢，上气力，好商贾渔猎。.....”也就是说，秦灭韩后，韩地移民甚多，移民的语言冲击也使韩地语言离古晋语越来越远。所以《方言》中，韩与周并举5次，与郑并举7次，与赵并举仅2次，与魏并举仅3次，与晋则没有并举情况，这也说明韩国的方言变化很大，到秦汉时期已经基本 脱离了古晋语，而与周郑方言共同发展。很多学者也将其划入周郑韩一系，与晋方言、赵魏方言不再有联系。',
        '赵国最初定都晋阳(今山西太原西南)，前425年迁都中牟(今河南鹤壁市西)，前386年迁都邯郸(今河北邯郸市)。在山西，霍山以北，即中部和北部是赵国的势力范围，赵武灵王即位后，学习游牧民族的长处，增强国力，使赵国最终成为战国七雄之一，其文化也逐渐摆脱了晋国文化的窠臼，走上了独立发展的道路，加上与韩、魏的自然阻隔，它的方言也逐渐与古晋语产生了不同。魏国最初定都安邑(今夏县西北禹王村)，前361年，迁都大梁(今河南开封市)。赵魏两国则由于地界相邻，交通便利，来往密切，所以语言上保持了较多的一致性。赵魏两国在山西境内主要据有北部、中部、东南部。而山西南部则与秦地往来密切，语言也在后来逐渐趋同。',
        '赵国最初定都晋阳(今山西太原西南)，前425年迁都中牟(今河南鹤壁市西)，前386年迁都邯郸(今河北邯郸市)。在山西，霍山以北，即中部和北部是赵国的势力范围，赵武灵王即位后，学习游牧民族的长处，增强国力，使赵国最终成为战国七雄之一，其文化也逐渐摆脱了晋国文化的窠臼，走上了独立发展的道路，加上与韩、魏的自然阻隔，它的方言也逐渐与古晋语产生了不同。魏国最初定都安邑(今夏县西北禹王村)，前361年，迁都大梁(今河南开封市)。赵魏两国则由于地界相邻，交通便利，来往密切，所以语言上保持了较多的一致性。赵魏两国在山西境内主要据有北部、中部、东南部。而山西南部则与秦地往来密切，语言也在后来逐渐趋同。'
      ],
      editList: []
    }
  },
  methods: {
    afterVisibleChange (val) {
      console.log('visible', val)
    },
    showDrawer () {
      console.log(this.editList)
      this.colors.push(this.color1)
      this.visible = true
    },
    getMessage (path) {
      const params = new URLSearchParams()
      params.append('page',"form")
      this.$http.post(path, params)
        .then(res => {
          console.log(res.data.data.length)
          for(let i=0;i<res.data.data.length;i++){
            if(res.data.data[i].contents !== ''){
              this.colors.push(res.data.data[i].color)
              this.editList.push(res.data.data[i].contents)
            }
          }
        })
    },
    onClose () {
      this.visible = false
    },
    reviseInnerText (path) {
      const params = new URLSearchParams()
      params.append('page',"form")
      params.append('contents', this.editList[this.editList.length-1])
      params.append('color', this.colors[this.editList.length-1])
      this.$http.post(path, params)
        .then(res => {
          if (res.data === 'no') {
            Message.error('添加失败')
          } else {
            Message({
              message: '添加成功',
              type: 'success'
            })
          }
        })
        .catch(() => {
          console.log('错误')
        })
    },
    finishEdit () {
      const str = document.getSelection().toString()
      let judge = true;
      for(const item in this.editList){
        if(this.editList[item] == str){
          judge = false;
          break;
        }
      }
      if(str.length>=300){
        judge = false
      }
      let post = true
      if(str.length==0 || str == '\n' || str == ''){
        post = false
      }
      if(judge){
        this.showDrawer()
        if(post){
          this.editList.push(str)
          this.reviseInnerText('/display/history/reviseContent/')
        }
      }
      else{
        Message({
              message: '添加失败',
              type: 'error'
        })
      }
    },
    first (index) {
      return 'first' + index
    },
    second (index) {
      return 'second' + index
    },
    third (index) {
      return 'third' + index
    }
  },
  created: function () {
    this.getMessage('/display/history/getMessage/')
  }
}
</script>
<style src="../style/history.css" scoped></style>
<style scoped>
.bgc button{
  margin-top: 20px;
}
</style>