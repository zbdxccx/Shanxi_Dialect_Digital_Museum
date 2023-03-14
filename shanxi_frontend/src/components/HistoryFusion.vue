<template>
  <div class="history-form">
      <div class="timeline">
          <a-timeline pending=" ">
              <a-timeline-item color="rgba(171, 117, 42)"><a href="#historic">山西方言与少数民族的接触融合</a></a-timeline-item>
              <a-timeline-item color="rgba(171, 117, 42)" ><a href="#huns" style="font-size: 12px;">与匈奴的接触</a></a-timeline-item>
              <a-timeline-item color="rgba(171, 117, 42)"><a href="#others" style="font-size: 12px;">与西羌、乌桓、鲜卑的接触</a></a-timeline-item>
              <a-timeline-item color="rgba(171, 117, 42)"><a href="#fight">山西方言的境外扩散</a></a-timeline-item>
              <a-timeline-item color="rgba(171, 117, 42)"><a href="#hong" style="font-size: 12px;">明洪武年间的移民</a></a-timeline-item>
              <a-timeline-item color="rgba(171, 117, 42)"><a href="#qing" style="font-size: 12px;">清朝时期向内蒙的移民</a></a-timeline-item>
              <a-timeline-item color="rgba(171, 117, 42)"><a href="#Shaanxi" style="font-size: 12px;">陕北晋语区的形成与晋商活动</a></a-timeline-item>
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
          <h3 id="historic">山西方言与少数民族的接触融合
          </h3>
          <p id="first">{{firstFusionContent}}</p>
          <h4 id="huns">与匈奴的接触</h4>
          <p id="second">{{secondFusionContent}}</p>
          <h4 id="others">与西羌、乌桓、鲜卑的接触</h4>
          <p  v-for="(count,index) in thirdFusionContent" :id="third(index)">{{count}}</p>
          <h3 id="fight">山西方言的境外扩散</h3>
          <p id="fourth">{{fourthFusionContent}}</p>
          <h4 id="hong">明洪武年间的移民</h4>
          <p id="fifth">{{fifthFusionContent}}</p>
          <h4 id="qing">清朝时期向内蒙的移民</h4>
          <p  v-for="(count,index) in sixthFusionContent" :id="sixth(index)">{{count}}</p>
          <h4 id="Shaanxi">陕北晋语区的形成与晋商活动</h4>
          <p v-for="(count,index) in seventhFusionContent" :id="seventh(index)">{{count}}</p>
        </div>
  </div>
