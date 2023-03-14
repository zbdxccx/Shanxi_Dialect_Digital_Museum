<template>
  <div class="history-images">
    <a-list :grid="styleGrid" :data-source="intro">
      <a-list-item slot="renderItem" slot-scope="item">
        <a-card :bordered = "false">
          <images-card :title="item.title" :content="item.content" :url='item.url' @turn1="change(item.index)" @turn2="change2()" @transfer="post(item.index)" v-if="item.isShow"></images-card>
        </a-card>
      </a-list-item>
    </a-list>
  </div>
</template>

<script>
import ImagesCard from './ImagesCard.vue'
export default {
  components: { ImagesCard },
  data () {
    return {
      styleGrid: {
        gutter: 16, 
        column: 3
      },
      intro: [
        {
          index: 1,
          title: '古晋语的形成与扩张',
          content: '史前时期,晋语主要受炎帝族和黄帝族两个部落的影响，同时受地理分化形成具有地方差异的晋语；晋国时期晋语随着战争的人口流动而广泛普及；战国时期受韩赵魏三国势力范围不同，区域内进一步形成独具特色的晋语。',
          url: require('../assets/left.jpg'),
          isShow: true
        },
        {
          index: 2,
          title: '古晋语的分化',
          content: '秦汉时期，古晋语分化形成两大方言。古晋语原生地语言与秦地语言靠拢，发展为秦晋方言，古晋语扩展地语言则演变为赵魏方言。在随后的一千多年时间里，这种分化由于行政区划、文化格局等因素逐渐稳定，最终形成今山西境内的两大方言：晋语和中原官话。',
          url: require('../assets/middle.jpg'),
          isShow: true
        },
        {
          index: 3,
          title: '民族融合与境外扩散',
          content: '在与匈奴、西羌、乌桓、鲜卑等少数民族的接触中，山西方言也在潜移默化的被影响着。同时，明清几次移民和晋商活动也让山西方言不断扩散，走向更远的地方。',
          url: require('../assets/right.jpg'),
          isShow: true
        }
      ]
    }
  },
  methods: {
    post (index) {
      this.$emit("prefer",index)
    },
    change(index) {
      for(let i = 0;i<this.intro.length;i++){
        if(this.intro[i].index === index) {
          continue
        }
        this.intro[i].isShow = false
        this.styleGrid.column = 1
      }
    },
    change2 () {
      for(let i = 0;i<this.intro.length;i++){
        this.intro[i].isShow = true
      }
      this.styleGrid.column = 3
    }
  }
}
</script>

<style scoped>
.history-images {
  margin: 50px;
}
</style>
