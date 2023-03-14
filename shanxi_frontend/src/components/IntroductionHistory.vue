<template>
    <div class="intro-history">
        <h1>{{this.title}}</h1>
        <p>{{this.introduction}}</p>
    </div>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            default: '山西方言历史'
        },
        introduction: {
            type: String,
            default: '山西方言'
        }
    }
}
</script>
<style scoped>
.intro-history {
    text-align: center;
    margin: 50px;
}
h1 {
    font-size: 32px;
    color:rgba(171, 117, 42, 0.6)
}
p {
    display: inline-block;
    vertical-align: middle;
    text-align: left;
    text-indent: 2em;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    max-width: 400px;
    font-size: 20px;
    color: #707070;
    line-height: 30px;
    -webkit-text-size-adjust: 100%;
    -webkit-font-smoothing: antialiased !important;
    font-family: "微软雅黑,'Heiti SC',黑体,Arial";
}
</style>