</template>
<script>
import {Message} from 'element-ui'
export default {
  data () {
    return {
      editable: false,
      visible: false,
      color1: '#000',
      colors: [],
      firstFusionContent: '山西历来是北方各少数民族活动的区域。自先秦始经秦汉，在魏晋南北朝出现高潮，直至唐宋，绵绵不绝。在与其他民族长期的接触、混居中，晋语的面貌也或多或少受到了影响。',
      secondFusionContent: '秦汉时期，匈奴成为活跃于山西境内的少数民族。秦、西汉时期，匈奴南下活动的主要地区是今雁北，即西汉时雁门郡和代郡。东汉时期，匈奴的骑兵进袭远至河东、上党地区(今临汾、运城、晋东南三地区)。建武24年(公元48年)，南北匈奴分裂。东汉政府允许南单于入居云中，后南单于又徒居西河，东汉西河郡包括今黄河西岸吕梁地区的大部。到曹魏时期，匈奴在山西分为五部，涉及今忻州、晋中、吕梁、临汾等四个地区，而以晋中为其中心。',
      thirdFusionContent: [
        '继匈奴之后，在山西活动的少数民族主要有西羌、乌桓、鲜卑。东汉至曹魏，乌桓内迁，主要居于今雁北、忻州、晋中地区。在曹魏末年乃至西晋年间，记载中的鲜卑部众似乎都在向山西地区聚拢，几乎每一种部族都在山西地区出现过，而且数量庞大，居留区域十分广泛，其声势已远远超过乌桓。到刘氏汉国创立之时，山西境内的其他各族百姓至少在100万人以上。另外唐代晚期，居于青海一带的土谷浑族受到吐蕃的攻击而东徙，后主要分 散在朔方、河东一带。沙陀部族也是唐末迁入河东境内。',
        '虽然历史上有众多的北方民族先后进入山西，与当地汉人杂居生活，但总的趋势是这些北方民族在文化和语言上被当地汉人同化，最终成为汉人的一部分。而这些少数民族对山西汉人的影响似乎并不大。其影响在文化风俗上体现为晋 中、晋北一带民风淳朴、性格粗犷:在语言上则主要集中在词汇上，尤其是亲属称谓、畜牧等方面的词汇。'
      ],
      fourthFusionContent: '战国时期，韩赵魏领土大大扩张，势力范围深入境外河南，但当时古晋语对境外方言的影响并不大。魏地南部反而受楚语渗透，韩地更是融于周洛方言。山西方言向境外的扩散主要是明清以来几次大的移民活动所致，这些移民活动是山西境外晋语区形成的直接原因。',
      fifthFusionContent: '据《明太祖实录》，洪武21年迁山西泽、潞两州(今山西东南部的晋城、长治等地)的人民于山东，22年迁沁州(今山西中部的沁县)民众于山东、河南、北平等地。河南《林县志》记载:林民先世多籍晋，其来也皆在明初。谱碣所载尤以洪洞为多……旧志云，永乐十年归并县属为二十五里，后相继迁民，加以军屯，增为三十三里。知在洪(洪武)、永(水乐)两朝，盖继续行之，不止一次也。2根据这条记录，移民的人数很多，甚至将县属增至三十三里。',
      sixthFusionContent: [
        '清康熙实行“移民实边”的政策后，大量汉人进入内蒙，其中山西移民是主力，从土默特沿黄河西行至达拉特旗、杭锦旗。这种大规模的迁民在《清水河亭志》记载中可窥见一斑:“清水一郡所属幅员辽阔至千余里，所有居民并无土著，大抵皆内地各州县人民流寓，而附近边墙之偏关、平鲁二县人尤为多，其风气各就所隶之地。”',
        '内蒙晋语区的形成与晋商的活动也密切相关。清朝以来，晋商在内蒙一带活动频繁，内蒙包头有句民谚:“先有复盛公，后有包头城”，复盛公即晋商所办买卖字号，包头的兴起与晋商密不可分。'
      ],
      seventhFusionContent: [
        '陕北地区很早就有晋商活动，其地处僻壤，交通不便，商业多靠晋人。(恒山县志》:“邑境地处山岳，交通滞窒，商业贸易不甚发达，.....而经营商人则县民、晋人各居其半.....布匹百货买自山西顺德等地，皮毛羊绒则由晋商洋行岁来收买，邑人经营拙于操纵，偶值金融紧张，周转立窘。”',
        '经过明清以来的移民运动和晋商的商业活动，山西方言逐渐扩散到河北、河南、陕西、内蒙一带，形成今天的山西境外的晋语区。'
      ],
      editList: []
    }
  },
  methods: {
    afterVisibleChange (val) {
      console.log('visible', val)
    },
    showDrawer () {
      this.colors.push(this.color1)
      this.visible = true
    },
    onClose () {
      this.visible = false
    },
    getMessage (path) {
      const params = new URLSearchParams()
      params.append('page',"fusion")
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
    reviseInnerText (path) {
      const params = new URLSearchParams()
      params.append('page',"fusion")
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
    third (index) {
      return 'third' + index
    },
    sixth (index) {
      return 'sixth' + index
    },
    seventh (index) {
      return 'seventh' + index
    }
  },
  created: function () {
    this.getMessage('/display/history/getMessage/')
  }
}
</script>
<style src="../style/history.css" scoped></style>
<style scoped>
h4 {
margin-top: 7px;
text-align: left;
vertical-align: center;
text-indent: 2em;
color: rgba(171, 117, 42);
}
.bgc button{
  margin-top: 20px;
}
</style>
