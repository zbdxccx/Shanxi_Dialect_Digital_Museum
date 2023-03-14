<!--
    @description: DialectAudioCard
    @author: longxiaoming
-->
<template>
  <div class="card-main" @click="handleClickCard">
    <div class="left">
      <!-- 名称 -->
      <div class="dialect-audio-card-name text-overflow">
        <span v-html="dialect.name" :title="dialect.name"></span>
      </div>
      <!-- 含义 -->
      <div class="dialect-audio-card-meaning text-overflow">
        <span>含义: </span>
        <span v-html="dialect.meaning" :title="dialect.meaning"></span>
      </div>
      <!-- 分区 -->
      <div class="dialect-audio-card-meaning text-overflow" v-if="dialect.classification">
          <span>分区: </span>
          <span v-html="dialect.classification" :title="dialect.classification"></span>
      </div>
      <!-- 备注 -->
      <div class="dialect-audio-card-remark text-overflow" v-if="dialect.remark">
        <span>备注: </span>
        <span v-html="dialect.remark" :title="dialect.remark"></span>
      </div>
    </div>
    <div class="right">
      <!-- 音频 -->
      <audio ref="audio" :src="dialect.audio_path" v-show="false"></audio>
      <i class="el-icon-video-play" @click.stop="handlePlay"></i>
      <!-- 收藏 -->
      <i class="el-icon-star-off" v-if="!dialect.isFavoured" @click.stop="handleFavour"></i>
      <i class="el-icon-star-on" v-else @click.stop="handleFavour"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: "DialectAudioCard",

  props: {
    data: {
      type: Object,
      default: () => {
        return {};
      },
    },
    highlightWord: {
      type: String,
      default: "",
    },
    autoPost: {
      type: Boolean,
      default: true,
    },
  },

  data() {
    return {
      dialect: {},
    };
  },

  methods: {
    handleFavour() {
      this.$emit("favour", this.dialect);
    },
    handleClickCard() {
      if (this.$route.path.toLowerCase() === "/dialectdisplay") {
        this.$emit("click-card", this.dialect);
      } else {
        this.$router.push({
          path: "/DialectDisplay",
          query: {
            dialectId: this.dialect.id,
          },
        });
      }
    },
    handlePlay() {
      // 先判断是否有音频,音频是否能正常播放
      if (this.dialect.audio_path) {
        console.log(this.$refs.audio.error);
        if (this.$refs.audio.error) {
          this.$message.error("音频文件无法播放");
        } else {
          this.$refs.audio.play();
        }
      }
    },
    highlight(word) {
      if (word) {
        this.dialect.name = this.data.name.replace(
          word,
          `<span style="color: red;">${word}</span>`
        );
        this.dialect.meaning = this.data.meaning.replace(
          word,
          `<span style="color: red;">${word}</span>`
        );
      } else{
        this.dialect.name = this.data.name;
        this.dialect.meaning = this.data.meaning;
      }
    },
  },

  mounted() {
    this.dialect = JSON.parse(JSON.stringify(this.data));
    this.highlight(this.highlightWord);
  },

  watch: {
    highlightWord(newVal, oldVal) {
        this.highlight(newVal);
    },
  },
};
</script>

<style scoped>
.card-main {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  background: rgb(237, 231, 215);
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
  padding: 4px;
  /* 出现动画, 由浅到深, 从左到右 */
  animation: fadeIn 1s;
  -moz-animation: fadeIn 1s; /* Firefox */
  -webkit-animation: fadeIn 1s; /* Safari and Chrome */
  -o-animation: fadeIn 1s; /* Opera */
  cursor: pointer;
}
.card-main:hover {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.3);
}
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateX(-100px);
  }
  100% {
    opacity: 1;
    transform: translateX(0);
  }
}
.right {
  flex: 0 0 80px;
  height: 100%;
  font-size: 30px;
  padding-top: 10px;
}
.left {
  flex: 1;
  height: 100%;
  text-align: left;
}
.dialect-audio-card-name {
  font-size: 30px;
}
.dialect-audio-card-meaning {
  font-size: 20px;
}
.dialect-audio-card-remark {
  font-size: 17px;
}
.right i {
  cursor: pointer;
}
.right i:hover {
  color: #409eff;
}
.text-overflow {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>