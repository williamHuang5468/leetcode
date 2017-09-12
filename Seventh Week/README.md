# 2017

- [x] 141
- [x] 203
- 160
- 142
- 148
- 42

## 141 尋找 Linked List 中有沒有 Circle

方法一：用 List 把走過的 Node 加進去

速度比較慢

方法二：改良方法一，用 Set 減少需要比較的量

方法三：用奔跑者方法

用兩指針，fast and slow，前者走兩步，後者走一步，當遇到就表示有 Circle，當 fast 遇到 None 表示沒有 Circle

方法四：用例外處理改良奔跑者

將法三的遇到 None 部份，交給例外處理。減少需要 Cover 的部份。

## 203 刪除 Linked List 中的指定元素

- 移動：`node = node.next`
- 刪除元素：`node.next = node.next.next`

方法：
1. 遇到的情況有，刪除的元素在 Linked List 的`首尾`和`中間`。
2. 處理首的方法是：在最前面增加一個輔助節點`Node(0)`
	1. 當首節點元素要刪除，指到下一節點
> 遇到的問題：一開始會用一個變數指向 `None` 作為首節點的表示，但是會遇到對 `None` 操作`.next` 遇到問題。

