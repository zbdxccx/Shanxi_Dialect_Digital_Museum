<template>
    <div class="show-images"  @mouseenter="changeIsOver()" @mouseleave="changeIsOver1()" @click="isClick()">
        <img :src="url" alt="" :class="setClass()">
        <a-card :title="title" :headStyle="{color:'rgba(171, 117, 42)'}" class="card-style" v-if="this.isOver" :hoverable = "true" :bordered = "false">
            <a class="content">点击查看具体内容</a>
        </a-card>
        <transition>
          <introduction-history v-show="this.isOver" :title="title" :introduction="content"></introduction-history>
        </transition>
   </div>
</template>

<script>
import IntroductionHistory from './IntroductionHistory.vue'
export default {
  components: { IntroductionHistory },
  props: {
    title: {
      type: String,
      default: '山西方言历史'
    },
    content: {
      type: String,
      default: 'hello'
    },
    url: {
      type: String,
      default: '../assets/logo.png'
    }
  },
  data () {
    return {
      isOver: false
    }
  },
  methods: {
    setClass () {
      if (this.isOver) {
        return 'flip-vertical-bck'
      } else {
        return 'simple'
      }
    },
    changeIsOver () {
      this.isOver = !this.isOver
      this.$emit('turn1')
    },
    changeIsOver1 () {
      this.isOver = !this.isOver
      this.$emit('turn2')
    },
    isClick () {
      this.$emit('transfer')
    }
  }
}
</script>

<style scoped>
.content {
  text-align: left;
  text-indent: 2em;
}
.show-images {
  position: relative;
  display: flex;
  min-height: 400px;
}
a {
  text-decoration: none;
  outline: none;
  color:rgba(171, 117, 42, 0.6)
}
.simple{
  height: 100%;
}
.card-style{
  position: absolute;
  top: 50%;
  width: 31%;
  margin-left: 1%;
  margin-right: 1%;
}
.flip-vertical-bck {
  width: 33%;
  -webkit-animation: flip-vertical-bck 0.5s ;
  animation: flip-vertical-bck 0.5s ;
  opacity:0.4;
  animation-fill-mode:forwards;
}
.v-enter-active {
    animation: move 0.5s;
}
@keyframes move {
    from {
        transform: translateX(100%);
    }
    to {
        transform: translate(0);
    }
}
 @-webkit-keyframes flip-vertical-bck {
  0% {
    -webkit-transform: translateZ(0) rotateY(0);
            transform: translateZ(0) rotateY(0);
  }
  100% {
    -webkit-transform: translateZ(-260px) rotateY(-180deg);
            transform: translateZ(-260px) rotateY(-180deg);
  }
}
@keyframes flip-vertical-bck {
  0% {
    -webkit-transform: translateZ(0) rotateY(0);
            transform: translateZ(0) rotateY(0);
  }
  100% {
    -webkit-transform: translateZ(-260px) rotateY(-180deg);
            transform: translateZ(-260px) rotateY(-180deg);
  }
}
</style>
