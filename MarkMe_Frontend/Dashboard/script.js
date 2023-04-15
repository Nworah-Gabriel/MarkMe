var button = document.getElementById('btn')
var modal = document.getElementById('modal')
var form = document.getElementById('form')
var msg = document.getElementById('msg')
var post = document.getElementById('post')
var title = document.getElementById('title')
var table = document.getElementById('table')
var session = document.getElementById('session')
var mark = document.getElementById('mark')
var header = document.getElementById('header')
var close = document.getElementById('close')
button.onclick = function openModal(){
    modal.classList.toggle('modal')
    console.log('clicked')
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    console.log("button clicked");
  
    formValidation();
  });

  let formValidation = () => {
    if (title.value === "") {
      msg.innerHTML = "cannot be blank";
      console.log("failure");
    } else{
        // console.log('success')
        // msg.innerHTML = title.value
        // title.value = ""
        // post.innerHTML = session.value
        // session.value = ""
        acceptData();
        modal.classList.add('modal')
    }
  };
  let data = {};
  let dataTwo = {};
  let acceptData = () => {
    data["text"] = title.value;
    dataTwo["text"] = session.value;
    console.log(data);
    createData()
  };
//add a column id then make a similar create post for it to add the table header once
  let createData = () => {
    table.innerHTML += `
    <tr>
      <td>${data.text}</td>
      <td>${dataTwo.text}</td>
      <td>
        <span class="options">
        <i onClick="markData(this)" class="fa fa-check-square" aria-hidden="true"></i>
        <i onclick="editData(this)" class="fa fa-pencil-square-o" aria-hidden="true"></i>

        </span></td>
    </tr>`;
    title.value =""
    session.value =""
  };
  let markData = (e) => {
    mark.classList.remove('mark')
    header.innerHTML = `<h1>English</h1>`
  };
  function closeModal() {
    mark.classList.add('mark')
  }