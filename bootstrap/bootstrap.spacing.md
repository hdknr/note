# 余白: [Spacing](https://getbootstrap.com/docs/4.1/utilities/spacing/)

## 記法

| ブレーク             | 記法                                     |
|---------------------|-----------------------------------------|
| `xs`                | `{property}{sides}-{size}`              |
| `sm`,`md`,`lg`, `xl`| `{property}{sides}-{breakpoint}-{size}` |

## 余白

|`{property}` | 余白           |
|-------------|---------------|
| `m`         | `margin`      |
| `p`         | `padding`     |

## 方向

|`{sides}`| 方向               |
|---------|-------------------|
| `t`     | `top`             | 
| `b`     | `bottom`          | 
| `l`     | `left`            | 
| `r`     | `right`           | 
| `x`     | `left` & `right`  | 
| `y`     | `top` & `bottom`  | 

## サイズ

|`{size}`| サイズ             |
|--------|-------------------|
| `0`    | `$spacer` * 0.00  | 
| `1`    | `$spacer` * 0.25  | 
| `2`    | `$spacer` * 0.50  | 
| `3`    | `$spacer` * 1.00  | 
| `4`    | `$spacer` * 1.50  | 
| `5`    | `$spacer` * 3.00  | 
| `auto` | 自動               |

- $spacerの基準値は `1rem` = `16px`
- $spacers Sassマップ変数にエントリを追加することで、さらにサイズの追加が可能

## モバイルだけ縦方向にパディングを設定する

- `pb-3` で `xs` 含めて top & bottom に 3

~~~html
<div class="pb-3 pb-md-0">
</div>
~~~