## 请求的url
###https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule

## formdata字段
    i: 狗       输入的词
    from: AUTO  写死
    to: AUTO    写死
    smartresult: dict   写死
    client: fanyideskweb    写死
    doctype: json   写死
    version: 2.1    写死
    keyfrom: fanyi.web  写死
    action: FY_BY_REALTlME  写死
    bv: eff2e73dc527a143fb4d0a678a264090    写死

* salt: 16185849569573  lst加上0-9的随机数
* sign: 89ac5a0029efc2530d0d20344879ef0b    md5加密（"fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@"）  e是用户输出的单词，i是 salt
* lts: 1618584956957  ~~~  时间戳

###js文件
        var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()  时间戳
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Tbh5E8=q6U3EXe+&L[4c@")
        }
    };