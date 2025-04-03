"use strict";

const container = document.getElementById('conitainer');
const input = document.getElementById('input');
const saveBtn = document.getElementById('saveBtn');
const clearBtn = document.getElementById('clearBtn');
const memoList = document.getElementById('memoList');


//保存ボタン
saveBtn.addEventListener('click', function () {
  const trimedInput = input.value.trim()     //入力された文字を取得

  if (trimedInput) {
    const items = JSON.parse(localStorage.getItem('items')) || [];
    items.push(trimedInput);   //新しいメモを追加
    localStorage.setItem('items', JSON.stringify(items));  //更新されたメモをローカルストレージに保存
    input.value = '';


    displayItems();
  } else {
    alert('メモを入力してください');
  }
});

//メモを表示
function displayItems() {
  const items = JSON.parse(localStorage.getItem('items')) || [];
  memoList.replaceChildren(); //一旦リストを空にする
  items.forEach(function (item, index) {
    const li = document.createElement('li');
    li.textContent = item;
    memoList.appendChild(li);

    //削除ボタンの追加
    const delBtn = document.createElement('button');
    delBtn.textContent = '削除';
    delBtn.setAttribute('id', index);
    delBtn.classList.add('delBtnStyle');
    //各メモの削除ボタン
    delBtn.addEventListener('click', function () {
      items.splice(index, 1);
      localStorage.setItem('items', JSON.stringify(items));
      displayItems();
    })
    memoList.append(delBtn);
  });
}

//削除
clearBtn.addEventListener('click', function () {
  localStorage.clear();
  memoList.replaceChildren();
})


displayItems();

