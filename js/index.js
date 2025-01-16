const siteContent = [
  "专题文章:什么是python来源：python程序与设计社团 发布时间：2024-11-29 08:40:34",
  "最新公告——上课要准备的东西来源：python程序与设计社团 发布时间：2024-11-29 07:51:34 ",
];

let input = document.getElementById("input");
let btn = document.getElementById("btn");
let output = document.getElementById("output");

btn.onclick = function () {
  let text = input.value;
  let result = text.replace(/[a-zA-Z0-9]/g, "*");
  output.innerHTML = result;
};
