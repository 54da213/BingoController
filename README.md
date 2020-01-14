## 关于项目
- 名称：摇奖机
- 版本:1.0

## 运行界面
![运行截图](https://upload-images.jianshu.io/upload_images/19864412-92057bcd764d1751.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 操作
- 点击Start开始，再次点击Over
## 说明

```python
# 随机算法按需修改
def bingo(prize_group):
    random.shuffle(prize_group)
    return random.sample(prize_group, 1)[0]
 ```
```python
# 获取奖池列表按需修改
def get_prize_group(*args, **kwargs):
    return [u"张三", u"李四", u"王五"]